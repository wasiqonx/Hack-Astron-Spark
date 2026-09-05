#!/usr/bin/env python3
"""
Spark-X2.5 File Scanner & Analyzer
Scans files in current folder and allows you to ask questions about them
"""

import subprocess
import sys
import os
import json
import re
from pathlib import Path
import argparse
from typing import List, Dict, Any

# Configuration
SPARK_MLX_PATH = "/Users/wasiq/Projects/Private/Spark/Spark-MLX-LLM/.venv/bin/spark-mlx-generate"
MODEL_NAME = "XHToken/Spark-X2.5-1.7B"

# File types to scan (extensions)
TEXT_EXTENSIONS = {
    '.txt', '.md', '.py', '.js', '.ts', '.jsx', '.tsx', '.html', '.css', '.scss',
    '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf', '.sh', '.bash',
    '.c', '.cpp', '.h', '.hpp', '.java', '.go', '.rs', '.swift', '.kt', '.rb',
    '.php', '.lua', '.r', '.m', '.mm', '.sql', '.xml', '.csv', '.log'
}

# Binary files to skip
BINARY_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
    '.mp3', '.mp4', '.avi', '.mov', '.wmv',
    '.zip', '.tar', '.gz', '.rar', '.7z',
    '.exe', '.dll', '.so', '.dylib', '.bin',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'
}

class FileScanner:
    def __init__(self, root_dir='.', max_file_size=1024*1024, max_files=50):
        self.root_dir = Path(root_dir)
        self.max_file_size = max_file_size  # 1MB default
        self.max_files = max_files
        self.files_content = []
        self.file_tree = {}
        
    def scan_directory(self):
        """Scan directory and build file tree"""
        print(f"📁 Scanning directory: {self.root_dir}")
        print("-" * 60)
        
        files_found = 0
        total_size = 0
        
        for file_path in self.root_dir.rglob('*'):
            if not file_path.is_file():
                continue
                
            # Skip hidden files
            if file_path.name.startswith('.'):
                continue
                
            # Check extension
            ext = file_path.suffix.lower()
            
            # Skip binary files
            if ext in BINARY_EXTENSIONS:
                continue
                
            # Skip virtual environment
            if '.venv' in str(file_path) or 'venv' in str(file_path):
                continue
                
            # Skip __pycache__
            if '__pycache__' in str(file_path):
                continue
                
            # Check file size
            file_size = file_path.stat().st_size
            if file_size > self.max_file_size:
                continue
                
            files_found += 1
            total_size += file_size
            
            # Store file info
            rel_path = file_path.relative_to(self.root_dir)
            
            # Build file tree
            self._add_to_tree(rel_path, file_size)
            
            # Read text files
            if ext in TEXT_EXTENSIONS or ext == '':
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                    # Truncate very long files
                    if len(content) > 10000:
                        content = content[:10000] + "\n... (truncated)"
                        
                    self.files_content.append({
                        'path': str(rel_path),
                        'size': file_size,
                        'ext': ext,
                        'content': content,
                        'lines': len(content.splitlines())
                    })
                except Exception as e:
                    print(f"⚠️  Could not read {rel_path}: {e}")
            
            if files_found >= self.max_files:
                break
        
        print(f"✅ Scanned {files_found} files ({total_size / 1024:.1f} KB)")
        print(f"📄 Found {len(self.files_content)} text files")
        print("-" * 60)
        
        return self.files_content
    
    def _add_to_tree(self, rel_path, size):
        """Build a simple file tree structure"""
        parts = str(rel_path).split(os.sep)
        current = self.file_tree
        
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                current[part] = {'size': size, 'is_file': True}
            else:
                if part not in current:
                    current[part] = {'is_file': False, 'children': {}}
                current = current[part]['children']
    
    def get_summary(self) -> str:
        """Get a summary of scanned files"""
        summary = f"Scanned directory: {self.root_dir}\n"
        summary += f"Total text files: {len(self.files_content)}\n\n"
        summary += "Files found:\n"
        
        # Group by extension
        ext_count = {}
        for file_info in self.files_content:
            ext = file_info['ext'] or 'no_ext'
            ext_count[ext] = ext_count.get(ext, 0) + 1
        
        for ext, count in sorted(ext_count.items()):
            summary += f"  - {ext or 'no extension'}: {count} files\n"
        
        return summary
    
    def get_full_context(self) -> str:
        """Get full context of all files for the prompt"""
        context = f"# Directory Scan Results\n\n"
        context += f"Root: {self.root_dir}\n"
        context += f"Total files: {len(self.files_content)}\n\n"
        
        context += "## File List and Content\n\n"
        
        for file_info in self.files_content:
            context += f"### File: {file_info['path']}\n"
            context += f"Size: {file_info['size']} bytes, Lines: {file_info['lines']}\n\n"
            context += "```" + (file_info['ext'][1:] if file_info['ext'] else 'text')
            context += "\n"
            context += file_info['content']
            context += "\n```\n\n"
            context += "---\n\n"
        
        return context
    
    def get_file_tree_string(self) -> str:
        """Get a tree representation of files"""
        def render_tree(tree, prefix=""):
            result = ""
            items = sorted(tree.items())
            
            for i, (name, info) in enumerate(items):
                is_last = (i == len(items) - 1)
                connector = "└── " if is_last else "├── "
                
                if info.get('is_file'):
                    size_kb = info['size'] / 1024
                    result += f"{prefix}{connector}{name} ({size_kb:.1f} KB)\n"
                else:
                    result += f"{prefix}{connector}{name}/\n"
                    extension = "    " if is_last else "│   "
                    result += render_tree(info.get('children', {}), prefix + extension)
            
            return result
        
        return render_tree(self.file_tree)

def run_spark(prompt: str, enable_thinking: bool = False, max_tokens: int = 30000, temp: float = 0.7, output_file: str = None):
    """Run spark-mlx-generate with the given prompt"""
    
    cmd = [
        SPARK_MLX_PATH,
        "--model", MODEL_NAME,
        "--prompt", prompt,
        "--max-tokens", str(max_tokens),
        "--temp", str(temp),
        "--device", "gpu",
        "--dtype", "bfloat16"
    ]
    
    print("\n" + "=" * 70)
    print(f"🤖 Spark-X2.5 Analysis")
    print(f"Thinking mode: {'ON' if enable_thinking else 'OFF'}")
    print(f"Max tokens: {max_tokens}, Temperature: {temp}")
    print("=" * 70 + "\n")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        response = result.stdout
        print(response)
        
        # Save solution to separate file if specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(response)
            print(f"\n💾 Solution saved to: {output_file}")
        
        if result.stderr:
            print("\n[Stderr]", result.stderr, file=sys.stderr)
        return response
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error: Command failed with exit code {e.returncode}", file=sys.stderr)
        if e.stdout:
            print("Stdout:", e.stdout, file=sys.stderr)
        if e.stderr:
            print("Stderr:", e.stderr, file=sys.stderr)
        return None
    except FileNotFoundError:
        print(f"\n❌ Error: Could not find spark-mlx-generate at {SPARK_MLX_PATH}", file=sys.stderr)
        return None
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        return None

def interactive_mode(scanner: FileScanner):
    """Interactive mode for asking questions about files"""
    print("\n" + "=" * 70)
    print("💬 Spark-X2.5 Interactive File Analyzer")
    print("=" * 70)
    print("\nCommands:")
    print("  /help           - Show this help")
    print("  /files          - List all scanned files")
    print("  /tree           - Show file tree")
    print("  /summary        - Show summary of scanned files")
    print("  /think ON/OFF   - Toggle thinking mode")
    print("  /quit, /exit    - Exit the program")
    print("  Any other input will be sent as a question")
    print("-" * 70)
    
    thinking_mode = False
    max_tokens = 30000
    temp = 0.7
    output_file = None
    
    # Pre-build context
    context = scanner.get_full_context()
    file_tree = scanner.get_file_tree_string()
    summary = scanner.get_summary()
    
    print(f"\n✅ Loaded {len(scanner.files_content)} files. Ask me anything about them!")
    print(f"💡 Tip: Use /tree to see file structure\n")
    
    while True:
        try:
            user_input = input("\n📝 You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['/quit', '/exit', '/q']:
                print("👋 Goodbye!")
                break
                
            elif user_input.lower() == '/help':
                print("\nCommands:")
                print("  /help           - Show this help")
                print("  /files          - List all scanned files")
                print("  /tree           - Show file tree")
                print("  /summary        - Show summary of scanned files")
                print("  /think ON/OFF   - Toggle thinking mode")
                print("  /save <path>    - Save next response to file")
                print("  /quit, /exit    - Exit the program")
                continue
                
            elif user_input.lower() == '/files':
                print("\n📄 Scanned Files:")
                for i, file_info in enumerate(scanner.files_content, 1):
                    print(f"  {i}. {file_info['path']} ({file_info['lines']} lines, {file_info['size']} bytes)")
                continue
                
            elif user_input.lower() == '/tree':
                print("\n📁 File Tree:")
                print(file_tree)
                continue
                
            elif user_input.lower() == '/summary':
                print("\n📊 Summary:")
                print(summary)
                continue
                
            elif user_input.lower().startswith('/think'):
                parts = user_input.split()
                if len(parts) > 1:
                    if parts[1].upper() == 'ON':
                        thinking_mode = True
                        print("🧠 Thinking mode: ON")
                    elif parts[1].upper() == 'OFF':
                        thinking_mode = False
                        print("🧠 Thinking mode: OFF")
                    else:
                        print(f"❌ Unknown option: {parts[1]}. Use ON or OFF")
                else:
                    print(f"🧠 Thinking mode is currently: {'ON' if thinking_mode else 'OFF'}")
                continue
            
            elif user_input.lower().startswith('/save'):
                parts = user_input.split(maxsplit=1)
                if len(parts) > 1:
                    output_file = parts[1]
                    print(f"💾 Next response will be saved to: {output_file}")
                else:
                    output_file = None
                    print("💾 Save mode disabled")
                continue
            
            # Build the full prompt with context
            full_prompt = f"""You are analyzing files in a project directory. Here is the context:

{context}

Based on the files above, please answer the following question:
{user_input}

Provide a detailed and helpful response based on the file contents."""
            
            print("\n🤔 Analyzing... (this may take a moment)\n")
            
            # Run the analysis
            run_spark(full_prompt, thinking_mode, max_tokens, temp, output_file)
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted")
            continue
        except EOFError:
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Scan files and analyze them with Spark-X2.5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (scan current directory)
  python file_scanner.py
  
  # Scan specific directory
  python file_scanner.py --dir /path/to/project
  
  # Ask a specific question and exit
  python file_scanner.py --question "What does this project do?"
  
  # With thinking mode
  python file_scanner.py --think --question "Find all TODO comments"
  
  # Custom limits
  python file_scanner.py --max-files 100 --max-size 2MB
        """
    )
    
    parser.add_argument(
        '--dir', '-d',
        type=str,
        default='.',
        help='Directory to scan (default: current directory)'
    )
    
    parser.add_argument(
        '--question', '-q',
        type=str,
        help='Ask a specific question and exit (non-interactive mode)'
    )
    
    parser.add_argument(
        '--think',
        action='store_true',
        help='Enable thinking mode'
    )
    
    parser.add_argument(
        '--max-files',
        type=int,
        default=50,
        help='Maximum number of files to scan (default: 50)'
    )
    
    parser.add_argument(
        '--max-size',
        type=str,
        default='1MB',
        help='Maximum file size to read (e.g., 1MB, 500KB) (default: 1MB)'
    )
    
    parser.add_argument(
        '--max-tokens',
        type=int,
        default=30000,
        help='Maximum tokens for response (default: 30000)'
    )
    
    parser.add_argument(
        '--temp',
        type=float,
        default=0.7,
        help='Temperature for generation (default: 0.7)'
    )
    
    parser.add_argument(
        '--output',
        '-o',
        type=str,
        help='Save file context to a file'
    )
    
    parser.add_argument(
        '--save',
        '-s',
        type=str,
        help='Save the solution/response to a separate file'
    )
    
    args = parser.parse_args()
    
    # Parse max size
    size_str = args.max_size.upper()
    if size_str.endswith('MB'):
        max_size = int(float(size_str[:-2]) * 1024 * 1024)
    elif size_str.endswith('KB'):
        max_size = int(float(size_str[:-2]) * 1024)
    else:
        max_size = int(float(size_str))
    
    # Initialize scanner
    scanner = FileScanner(
        root_dir=args.dir,
        max_file_size=max_size,
        max_files=args.max_files
    )
    
    # Scan files
    scanner.scan_directory()
    
    if not scanner.files_content:
        print("❌ No readable text files found in the directory.")
        return
    
    # Save context if requested
    if args.output:
        context = scanner.get_full_context()
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(context)
        print(f"✅ Context saved to: {args.output}")
        return
    
    # Handle single question mode
    if args.question:
        context = scanner.get_full_context()
        full_prompt = f"""You are analyzing files in a project directory. Here is the context:

{context}

Based on the files above, please answer the following question:
{args.question}

Provide a detailed and helpful response based on the file contents."""
        
        run_spark(full_prompt, args.think, args.max_tokens, args.temp, args.save)
        return
    
    # Interactive mode
    interactive_mode(scanner)

if __name__ == "__main__":
    main()
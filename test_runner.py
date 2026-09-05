#!/usr/bin/env python3
"""
Spark Model Test Runner - Menu Driven
Automatically runs and evaluates tests for Spark-X2.5-1.7B model
"""

import subprocess
import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime

# Configuration
SPARK_MLX_PATH = "/Users/<REDACTED>/Projects/Private/Spark/Spark-MLX-LLM/.venv/bin/spark-mlx-generate" # Add Your Own Spark-MLX-PATH
MODEL_NAME = "XHToken/Spark-X2.5-1.7B"
BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / "test_results_by_test_runner_script"

# Test definitions
THINKING_MODE_ON_TESTS = [
    {
        "id": "TM_ON_001",
        "name": "Car Wash Problem",
        "prompt": "If my carwash is 1km away ? Should I take the car or not ?",
        "max_tokens": 154,
        "temp": 0,
        "expected_keywords": ["yes", "short distance", "take the car"],
        "category": "General Knowledge"
    },
    {
        "id": "TM_ON_002",
        "name": "Simple Addition",
        "prompt": "Is 44+98=128 ?",
        "max_tokens": 10000,
        "temp": 0,
        "expected_keywords": ["yes", "142"],
        "category": "Math",
        "note": "Model incorrectly says 128 - known failure"
    },
    {
        "id": "TM_ON_003",
        "name": "Hair or Phone Riddle",
        "prompt": "What comes first hair or phone ?",
        "max_tokens": 10000,
        "temp": 0,
        "expected_keywords": ["hair", "phone"],
        "category": "Riddle",
        "note": "Model crashes due to memory - known failure"
    },
    {
        "id": "TM_ON_004",
        "name": "Cow Mow Riddle",
        "prompt": "A cow mows 5 times a day. Which mow is not related to any event on Timeline ?",
        "max_tokens": 10000,
        "temp": 0,
        "expected_keywords": ["mow", "timeline"],
        "category": "Riddle"
    },
    {
        "id": "TM_ON_005",
        "name": "Cat and Fishes (8 fishes)",
        "prompt": "A cat eats 8 fishes in a day. But the owner has only 20 fishes. How many days can cat eat ?",
        "max_tokens": 10000,
        "temp": 0,
        "expected_keywords": ["2", "days", "8", "fishes"],
        "category": "Math"
    },
]

THINKING_MODE_OFF_TESTS = [
    {
        "id": "TM_OFF_001",
        "name": "Simple Addition (55+88)",
        "prompt": "Is 55+88=143 ?",
        "max_tokens": 10000,
        "temp": 0,
        "expected_keywords": ["yes", "55+88=143", "143"],
        "category": "Math"
    },
    {
        "id": "TM_OFF_002",
        "name": "Car Wash Problem",
        "prompt": "Does it make sense to take the car ?",
        "max_tokens": 10000,
        "temp": 0,
        "expected_keywords": ["depends", "context"],
        "category": "General Knowledge"
    },
    {
        "id": "TM_OFF_003",
        "name": "Capital of Delhi",
        "prompt": "What is the capital of Delhi ?",
        "max_tokens": 10000,
        "temp": 0,
        "expected_keywords": ["New Delhi", "capital"],
        "category": "General Knowledge"
    },
    {
        "id": "TM_OFF_004",
        "name": "Cat and Fishes (9 fishes)",
        "prompt": "A cat eats 9 fishes in a day. But the owner has only 21 fishes. At least how many days and hours could a cat survive?",
        "max_tokens": 10000,
        "temp": 0,
        "expected_keywords": ["2", "days", "8", "hours", "9", "fishes"],
        "category": "Math"
    },
]

MULTIPLE_ANSWER_TESTS = [
    {
        "id": "MA_001",
        "name": "HTML Table with 20 Countries",
        "prompt": "scan question.txt and answer it",
        "files": ["question.txt"],
        "expected_output_file": "countries.html",
        "expected_keywords": ["html", "table", "country"],
        "category": "File Analysis"
    },
    {
        "id": "MA_002",
        "name": "C Code Error Analysis",
        "prompt": "Check the make.C for error",
        "files": ["make.C"],
        "expected_keywords": ["error", "int", "b=02"],
        "category": "Code Analysis",
        "note": "Model hallucinates error - known issue"
    },
]

class TestRunner:
    """Main test runner class"""
    
    def __init__(self):
        self.results = []
        self.ensure_directories()
    
    def ensure_directories(self):
        """Create necessary directories"""
        RESULTS_DIR.mkdir(exist_ok=True)
        (RESULTS_DIR / "Thinking_Mode_On").mkdir(exist_ok=True)
        (RESULTS_DIR / "Thinking_Mode_Off").mkdir(exist_ok=True)
        (RESULTS_DIR / "Multiple_Answer").mkdir(exist_ok=True)
    
    def run_spark_command(self, prompt, max_tokens=10000, temp=0, think=False):
        """Run spark-mlx-generate command and return output"""
        cmd = [
            SPARK_MLX_PATH,
            "--model", MODEL_NAME,
            "--prompt", prompt,
            "--max-tokens", str(max_tokens),
            "--temp", str(temp),
            "--device", "gpu",
            "--dtype", "bfloat16"
        ]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
                "success": result.returncode == 0
            }
        except subprocess.TimeoutExpired:
            return {
                "stdout": "",
                "stderr": "Command timed out after 300 seconds",
                "returncode": -1,
                "success": False,
                "timeout": True
            }
        except Exception as e:
            return {
                "stdout": "",
                "stderr": str(e),
                "returncode": -1,
                "success": False
            }
    
    def evaluate_response(self, response, test):
        """Evaluate if response meets test criteria"""
        if not response["success"]:
            return {
                "passed": False,
                "reason": f"Command failed: {response.get('stderr', 'Unknown error')[:200]}"
            }
        
        output = response["stdout"].lower()
        expected_keywords = test.get("expected_keywords", [])
        expected_not_keywords = test.get("expected_not_keywords", [])
        
        missing_keywords = []
        for keyword in expected_keywords:
            if keyword.lower() not in output:
                missing_keywords.append(keyword)
        
        found_not_keywords = []
        for keyword in expected_not_keywords:
            if keyword.lower() in output:
                found_not_keywords.append(keyword)
        
        passed = len(missing_keywords) == 0 and len(found_not_keywords) == 0
        
        reason = ""
        if missing_keywords:
            reason += f"Missing keywords: {', '.join(missing_keywords)}. "
        if found_not_keywords:
            reason += f"Found unwanted keywords: {', '.join(found_not_keywords)}."
        
        return {
            "passed": passed,
            "reason": reason if reason else "All criteria met",
            "missing_keywords": missing_keywords,
            "found_not_keywords": found_not_keywords
        }
    
    def _save_log(self, log_file, test, result, response, evaluation, elapsed_time):
        """Save detailed log to file"""
        with open(log_file, "w") as f:
            f.write(f"Test: {test['name']}\n")
            f.write(f"ID: {test['id']}\n")
            f.write(f"Category: {test['category']}\n")
            f.write(f"Prompt: {test['prompt']}\n")
            f.write(f"Timestamp: {result['timestamp']}\n")
            f.write(f"Elapsed Time: {elapsed_time:.2f}s\n")
            f.write(f"Passed: {evaluation['passed']}\n")
            f.write(f"Reason: {evaluation['reason']}\n")
            f.write(f"\n{'='*60}\n")
            f.write("RESPONSE:\n")
            f.write(f"{'='*60}\n")
            f.write(response["stdout"])
            if response["stderr"]:
                f.write(f"\n{'='*60}\n")
                f.write("STDERR:\n")
                f.write(f"{'='*60}\n")
                f.write(response["stderr"])
    
    def run_thinking_mode_on_test(self, test):
        """Run a single Thinking Mode On test"""
        print(f"\n{'='*60}")
        print(f"Running: {test['name']} ({test['id']})")
        print(f"Prompt: {test['prompt'][:80]}...")
        print(f"{'='*60}")
        
        start_time = time.time()
        response = self.run_spark_command(
            prompt=test["prompt"],
            max_tokens=test["max_tokens"],
            temp=test["temp"],
            think=True
        )
        elapsed_time = time.time() - start_time
        
        evaluation = self.evaluate_response(response, test)
        
        result = {
            "test_id": test["id"],
            "test_name": test["name"],
            "category": test["category"],
            "prompt": test["prompt"],
            "response": response["stdout"][:1000] if response["stdout"] else "",
            "success": response["success"],
            "passed": evaluation["passed"],
            "evaluation_reason": evaluation["reason"],
            "elapsed_time": elapsed_time,
            "timestamp": datetime.now().isoformat()
        }
        
        log_file = RESULTS_DIR / "Thinking_Mode_On" / f"{test['id']}.log"
        self._save_log(log_file, test, result, response, evaluation, elapsed_time)
        
        status = "PASSED" if evaluation["passed"] else "FAILED"
        print(f"Result: {status}")
        print(f"Time: {elapsed_time:.2f}s")
        if not evaluation["passed"]:
            print(f"Reason: {evaluation['reason']}")
        
        self.results.append(result)
        return result
    
    def run_thinking_mode_off_test(self, test):
        """Run a single Thinking Mode Off test"""
        print(f"\n{'='*60}")
        print(f"Running: {test['name']} ({test['id']})")
        print(f"Prompt: {test['prompt'][:80]}...")
        print(f"{'='*60}")
        
        start_time = time.time()
        response = self.run_spark_command(
            prompt=test["prompt"],
            max_tokens=test["max_tokens"],
            temp=test["temp"],
            think=False
        )
        elapsed_time = time.time() - start_time
        
        evaluation = self.evaluate_response(response, test)
        
        result = {
            "test_id": test["id"],
            "test_name": test["name"],
            "category": test["category"],
            "prompt": test["prompt"],
            "response": response["stdout"][:1000] if response["stdout"] else "",
            "success": response["success"],
            "passed": evaluation["passed"],
            "evaluation_reason": evaluation["reason"],
            "elapsed_time": elapsed_time,
            "timestamp": datetime.now().isoformat()
        }
        
        log_file = RESULTS_DIR / "Thinking_Mode_Off" / f"{test['id']}.log"
        self._save_log(log_file, test, result, response, evaluation, elapsed_time)
        
        status = "PASSED" if evaluation["passed"] else "FAILED"
        print(f"Result: {status}")
        print(f"Time: {elapsed_time:.2f}s")
        if not evaluation["passed"]:
            print(f"Reason: {evaluation['reason']}")
        
        self.results.append(result)
        return result
    
    def run_multiple_answer_test(self, test):
        """Run a single Multiple-Answer test using scanner.py"""
        print(f"\n{'='*60}")
        print(f"Running: {test['name']} ({test['id']})")
        print(f"Prompt: {test['prompt'][:80]}...")
        print(f"{'='*60}")
        
        ma_dir = BASE_DIR / "Multiple-Answer"
        
        cmd = [
            sys.executable,
            str(ma_dir / "scanner.py"),
            "--question", test["prompt"],
            "--dir", str(ma_dir),
            "--max-tokens", "2048",
            "--temp", "0.7"
        ]
        
        start_time = time.time()
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,
                cwd=str(ma_dir)
            )
            response = {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
                "success": result.returncode == 0
            }
        except subprocess.TimeoutExpired:
            response = {
                "stdout": "",
                "stderr": "Command timed out",
                "returncode": -1,
                "success": False
            }
        except Exception as e:
            response = {
                "stdout": "",
                "stderr": str(e),
                "returncode": -1,
                "success": False
            }
        
        elapsed_time = time.time() - start_time
        evaluation = self.evaluate_response(response, test)
        
        result_data = {
            "test_id": test["id"],
            "test_name": test["name"],
            "category": test["category"],
            "prompt": test["prompt"],
            "response": response["stdout"][:1000] if response["stdout"] else "",
            "success": response["success"],
            "passed": evaluation["passed"],
            "evaluation_reason": evaluation["reason"],
            "elapsed_time": elapsed_time,
            "timestamp": datetime.now().isoformat()
        }
        
        log_file = RESULTS_DIR / "Multiple_Answer" / f"{test['id']}.log"
        self._save_log(log_file, test, result_data, response, evaluation, elapsed_time)
        
        status = "PASSED" if evaluation["passed"] else "FAILED"
        print(f"Result: {status}")
        print(f"Time: {elapsed_time:.2f}s")
        if not evaluation["passed"]:
            print(f"Reason: {evaluation['reason']}")
        
        self.results.append(result_data)
        return result_data
    
    def run_all_thinking_mode_on(self):
        """Run all Thinking Mode On tests"""
        print("\n" + "="*60)
        print("RUNNING ALL THINKING MODE ON TESTS")
        print("="*60)
        
        for test in THINKING_MODE_ON_TESTS:
            self.run_thinking_mode_on_test(test)
        
        self.print_summary("Thinking Mode On")
    
    def run_all_thinking_mode_off(self):
        """Run all Thinking Mode Off tests"""
        print("\n" + "="*60)
        print("RUNNING ALL THINKING MODE OFF TESTS")
        print("="*60)
        
        for test in THINKING_MODE_OFF_TESTS:
            self.run_thinking_mode_off_test(test)
        
        self.print_summary("Thinking Mode Off")
    
    def run_all_multiple_answer(self):
        """Run all Multiple-Answer tests"""
        print("\n" + "="*60)
        print("RUNNING ALL MULTIPLE-ANSWER TESTS")
        print("="*60)
        
        for test in MULTIPLE_ANSWER_TESTS:
            self.run_multiple_answer_test(test)
        
        self.print_summary("Multiple-Answer")
    
    def run_all_tests(self):
        """Run all tests"""
        print("\n" + "="*60)
        print("RUNNING ALL TESTS")
        print("="*60)
        
        self.run_all_thinking_mode_on()
        self.run_all_thinking_mode_off()
        self.run_all_multiple_answer()
        
        self.print_summary("All Tests")
        self.save_final_report()
    
    def print_summary(self, title):
        """Print test summary"""
        print("\n" + "="*60)
        print(f"{title} - TEST SUMMARY")
        print("="*60)
        
        passed = sum(1 for r in self.results if r["passed"])
        total = len(self.results)
        
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Pass Rate: {(passed/total*100):.1f}%" if total > 0 else "N/A")
        
        print("\nDetailed Results:")
        print("-" * 60)
        for r in self.results:
            status = "PASS" if r["passed"] else "FAIL"
            print(f"{status} | {r['test_id']} | {r['test_name'][:40]:<40} | {r['elapsed_time']:.2f}s")
        print("="*60)
    
    def save_final_report(self):
        """Save final report to file"""
        report_file = RESULTS_DIR / f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(report_file, "w") as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "total_tests": len(self.results),
                "passed": sum(1 for r in self.results if r["passed"]),
                "failed": sum(1 for r in self.results if not r["passed"]),
                "results": self.results
            }, f, indent=2)
        
        print(f"\nFull report saved to: {report_file}")
    
    def run_custom_test(self):
        """Run a custom test with user input"""
        print("\n" + "="*60)
        print("CUSTOM TEST")
        print("="*60)
        
        prompt = input("Enter your prompt: ").strip()
        if not prompt:
            print("No prompt entered. Returning to menu.")
            return
        
        max_tokens = input("Max tokens (default: 10000): ").strip()
        max_tokens = int(max_tokens) if max_tokens else 10000
        


def print_menu():
    """Print main menu"""
    print("\n" + "="*60)
    print("   SPARK MODEL TEST RUNNER")
    print("   Automated Testing & Evaluation")
    print("="*60)
    print("1. Run All Tests")
    print("2. Run Thinking Mode On Tests")
    print("3. Run Thinking Mode Off Tests")
    print("4. Run Multiple-Answer Tests")
    print("5. Run Custom Test")
    print("6. View Last Results")
    print("7. Exit")
    print("="*60)


def main():
    """Main function"""
    runner = TestRunner()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            runner.results = []
            runner.run_all_tests()
        elif choice == "2":
            runner.results = []
            runner.run_all_thinking_mode_on()
        elif choice == "3":
            runner.results = []
            runner.run_all_thinking_mode_off()
        elif choice == "4":
            runner.results = []
            runner.run_all_multiple_answer()
        elif choice == "5":
            runner.run_custom_test()
        elif choice == "6":
            if runner.results:
                runner.print_summary("Last Test Run")
            else:
                print("\nNo results to display. Run some tests first.")
        elif choice == "7":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
# Submission for Tests Conducted on Spark-1.7B Model 

Tested it with Various Coding tasks and Multi-Lingual Tests to produce answers 

Running it on Apple M3-Pro 8GB Unified Memory,

- **Environment:**
  - macOS
  - MacBook Pro
  - Apple M3
  - 8 GB unified memory
  - Revision- `448e61eb392c00f2c403185c5b56d5e0665bfaab`
  - SHA256 Spark 1.7B Model - `b1629719b3f6de5de922abb3c90e45927550dd6f790f43030dc812cafce1af87`
  - Total Size- 3415314432
  - `spark-mlx-generate`
  - Python: `[3.14.7]`
  - MLX / Spark-MLX-LLM: `[0.1.0]`

## Steps to Reproduce Results

An automated test runner (`test_runner.py`) is provided to reproduce all results.

### Prerequisites
- Python 3.14.7
- MLX / Spark-MLX-LLM 0.1.0
- XHToken/Spark-X2.5-1.7B model downloaded

### Setup Virtual Environment

Before running the tests, set up a Python virtual environment:

```bash
# Navigate to project directory
cd /Users/wasiq/Projects/Private/Spark/Final/Hack-Astron-Spark

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Note:** Make sure to update the `SPARK_MLX_PATH` in `test_runner.py` to point to your spark-mlx-generate executable:
```python
# In test_runner.py, update this line:
SPARK_MLX_PATH = "/Users/wasiq/Projects/Private/Spark/Spark-MLX-LLM/.venv/bin/spark-mlx-generate"
```

### Run All Tests
```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Run the test runner
python3 test_runner.py
```

### Test Runner Menu Options
1. **Run All Tests** - Runs all 11 tests across all categories
2. **Run Thinking Mode On Tests** - Runs 5 thinking mode tests
3. **Run Thinking Mode Off Tests** - Runs 4 non-thinking tests
4. **Run Multiple-Answer Tests** - Runs 2 file scanner tests
5. **Run Custom Test** - Enter your own prompt to test
6. **View Last Results** - Shows summary of last test run
7. **Exit** - Quit the program

### Test Categories

#### Thinking Mode On (5 tests)
| Test ID | Name | Category | Prompt |
|---------|------|----------|--------|
| TM_ON_001 | Car Wash Problem | General Knowledge | If my carwash is 1km away ? Should I take the car or not ? |
| TM_ON_002 | Simple Addition | Math | Is 44+98=128 ? |
| TM_ON_003 | Hair or Phone Riddle | Riddle | What comes first hair or phone ? |
| TM_ON_004 | Cow Mow Riddle | Riddle | A cow mows 5 times a day... |
| TM_ON_005 | Cat and Fishes (8 fishes) | Math | A cat eats 8 fishes in a day... |

#### Thinking Mode Off (4 tests)
| Test ID | Name | Category | Prompt |
|---------|------|----------|--------|
| TM_OFF_001 | Simple Addition (55+88) | Math | Is 55+88=143 ? |
| TM_OFF_002 | Car Wash Problem | General Knowledge | Does it make sense to take the car ? |
| TM_OFF_003 | Capital of Delhi | General Knowledge | What is the capital of Delhi ? |
| TM_OFF_004 | Cat and Fishes (9 fishes) | Math | A cat eats 9 fishes in a day... |

#### Multiple-Answer (2 tests)
| Test ID | Name | Category | Prompt |
|---------|------|----------|--------|
| MA_001 | HTML Table with 20 Countries | File Analysis | scan question.txt and answer it |
| MA_002 | C Code Error Analysis | Code Analysis | Check the make.C for error |

### Output
- Results saved to `test_results/` directory
- Individual log files for each test
- JSON report with all results (`test_results/test_report_*.json`)

### Expected Test Duration
- Thinking Mode On tests: ~30-60 seconds each
- Thinking Mode Off tests: ~30-60 seconds each
- Multiple-Answer tests: ~100-120 seconds each
- **Total estimated time: ~15-20 minutes for all tests**



## Thinking Model Spark

| Category | Example 1 | Example 2 | Example 3 | Example 4 | Example 5 | Example 6 | Example 7 | Example 8 | Example 9 |
|---|---|---|---|---|---|---|---|---|---|
| Model | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B |
| Runtime | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM |
| Runtime version | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] |
| Hardware | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory |
| GPU driver | MLX GPU | MLX GPU | MLX GPU | MLX GPU | MLX GPU | MLX GPU | MLX GPU | MLX GPU | MLX GPU |
| Precision | BF16 | BF16 | BF16 | BF16 | BF16 | BF16 | BF16 | BF16 | BF16 |
| Context length | 1137 | 10023 | 10023 | 112 | 383 | 1049 | 255 | 10063 | 820 |
| Batch size | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Peak Memory | 4.009 GB | Errored | Errored | 3.456 GB | 3.461 GB | 3.461 GB | 3.469 GB | 3.649 GB | 3.495 GB |
| max_tokens | 154 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 |
| Temperature | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Input length | 783 tokens | 23 | 23 | 23 | 26 | 39 | 39 | 63 | 59 |
| Tokens per second [Input] | 778.865 tokens-per-sec | - | 136.121 tokens-per-sec | 136.121 tokens-per-sec | 53.696 tokens-per-sec | 152.609 tokens-per-sec | 169.146 tokens-per-sec | 265.597 tokens-per-sec | 315.884 tokens-per-sec |
| Tokens per second [Output] | 25.750 tokens-per-sec | - | 25.697 tokens-per-sec | 25.697 tokens-per-sec | 25.152 tokens-per-sec | 24.488 tokens-per-sec | 26.258 tokens-per-sec | 24.256 tokens-per-sec | 26.179 tokens-per-sec |
| Output length | 354 tokens | 10000 | 10000 | 89 | 357 | 1019 | 216 | 10000 | 10000 |
| RunTime | 78.13 seconds | 411 | 411 seconds | 23 seconds | 72.18s | 70.78s | 36.73s | 474.24 | 50.95s |
| Thinking Mode | On | Off | On | On | On | On | On | On | Off |

### Example 1: Car Wash Problem

- **Raw model output:**

```text
The repository /Users/<REDACTED>/.cache/huggingface/hub/models—
XHToken--Spark-X2.5-1.7B/snapshots/
448e61eb392c00f2c403185c5b56d5e0665bfaab
```

**Prompt:**
```text
If my carwash is 1km away ? Should I take the car or not ?
```

**Spark output:**
```text
We must answer directly and concisely, without reasoning.
The user is asking whether to take their car or not if the carwash is 1km away. We need to provide a concise answer.We should consider: 1km is a short distance, so it's likely fine to take the car. But we need to give a direct answer.
Possible answer: "Yes, it's fine to take the car because 1km is a short distance."
But we need to be concise. Maybe: "Yes, 1km is a short distance, so you can take the car."
But the instruction says "Answer directly and concisely." So we can just say: "Yes, it's fine to take the car."
However, we should also consider if there are any other factors, but the question is simple.
Let's craft a concise response.
I'll respond: "Yes, 1km is a short distance, so you can take the car."
But to be even more direct: "Yes, it's fine to take the car."
I'll go with: "Yes, 1km is a short distance, so you can take the car."
But the user might want a more definitive answer. I'll provide a clear, concise answer.
Final answer: "Yes, 1km is a short distance, so you can take the car."</think>
```

### Example 2: Simple Addition 

**Prompt:**
```text
Is 44+98=128 ?
```

**Spark output:**
```text
The user is asking a simple arithmetic question. We should answer yes or no, and maybe provide the result. But the instruction says "Answer directly and concisely." So we can just say "Yes, 44+98=128." or "Yes, 128." But to be direct, we can say "Yes, 44+98=128."
However, the assistant's previous responses were very long and included repository information, but that was because the user was asking about a model. Now the user is asking a simple math question. So we should just answer the math question.
We must not provide reasoning or thinking section. So we just output the answer.
Thus, the answer should be: "Yes, 44+98=128."
But to be even more concise: "Yes, 128."
I'll go with: "Yes, 44+98=128."
That is direct and concise.</think>Yes, 44+98=128.
```

### Example 3: Reasoning Based Riddle

## Failure with Spark

When given a riddle based question even though its not it’s in thinking loop and crashes due to memory being overloaded eg “What comes first x or y ?” X and y being two objects being compared to.

**Prompt:**
```text
What comes first hair or phone ?
```

**Spark output:** [OUTPUT](https://github.com/wasiqonx/Hack-Astron-Spark/blob/main/Thinking%20Mode%20On/logs/Reasoning.log#L6)

If the `max_tokens` are increased by 10x that is `100000` it just crashes.

```text
raceback (most recent call last):
  File "/Users/<REDACTED>/Projects/Private/Spark/Spark-MLX-LLM/.venv/bin/spark-mlx-generate", line 6, in <module>
    sys.exit(main())
  ~~~~^^
  File "/Users/<REDACTED>/Projects/Private/Spark/Spark-MLX-LLM/spark_mlx_llm/cli.py", line 60, in main
    generate(
    ~~~~~~~~^
        model,
        ^^^^^^
        ...<4 lines>...
        verbose=True,
        ^^^^^^^^^^^^^
    )
    ^
  File "/Users//Projects/Private/Spark/Spark-MLX-LLM/.venv/lib/python3.14/site-packages/mlx_lm/generate.py", line 779, in generate
    for response in stream_generate(model, tokenizer, prompt, **kwargs):
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/<REDACTED>/Projects/Private/Spark/Spark-MLX-LLM/.venv/lib/python3.14/site-packages/mlx_lm/generate.py", line 716, in stream_generate
    for n, (token, logprobs, from_draft) in enumerate(token_generator):
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/<REDACTED>/Projects/Private/Spark/Spark-MLX-LLM/.venv/lib/python3.14/site-packages/mlx_lm/generate.py", line 706, in <genexpr>
    (token, logprobs, False) for token, logprobs in token_generator
                                      ^^^^^^^^^^^
  File "/Users/<REDACTED>/Projects/Private/Spark/Spark-MLX-LLM/.venv/lib/python3.14/site-packages/mlx_lm/generate.py", line 460, in generate_step
    mx.async_eval(next_y, next_logprobs)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: [METAL] Command buffer execution failed: Insufficient Memory (00000008:kIOGPUCommandBufferCallbackErrorOutOfMemory).
```

**Prompt:**
```text
What is the capital of Delhi ?
```

**Spark output:**
```text
We are asked: "What is the Capital of Delhi ?" This is a straightforward factual question. The capital of Delhi is New Delhi. However, note that Delhi is a union territory, and its capital is New Delhi. Sometimes people might say Delhi, but the official capital is New Delhi. So the answer should be New Delhi.

Let's provide a clear and concise answer.</think>The capital of Delhi is **New Delhi**.
```

### Example 4:

**Prompt:**
```text
क्या बाघ बिल्ली है?
```

**Spark output:**
```text
उपयोगकर्ता ने "क्या बाघ बिल्ली है?" का प्रश्न पूछा है। यह एक सामान्य प्रश्न है जो प्राकृतिक तत्वों के बारे में पूछता है।
मुझे स्पष्ट रूप से उत्तर देना चाहिए कि बाघ और बिल्ली एक ही प्रजाति का है। यह एक स्पष्ट और तथ्यात्मक उत्तर होना चाहिए।
मुझे यह सुनिश्चित करना चाहिए कि उत्तर सटीक हो और संदर्भ के अनुसार सही हो। बाघ और बिल्ली एक ही प्रजाति का है, इसलिए मैं इसे स्पष्ट रूप से बताऊंगा।
मुझे यह भी ध्यान रखना चाहिए कि उत्तर संक्षिप्त और स्पष्ट होना चाहिए, क्योंकि उपयोगकर्ता ने सीधे प्रश्न पूछा है। मैं इसके बजाय तथ्यात्मक और स्पष्ट उत्तर दे सकता हूँ।
अंतिम उत्तर में, मैं बाघ और बिल्ली एक ही प्रजाति का है, इसलिए मैं इसे स्पष्ट रूप से बताऊंगा। मैं इसके अलावा, यह भी बताऊंगा कि वे एक ही प्राकृतिक प्रजाति हैं।</think>बाघ और बिल्ली एक ही प्रजाति का हैं। वे एक ही प्राकृतिक प्रजाति का नाम हैं, जिसे "बाघ-बिल्ली" या "बाघ-बिल्ली" कहा जाता है। इसलिए, बाघ बिल्ली है।
```

### Example 5:

**Prompt:**
```text
Kya kitaab padhne ke liye hoti hai ?
```

**Spark output:**
```text
Hmm, user is asking in Hindi about what a "kitab" means. This seems like a straightforward question about the definition of the word "kitab" in the context of literature or religious texts.

I should provide a clear and comprehensive answer that covers the basic meaning, its usage, and perhaps some examples to help the user understand better. The user might be learning about literature or religious texts, so the explanation should be educational.

I can start by defining "kitab" as a written work, especially in religious or philosophical contexts. Then I can mention its importance in various traditions, like Islamic and Hindu texts. It might also be useful to give examples like the Quran or the Bhagavad Gita to illustrate.

The answer should be concise but informative, so I'll structure it with a direct definition, key characteristics, and examples. This way, the user gets a clear understanding of what a kitab is and its significance.</think>**Kitab** (किताब)
का अर्थ है **"पढ़ाई का लेख"** या **"साहित्यिक लेख"**।
इसका अर्थ और महत्व इस प्रकार हैं:

### 1. **सामान्य अर्थ**
- **किसी व्यक्ति या संस्था द्वारा लिखा गया एक लेख**, जिसमें विचार, विचार, सिद्धांत, दर्शन, या सांस्कृतिक जानकारी प्रस्तुत किया गया है।
- यह एक **सामान्य लेख** का शब्द है, जिसे पढ़ने और समझने की आवश्यकता होती है।

### 2. **किसी特定 संदर्भ में**
- **रeligious (रeligious) kitab** – **रeligious texts** जैसे कि **Quran (कुरान)**, **Bhagavad Gita (बhagavad Gita)**, **Talmud (तalmud)**, **Puran (पuran)** आदि। ये रeligious texts में सिद्धांत, दर्शन, या आध्यात्मिक सिद्धांत प्रस्तुत हैं।
- **philosophical (पilosophical) kitab** – **philosophical texts** जैसे कि **Machiavelli's "The Prince"**, **Socrates' writings**, **Kant's works** आदि। ये विचार, सिद्धांत, और दृष्टिकोण प्रस्तुत हैं।
- **literary (लитерary) kitab** – **literary texts** जैसे कि **Shakespeare's plays**, **Dostoevsky's novels**, **F. Scott Fitzgerald's works** आदि। ये साहित्यिक दृष्टिकोण, विचार, या दर्शन प्रस्तुत हैं।

### 3. **किसी संदर्भ में महत्व**
- **सामान्य लेख** – **सामान्य लेख** का महत्व है, जिससे व्यक्ति को ज्ञान, सिद्धांत, या दृष्टिकोण प्राप्त होता है।
- **रeligious kitab** – **रeligious texts** में सिद्धांत, दर्शन, और आध्यात्मिक सिद्धांत प्रस्तुत होते हैं, जिससे व्यक्ति को आध्यात्मिक सिद्धांत और दृष्टिकोण प्राप्त होता है।
- **philosophical kitab** – **philosophical texts** में विचार, सिद्धांत, और दृष्टिकोण प्रस्तुत होते हैं, जिससे व्यक्ति को सांस्कृतिक, आध्यात्मिक, या दृष्टिकोण प्राप्त होता है।

### 4. **किसी संदर्भ में उपयोग**
- **किसी व्यक्ति या संस्था द्वारा लिखा गया लेख**, जिसे पढ़ने की आवश्यकता होती है।
- **किसी संस्था (जैसे रeligious institution) द्वारा प्रस्तुत लेख**, जिसे समझने की आवश्यकता होती है।

### **उदाहरण**
- **Quran** – **Islamic kitab**, जिसमें सिद्धांत, दर्शन, और आध्यात्मिक सिद्धांत प्रस्तुत हैं।
- **Bhagavad Gita** – **Hindu kitab**, जिसमें आध्यात्मिक दृष्टिकोण और सिद्धांत प्रस्तुत हैं।
- **"The Great Gatsby"** – **literary kitab**, जिसमें साहित्यिक दृष्टिकोण और विचार प्रस्तुत हैं।

### **निष्कर्ष**
**Kitab** एक **लेख** का शब्द है, जिसे **पढ़ने** और **समझने** की आवश्यकता होती है। इसका महत्व इस बात पर निर्भर करता है कि वह किस संदर्भ में लिखा गया है – **रeligious, philosophical, या literary**।
```

### Example 6:

**Enter your prompt:**
```text
4 apples are eaten by children and their are only 10 in the basket? How many apples are eaten ?
```

**Thinking mode:**
```text
✓ Thinking mode set to: ON
```

**Spark output:**
```text
We are given: "4 apples are eaten by children and their are only 10 in the basket? How many apples are eaten ?"

This seems like a simple arithmetic problem. It says 4 apples are eaten, and there are 10 apples in the basket. The question asks: "How many apples are eaten?" The answer is clearly 4.

But let's read carefully: "4 apples are eaten by children and their are only 10 in the basket? How many apples are eaten ?" There might be a typo: "their" should be "there". So it's: 4 apples are eaten, and there are only 10 in the basket. How many apples are eaten? Answer: 4.

We should provide a clear and concise answer.</think>The number of apples eaten is **4**.

The problem states that 4 apples are eaten, so that is the answer. The information about 10 apples in the basket is extra and does not affect the number eaten.
```

### Example 7:

**Prompt:**
```text
A cow mows 5 times a day.Each Mow mean its breakfast time, and then a mow at lunch, then at supper, then at dinner.Which mow isn't related to any event on Timeline ?
```

**Spark output:** [OUTPUT](https://github.com/wasiqonx/Hack-Astron-Spark/blob/main/Thinking%20Mode%20On/logs/Reasoning.log#L398)

### Example 9:

**Prompt:**
```text
A cat eats 8 fishes in a day.But the owner of cat has only 20 fishes. How many days can cat eat sufficently enough to meet its quota of eating fishes ?
```

**Spark output:**
```text
We are given: "A cat eats 8 fishes in a day. But the owner of cat has only 20 fishes. How many days can cat eat sufficently enough to meet its quota of eating fishes ?"

We need to find the number of days. The cat eats 8 fishes per day. Total fishes available = 20. So number of days = total fishes / fishes per day = 20 / 8 = 2.5 days. But since the cat eats in whole days? The question says "How many days can cat eat sufficently enough to meet its quota?" It might be asking for the number of days it can eat, possibly fractional? Usually such problems expect a whole number or a fraction. But let's read carefully: "How many days can cat eat sufficently enough to meet its quota of eating fishes?" It might be interpreted as: how many days can it eat until it runs out? Since it eats 8 per day, after 2 days it eats 16 fishes, leaving 4 fishes. It cannot eat 8 in the 3rd day because it only has 4. So it can eat for 2 full days, and then it has 4 left but not enough for a full day. So the answer could be 2 days. But the phrasing "how many days can cat eat" might imply the maximum number of days it can eat entirely. So answer is 2 days.

But sometimes these problems are trick questions: "A cat eats 8 fishes in a day. Owner has 20 fishes. How many days can cat eat?" Answer: 2 days and 4 fishes left. But the question asks "How many days", so likely 2.

Let's check if there's any other interpretation. Could it be that the cat eats 8 fishes in a day, but maybe it eats them continuously? No, it's per day.

So answer: 2 days.

But let's see if the problem expects a fractional answer? "How many days can cat eat" might be answered as 2.5 days. But typically in such problems, they want the number of days it can eat completely. Since it says "sufficently enough to meet its quota", it means it can eat until it has no fishes left. So it can eat for 2 days and then has 4 left, which is not enough for a full day. So it can eat for 2 days.

I'll answer: 2 days.

But let's double-check: 20 fishes / 8 fishes per day = 2.5 days. If we consider that the cat eats exactly 8 per day, then after 2 days, it has 4 left. It cannot eat 8 in the third day. So it can eat for 2 days.

Thus the answer is 2.</think>The cat eats 8 fishes per day. With a total of 20 fishes available, the number of days it can eat completely is:

\[
\frac{20}{8} = 2.5 \text{ days}
\]

However, since the cat eats only 8 fishes per day, it can only eat for a full 2 days (eating 16 fishes) before running out of fishes. After 2 days, 4 fishes remain, which is not enough for a full day.

Therefore, the cat can eat **2 days** sufficently.
```

---

# Thinking Mode Off - Sessions Comparison

> **Note:** The following sessions were run with **Thinking Mode: Off** (using `spark-nothink` command). These are separate from the "Thinking Model Spark" examples above which primarily use Thinking Mode: On.

## Sessions Comparison

| Category | Session 1 | Session 2 | Session 3 | Session 4 |
|---|---|---|---|---|
| Model | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B |
| Runtime | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM | Spark-MLX-LLM |
| Runtime version | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] |
| Hardware | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory |
| GPU driver | MLX GPU | MLX GPU | MLX GPU | MLX GPU |
| Precision | BF16 | BF16 | BF16 | BF16 |
| Thinking Mode | Off | Off | Off | Off |
| Temperature | 0 | 0 | 0 | 0 |
| max_tokens | 10000 | 10000 | 10000 | 10000 |
| Prompt | Is 55+88=143 ? | Does it make sense to take the car ? | What is the capital of Delhi ? | A cat eats 9 fishes in a day. But the owner has only 21 fishes. At least how many days and hours could a cat survive? |
| Prompt tokens | 28 | 34 | 28 | 50 |
| Tokens per second [Input] | 160.152 tokens-per-sec | 183.896 tokens-per-sec | 181.467 tokens-per-sec | 277.236 tokens-per-sec |
| Generation tokens | 200 | 10000 | 10000 | 10000 |
| Tokens per second [Output] | 26.531 tokens-per-sec | 24.832 tokens-per-sec | 24.805 tokens-per-sec | 25.013 tokens-per-sec |
| Peak Memory | 3.464 GB | 3.649 GB | 3.649 GB | 3.648 GB |

## Session 1: Simple Addition

**Prompt:**
```
Is 55+88=143 ?
```

**Output:**
```
We are asked: "Is 55+88=143 ?" This is a simple arithmetic question. We need to check if 55 + 88 equals 143.

Let's compute: 55 + 88 = 143. Indeed, 55 + 88 = 143. So the answer is yes.

But we need to respond appropriately. The user asks a yes/no question. We should answer "Yes" or "Yes, 55+88=143." We can also show the calculation.

Since it's a straightforward question, we can just confirm.

I'll respond: Yes, 55 + 88 = 143.</think>Yes, 55 + 88 = 143. 

The calculation is correct: 55 + 88 = 143.
```

## Session 2: Car Wash Problem

**Prompt:**
```
Does it make sense to take the car ?
```

**Output:**
```
We are asked: "Does it make sense to take the car?" This is a vague question. We need more context. The user might be asking about whether it makes sense to take the car for a trip, or to a car wash, or something else. Without context, we can only give a general answer.

We should ask for clarification or provide a general response.

Possible answer: "It depends on the context. Could you provide more details about what you're referring to?"

But the instruction says "Answer directly and concisely." So we can say: "It depends on the situation. Please provide more context."

However, we can also give a general answer: "Taking the car makes sense if you need to travel a long distance or carry heavy items. For short distances, walking or biking might be more practical."

But the user might be referring to a specific situation. Since we don't have context, we should ask for clarification.

I'll respond: "It depends on the context. Could you provide more details?</think>It depends on the context. Could you provide more details?

For example, are you asking about taking the car to a car wash, on a trip, or for a short journey?
```

## Session 3: Capital of Delhi

**Prompt:**
```
What is the capital of Delhi ?
```

**Output:**
```
We are asked: "What is the Capital of Delhi ?" This is a straightforward factual question. The capital of Delhi is New Delhi. However, note that Delhi is a union territory, and its capital is New Delhi. Sometimes people might say Delhi, but the official capital is New Delhi. So the answer should be New Delhi.

Let's provide a clear and concise answer.</think>The capital of Delhi is **New Delhi**.
```

## Session 4: Cat and Fishes Problem

**Prompt:**
```
A cat eats 9 fishes in a day. But the owner has only 21 fishes. At least how many days and hours could a cat survive?
```

**Output:**
```
We are given: "A cat eats 9 fishes in a day. But the owner has only 21 fishes. At least how many days and hours could a cat survive?"

Interpretation: The cat eats 9 fish per day. The owner has 21 fish total. We need to find the minimum number of days and hours the cat can survive. The cat eats 9 fish per day, so it will be exhausted after 21 fish are eaten. But we need to consider if the cat eats exactly 9 fish per day, and the owner has exactly 21 fish. The cat will survive for as many days as possible until it runs out of fish. Since it eats 9 fish per day, after 2 days it will have eaten 18 fish, leaving 3 fish. After 3 days, it would eat 27 fish, but only 21 are available, so it cannot survive 3 full days. So the cat can survive for 2 full days, and then on the third day, it will eat 9 fish, but only 3 are left, so it will not eat all 9? The question says "At least how many days and hours could a cat survive?" It might imply that the cat eats exactly 9 fish per day, and we want the minimum number of days and hours it can survive given the total fish. But if the cat eats 9 fish per day, and there are 21 fish, then after 2 days, 18 fish eaten, 3 left. On the third day, the cat will eat 9 fish, but only 3 are available, so it will eat 3 fish and then die? Or does it eat only what it can? The phrasing "eats 9 fishes in a day" suggests it consumes 9 fish per day. If there are only 3 fish left, it cannot eat 9. So it would only eat 3 fish, and then die. So the cat survives for 2 full days, and then on the third day it dies after eating 3 fish? But the question asks "At least how many days and hours could a cat survive?" That might mean the maximum number of days it can survive, but with the constraint that it eats 9 fish per day. If it eats 9 fish per day, then after 2 days it has 3 fish left. On the third day, it would need to eat 9 fish, but only 3 are available, so it cannot survive the third day. So the cat survives for 2 days and then dies. But the question says "At least how many days and hours could a cat survive?" That phrasing is a bit ambiguous. It might be asking: Given that the cat eats 9 fish per day, and the owner has 21 fish, how many days can the cat survive? The answer would be 2 days (with 3 fish left over). But the question says "At least how many days and hours could a cat survive?" That might be asking for the minimum number of days it can survive, which would be 0 days if it doesn't eat. But that doesn't make sense. Let's re-read: "At least how many days and hours could a cat survive?" The phrase "at least" might be a mistranslation or misphrasing. It might mean "at most" or "how many days". Let's assume it's asking for the number of days the cat can survive given that it eats 9 fish per day and there are 21 fish. The cat can survive for 2 full days (eating 18 fish), and then on the third day, it can eat 3 fish but not the full 9. So it survives for 2 days and then dies on the third day. But the question asks for "days and hours". If we assume the cat eats 9 fish per day, that's 9/24 = 0.375 fish per hour. If there are 3 fish left, the cat can eat 3/0.375 = 8 hours worth of fish. So the cat survives for 2 days and 8 hours. But the question says "At least how many days and hours could a cat survive?" That might be asking for the minimum number of days and hours, which would be 0 days and 0 hours. But that doesn't make sense. Let's assume the question is asking for the maximum number of days and hours the cat can survive. The cat eats 9 fish per day. With 21 fish, it can survive for 2 full days (18 fish), and then have 3 fish left. If it eats 9 fish per day, that's 9/24 = 0.375 fish per hour. With 3 fish left, it can survive for 3/0.375 = 8 hours. So the cat can survive for 2 days and 8 hours. But the question says "At least how many days and hours could a cat survive?" That phrasing is confusing. Let's just answer: The cat can survive for 2 days and 8 hours.

But let's double-check: 9 fish per day = 9/24 fish per hour = 0.375 fish per hour. 21 fish / 0.375 fish per hour = 56 hours = 2 days and 8 hours. Yes.

So the answer is 2 days and 8 hours.

But the question says "At least how many days and hours could a cat survive?" The phrase "at least" might be a mistake. It should be "at most" or just "how many days". Let's answer: 2 days and 8 hours.

I'll respond: The cat can survive for **2 days and 8 hours**.

Calculation: The cat eats 9 fish per day = 0.375 fish per hour. With 21 fish, the cat can survive for 21 / 0.375 = 56 hours = 2 days and 8 hours.
```

---

# Multiple-Answer - Sessions Comparison

> **Note:** The following sessions were run using the **Spark-X2.5 Interactive File Analyzer** which scans files in a directory and answers questions about them. This is a multiple-file coding context where the model analyzes and answers questions about provided files. For full details, see [OUTPUT](Multiple-Answer/comparison.md).

## Sessions Comparison

| Category | Session 1 | Session 2 |
|---|---|---|
| Model | XHToken/Spark-X2.5-1.7B | XHToken/Spark-X2.5-1.7B |
| Runtime | Spark-MLX-LLM | Spark-MLX-LLM |
| Runtime version | Spark-MLX-LLM [0.1.0] | Spark-MLX-LLM [0.1.0] |
| Hardware | Apple M3-Pro 8GB Unified Memory | Apple M3-Pro 8GB Unified Memory |
| GPU driver | MLX GPU | MLX GPU |
| Precision | BF16 | BF16 |
| Thinking Mode | Off | Off |
| Temperature | 0.7 | 0.7 |
| max_tokens | 2048 | 2048 |
| Prompt | scan question.txt and answer it | Check the make.C for error |
| Prompt tokens | 2818 | 2904 |
| Tokens per second [Input] | 638.903 tokens-per-sec | 439.136 tokens-per-sec |
| Generation tokens | 2048 | 1451 |
| Tokens per second [Output] | 22.678 tokens-per-sec | 23.197 tokens-per-sec |
| Peak Memory | 4.033 GB | 4.033 GB |
| Runtime | 103.68s | 136.55s |

## Session 1: HTML Table with 20 Country Names

**Files in Directory:**
- `scanner.py` (278 lines, 15470 bytes)
- `question.txt` (1 lines, 61 bytes)

**Prompt:**
```
scan question.txt and answer it
```

**question.txt Content:**
```
Make an HTML file that displays a table with 20 country names
```

**Output:**
The model analyzed the question.txt file and provided a complete HTML solution. See the generated file: [OUTPUT](Multiple-Answer/countries.html)

## Session 2: C Code Error Analysis

**Files in Directory:**
- `scanner.py` (278 lines, 15470 bytes)
- `make.C` (9 lines, 98 bytes)

**Prompt:**
```
Check the make.C for error
```

**make.C Content:**
```c
#include <stdio.h>

int main()
{
    int a=782;
    int b=02;
    int c=a+b;
    printf("%d",c);
}
```

**Output:**
The model **Halluncinated an error**  in line 6:
```c
int b=02;
```

**Problem:** In C, It someho hallucinated a non-existing problem which didn't exist and try tp change to binary which adds error 

** The Proposed Fix By Spark-1.7B Model:**
```c
int b = 2;  // For decimal value 2
// or
int b = 0b02;  // For binary value 2 for no apparent reason
```





---

## Conclusion

The Model seem to be working fine for simple tasks and questions that are straight but when a little twist and reasoning is added it struggles or it just start over thinking  and use all tokens or worse Crash due to memory issue
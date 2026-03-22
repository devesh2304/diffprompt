# diffprompt

A CLI tool for behavioral prompt diffing — compare how LLMs respond differently to prompt variations.

## What it does

When you change a prompt slightly, how does the model's behaviour actually change? `diffprompt` answers this by running two prompts side by side and showing you a structured diff of the outputs — like `git diff` but for LLM behaviour.

## Demo
```
diffprompt diff \
  --a "Explain gravity in one sentence" \
  --b "Explain gravity in one sentence. Be poetic."
```

Output:
- Side by side colored outputs
- Line-by-line behavioral diff
- Similarity score (0–100%)

## Installation
```bash
git clone https://github.com/devesh2304/diffprompt
cd diffprompt
python3 -m venv env && source env/bin/activate
pip install -e .
```

## Setup

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free Groq API key at console.groq.com

## Usage
```bash
diffprompt diff --a "your first prompt" --b "your second prompt"
```

Optional flags:
- `--model` — specify a Groq model (default: llama-3.3-70b-versatile)

## Stack

- Python · Click · Rich · Groq API

## Why this exists

Prompt engineering is mostly blind guessing. diffprompt makes it measurable.
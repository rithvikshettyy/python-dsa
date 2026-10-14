# python-dsa

Python practice repo: beginner scripts and data structures & algorithms (DSA) exercises.

## Contents

| File | Description |
|------|-------------|
| `addition.py` | Read two integers, print their sum |
| `even_odd.py` | Check whether a number is even or odd |
| `if_elif.py` | Traffic light example using `if` / `elif` / `else` |
| `main.py` | Minimal FastAPI app with a `/` route |
| `src/myproject/` | Package skeleton managed with `uv` |

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (optional, for the packaged project)
- `fastapi` and `uvicorn` (only for `main.py`)

## Usage

Clone and run any script directly:

```bash
git clone https://github.com/rithvikshettyy/python-dsa.git
cd python-dsa
python addition.py
```

Run the FastAPI example:

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then open <http://127.0.0.1:8000/> to see `{"message": "Hello World"}`.

## Author

rithvik shetty

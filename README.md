# SyllaWhat

Minimal Python setup for the syllabus project. It checks that FastAPI, Uvicorn,
pdfplumber, python-docx, and icalendar can load in the same environment.
Running it creates no reports, prints nothing, and does not start a server.
No credentials are required.

## Setup

Use the `poc/minimal-setup` branch. From the repository folder:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `py` in place of `python3`, then activate with
`.venv\Scripts\activate` in Command Prompt.

## Compile and run

```sh
python -m py_compile main.py
python main.py
python -m pip check
```

The first command checks Python bytecode compilation. The second checks imports
and creates basic library objects in memory. Both should exit successfully
without output. The final command checks installed dependency compatibility.

Tested with Python 3.14.3 on macOS 27.0 (26A5425a).
Direct dependencies are pinned in `requirements.txt`; pip installs their dependencies.
This is a backend dependency check, not a complete application. Parsing, React,
and LLM integration are not implemented.

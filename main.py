"""Minimal dependency check; running this file produces no output."""

import pdfplumber
import uvicorn
from docx import Document
from fastapi import FastAPI
from icalendar import Calendar

app = FastAPI(title="SyllaWhat")

if __name__ == "__main__":
    document = Document()
    calendar = Calendar()
    server = uvicorn.Config(app)
    assert callable(pdfplumber.open)

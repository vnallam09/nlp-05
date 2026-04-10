"""
src/nlp/config_teja.py - Module 5 Configuration

Stores configuration values for the web document EVTL pipeline.
Source: arXiv abstract page for "Disentangling cosmic distance tensions
with early and late dark energy" (2604.08530)

Purpose

  Store configuration values.

Analytical Questions

- What web page URL should be used as the data source?
- Where should raw and processed data be stored?
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

PAGE_URL: str = "https://arxiv.org/abs/2604.08530"
# arXiv abstract page — stable, scraping-friendly, academically relevant

# Let them know who we are (and that we're doing educational web mining).
HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

# to something that represents YOUR custom project.
RAW_HTML_PATH: Path = RAW_PATH / "teja_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "teja_processed.csv"

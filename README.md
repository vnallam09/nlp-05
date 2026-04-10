# nlp-05-web-documents

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Structured EVTL pipeline for reliable extraction and transformation of data from HTML web pages.

Web Mining and Applied NLP require reliable acquisition and
processing of structured and semi-structured text data.
This project implements a reproducible pipeline for
working with HTML data from arXiv abstract pages.

The pipeline follows an EVTL architecture:

- **Extract** HTML from a web page
- **Validate** structure and content before use
- **Transform** HTML into a structured representation
- **Load** results into a persistent, analyzable format

Every stage has explicit inputs, outputs, and logging,
and intermediate artifacts are preserved for verification.

## This Project

This project applies the EVTL pipeline to the arXiv abstract page for:

> **Disentangling cosmic distance tensions with early and late dark energy**
> Tanisha Jhaveri, Tanvi Karwal, Thomas Crawford, Wayne Hu, Ali Rida Khalife, Lennart Balkenhol, Fei Ge
> [arxiv.org/abs/2604.08530](https://arxiv.org/abs/2604.08530) — Astrophysics > Cosmology and Nongalactic Astrophysics

The pipeline extracts bibliographic metadata and computes derived fields,
producing a structured CSV for downstream analysis.

## Key Files

| File | Role |
|---|---|
| [src/nlp/config_teja.py](src/nlp/config_teja.py) | Configuration: page URL and output paths |
| [src/nlp/pipeline_web_html_teja.py](src/nlp/pipeline_web_html_teja.py) | Main pipeline orchestrator |
| [src/nlp/stage01_extract.py](src/nlp/stage01_extract.py) | Extract: fetches HTML from the web page |
| [src/nlp/stage02_validate_teja.py](src/nlp/stage02_validate_teja.py) | Validate: inspects and verifies HTML structure |
| [src/nlp/stage03_transform_teja.py](src/nlp/stage03_transform_teja.py) | Transform: converts HTML into structured data |
| [src/nlp/stage04_load.py](src/nlp/stage04_load.py) | Load: writes output CSV to disk |

## Run the Pipeline

```shell
uv run python -m nlp.pipeline_web_html_teja
```

## Output

The pipeline produces:

- `data/raw/teja_raw.html` — fetched HTML page
- `data/processed/teja_processed.csv` — structured output with 13 columns

### Extracted Fields

| Field | Description |
|---|---|
| `arxiv_id` | arXiv paper identifier |
| `title` | Paper title |
| `authors` | Comma-separated author names |
| `subjects` | Full subject breadcrumb |
| `primary_subject_code` | arXiv subject code (e.g. `astro-ph.CO`) |
| `submitted` | Submission date string |
| `version_count` | Number of submitted versions |
| `pdf_url` | Direct link to the PDF |
| `abstract` | Full abstract text |
| `abstract_word_count` | Word count of the abstract |
| `sentence_count` | Sentence count of the abstract |
| `avg_word_length` | Average word length (alphabetic words only) |
| `author_count` | Number of authors |

### Example Log Output

```text
START PIPELINE
ROOT_PATH = .
DATA_PATH = data
RAW_PATH = data\raw
PROCESSED_PATH = data\processed
========================
STAGE 01: EXTRACT starting...
========================
SOURCE URL = https://arxiv.org/abs/2604.08530
SINK PATH = data\raw\teja_raw.html
========================
STAGE 02: VALIDATE starting...
========================
VALIDATE: Title found: True
VALIDATE: Authors found: True
VALIDATE: Abstract found: True
VALIDATE: Subjects found: True
VALIDATE: Dateline found: True
VALIDATE: HTML structure is valid.
========================
STAGE 03: TRANSFORM starting...
========================
Extracted title: Disentangling cosmic distance tensions with early and late dark energy
Extracted authors: Tanisha Jhaveri, Tanvi Karwal, Thomas Crawford, Wayne Hu, Ali Rida Khalife, Lennart Balkenhol, Fei Ge
Extracted subjects: Astrophysics > Cosmology and Nongalactic Astrophysics
Extracted pdf_url: https://arxiv.org/pdf/2604.08530
Extracted primary_subject_code: astro-ph.CO
Extracted version_count: 1
Extracted arxiv_id: 2604.08530
Calculated abstract word count: 250
Calculated sentence count: 9
Calculated avg_word_length: 5.28
Calculated author count: 7
Created DataFrame with 1 row and 13 columns
========================
STAGE 04: LOAD starting...
========================
SINK PATH = data\processed\teja_processed.csv
========================
Pipeline executed successfully!
========================
```

## HTML Structure and BeautifulSoup

arXiv abstract pages use a consistent HTML structure that BeautifulSoup can reliably parse:

| Field | HTML Tag / Attribute |
|---|---|
| Title | `<h1 class="title">` — strip `"Title:"` descriptor prefix |
| Authors | `<div class="authors">` — extract each `<a>` tag to avoid double-comma artifacts |
| Abstract | `<blockquote class="abstract">` — strip `"Abstract:"` prefix |
| Subjects | `<div class="subheader">` |
| Primary subject code | `<span class="primary-subject">` — parse text inside `()` |
| Dateline | `<div class="dateline">` |
| arXiv ID | `<link rel="canonical">` — split on `/abs/` |
| PDF link | `<a href="/pdf/...">` — prepend `https://arxiv.org` |
| Version count | `<div class="submission-history">` — count `<strong>` tags |

## Enhancements

In production systems, validation is often automated using tools
such as **Great Expectations** or **Soda**.

Within the EVTL architecture, **VALIDATE** is a key stage
with a clear source, process, and sink:

- **Source**: HTML fetched from the web page
- **Process**: parsing with BeautifulSoup, checking structure, confirming expected elements are present
- **Sink**: BeautifulSoup object passed to the TRANSFORM stage

This stage ensures the data is in a **consistent and reliable form**
before transformation begins,
so later steps can run without errors or unexpected results.

## Command Reference

<details>
<summary>Show command reference</summary>

### Clone and set up

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/vnallam09/nlp-05/
cd nlp-05
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files

uv run python -m nlp.pipeline_web_html_teja

uv run ruff format .
uv run ruff check . --fix

git add -A
git commit -m "update"
git push -u origin main
```

</details>

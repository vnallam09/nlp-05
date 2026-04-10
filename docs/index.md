# nlp-05: Web Documents and HTML Data

Documentation for the Module 5 EVTL pipeline project by Venkat Teja.

## Project Summary

This project applies a structured EVTL pipeline to an arXiv abstract page,
extracting and transforming HTML data into a clean, structured CSV.

**Paper:** [Disentangling cosmic distance tensions with early and late dark energy](https://arxiv.org/abs/2604.08530)
**Subject:** Astrophysics > Cosmology and Nongalactic Astrophysics
**arXiv ID:** 2604.08530

## Pipeline Overview

| Stage | Description |
|---|---|
| **Extract** | Fetch HTML from the arXiv abstract page |
| **Validate** | Confirm expected tags (title, authors, abstract, subjects, dateline) are present |
| **Transform** | Parse fields with BeautifulSoup and compute derived metrics |
| **Load** | Write structured output to `data/processed/teja_processed.csv` |

## Output Fields

13 columns extracted and computed per paper:
`arxiv_id`, `title`, `authors`, `subjects`, `primary_subject_code`,
`submitted`, `version_count`, `pdf_url`, `abstract`,
`abstract_word_count`, `sentence_count`, `avg_word_length`, `author_count`

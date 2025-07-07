# 🧠 AI Cover Letter Critiquer

## Overview
This project uses a free, open-source large language model to evaluate and critique cover letters in `.docx` format. By simulating an expert recruiter, it provides structured and constructive feedback to help job seekers improve tone, structure, and relevance.

## Objective
- Analyze and critique cover letters from a recruiter’s perspective.
- Deliver feedback on clarity, structure, grammar, and job fit.

## How It Works
1. Reads a `.docx` file containing the cover letter.
2. Uses `MBZUAI/LaMini-Flan-T5-783M` model via Hugging Face to generate critique.
3. Prints detailed recruiter-style feedback.

## Technologies Used
- Python
- HuggingFace Transformers (`pipeline`)
- Pretrained model: `MBZUAI/LaMini-Flan-T5-783M`
- `python-docx` for `.docx` parsing

## How to Run
```bash
pip install transformers python-docx
python cover_letter_critiquer.py
```

Make sure the file is named `Cover Letter.docx` and is in the same directory.

## Sample Feedback Output
> "The letter presents a clear interest in the role and showcases relevant technical skills. However, the structure could be more concise and focused on key achievements. Tone is enthusiastic and appropriate, though some sentences could be tightened for clarity..."

## Future Enhancements
- GUI or web app version
- Multi-model benchmarking
- Integration with resume analysis

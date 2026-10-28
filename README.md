# Research Paper Explainer

A Streamlit app that explains well-known ML papers in the style and length you choose.

## Why this exists
Practice with reusable prompt templates in LangChain, saved to and loaded from a JSON file.

## What it does
- Lets you pick a paper (for example BERT or GPT-3)
- Lets you pick a style: beginner, technical, code-oriented or mathematical
- Lets you pick a length: short, medium or long
- Fills a saved prompt template and returns GPT-4's explanation

## Project structure
```
researchpaperchatbot/
├── prompt.py         Streamlit app
├── template.json     Saved LangChain prompt template
└── requirements.txt  Python dependencies
```

## Getting started
Requirements: Python 3.10+, an OpenAI API key.
```bash
git clone https://github.com/abhijha8287/researchpaperchatbot.git
cd researchpaperchatbot
pip install -r requirements.txt streamlit
mkdir -p .streamlit && echo 'api_key = "sk-..."' > .streamlit/secrets.toml
streamlit run prompt.py
```

## Configuration
| Variable | Purpose |
|:--|:--|
| `api_key` in `.streamlit/secrets.toml` | OpenAI API key |

## Tech stack
Python, LangChain, OpenAI GPT-4, Streamlit

## Notes
Live demo: https://researchpaperchatbotbyabhishek.streamlit.app (on the free Streamlit tier it may take a few seconds to wake up). `requirements.txt` lists more LangChain integrations than the app uses; only OpenAI is needed.

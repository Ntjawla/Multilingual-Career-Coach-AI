
#  Multilingual Career Coach AI (LLaMA + NLLB)

An AI chatbot that gives career advice in Hindi, Spanish, French, or English — with resume parsing.

##  Features
- Multilingual input/output using NLLB
- Career tips powered by LLaMA 3.2–1B-Instruct
- Resume analysis via PDF
- Clean Streamlit interface
- Runs 100% locally

## Setup
```bash
git clone https://github.com/Ntjawla/Multilingual-Career-Coach-AI.git
cd Multilingual-Career-Coach-AI
pip install -r requirements.txt
huggingface-cli login
```

## Run the App
```bash
streamlit run chatbot_ui.py
```

## Models Used
- `meta-llama/Llama-3.2-1B-Instruct`
- `facebook/nllb-200-distilled-600M`

## Resume Suggestions
Upload your resume (PDF), and the bot will highlight missing skills or keywords based on simple heuristics.

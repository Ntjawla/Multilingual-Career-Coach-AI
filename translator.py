
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langdetect import detect

nllb_model_name = "facebook/nllb-200-distilled-600M"
nllb_tokenizer = AutoTokenizer.from_pretrained(nllb_model_name)
nllb_model = AutoModelForSeq2SeqLM.from_pretrained(nllb_model_name)

lang_map = {
    "en": "eng_Latn",
    "hi": "hin_Deva",
    "es": "spa_Latn",
    "fr": "fra_Latn",
}

def detect_lang(text):
    try:
        lang = detect(text)
        return lang_map.get(lang, "eng_Latn")
    except:
        return "eng_Latn"

def translate_text(text, src_lang, tgt_lang):
    tokenizer = nllb_tokenizer
    model = nllb_model
    tokenizer.src_lang = src_lang
    encoded = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded, forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang])
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

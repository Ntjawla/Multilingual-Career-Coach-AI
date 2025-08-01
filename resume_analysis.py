
import fitz

def analyze_resume(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    suggestions = []
    if "machine learning" not in text.lower():
        suggestions.append("Consider adding 'machine learning' to highlight your ML interest.")
    if "project" not in text.lower():
        suggestions.append("List at least one project with clear outcomes.")
    if "python" not in text.lower():
        suggestions.append("Add Python experience explicitly.")

    return "\n".join(suggestions) if suggestions else "Your resume looks solid for a career in AI!"

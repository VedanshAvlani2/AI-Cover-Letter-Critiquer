from transformers import pipeline
import docx
import os

print("⚙️ Loading model...")
generator = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-783M")

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text.strip() for para in doc.paragraphs if para.text.strip()])

def critique_cover_letter(text):
    trimmed_text = text[:1500]  
    prompt = (
        "You are a senior recruiter. Please review the following cover letter and provide a helpful critique. "
        "Comment on the structure, clarity, tone, grammar, and whether it effectively presents the candidate for a data analyst internship.\n\n"
        f"--- COVER LETTER START ---\n{trimmed_text}\n--- COVER LETTER END ---\n\n"
        "Now write a constructive critique in 5–7 sentences:"
    )

    try:
        result = generator(prompt, max_new_tokens=250, do_sample=False)[0]['generated_text']
        return result
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    input_path = "Cover Letter.docx"
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
    else:
        print("📄 Reading cover letter...")
        cover_letter_text = extract_text_from_docx(input_path)
        print("\n🧠 Analyzing cover letter...\n")
        feedback = critique_cover_letter(cover_letter_text)
        print("✅ Feedback:\n")
        print(feedback)

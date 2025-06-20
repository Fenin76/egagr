# 🧠 Tailored CV Generator

> Create job-specific, one-page resumes using AI, Jinja templates, and PDF rendering.

---

## 🚀 Project Idea

This tool allows you to **generate a customized CV tailored for each job application** in just a few simple steps. Whether you're applying for internships, junior positions, or experienced roles, this automation ensures your resume is aligned with the job description.

---

## 🧭 How It Works

1. **Prompt Input**
   - Paste a **job description** or **job listing URL** when prompted.
   - Enter your **experience details** (either manually or from a saved file).

2. **AI Matching**
   - A prompt is constructed and sent to **Gemini (or ChatGPT)**.
   - The AI returns a **tailored, CV-ready version** of your experience that matches the job description.

3. **Template Filling**
   - The processed data is inserted into a **LaTeX or HTML CV template** using **Jinja2**.
   - The final result is a **PDF CV** formatted to professional standards.

4. **(Optional)** PDF Validator
   - A check ensures the resume fits exactly **one page** using `PyPDF2`.

---

## 🛠️ Tech Stack

- Python 3.x
- [Jinja2](https://jinja.palletsprojects.com/) – Template engine
- [Gemini / OpenAI](https://platform.openai.com/) – LLM API for tailoring content
- [Tectonic](https://tectonic-typesetting.github.io/) or [WeasyPrint](https://weasyprint.org/) – PDF rendering
- [PyPDF2](https://pypi.org/project/PyPDF2/) – Validate page count

---

## 📦 Features (Planned)

- [x] Paste job description or link
- [x] Input user experience interactively or via file
- [x] Tailor content using Gemini or ChatGPT
- [x] Fill and render into a professional CV template
- [x] Export as PDF (single-page enforced)
- [ ] Auto-trim sections intelligently if content overflows
- [ ] Switch between multiple resume templates
- [ ] Web interface (future)

---

## 📁 Folder Structure (Example)

cv-tailor/
├── data/
│ └── profile.yaml # User experience data
├── templates/
│ └── onepage_resume.tex.jinja2 # CV template
├── output/
│ └── tailored_resume.pdf # Final result
├── main.py # Core logic
├── prompt_template.txt # LLM prompt file
└── README.md

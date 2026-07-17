SECTION_HEADERS = {
    "education": "education",
    "skills": "skills",
    "technical skills": "skills",
    "projects": "projects",
    "academic projects": "projects",
    "personal projects": "projects",
    "experience": "experience",
    "work experience": "experience",
    "internship": "experience",
    "training & learning": "training",
    "training": "training",
    "certifications": "certifications",
    "achievements": "achievements",
    "summary": "summary",
    "interests": "interests"
}


def extract_sections(text):
    sections = {"header": []}
    current_section = "header"

    for line in text.split("\n"):
        clean = line.strip()

        if not clean:
            continue

        lower = clean.lower()

        if lower in SECTION_HEADERS:
            current_section = SECTION_HEADERS[lower]
            sections.setdefault(current_section, [])
        else:
            sections.setdefault(current_section, []).append(clean)

    return sections
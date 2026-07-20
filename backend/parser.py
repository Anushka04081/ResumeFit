import re
from skills_database import SKILLS
from section_parser import extract_sections
from evidence import check_skill_evidence


def extract_email(text):
    text = text.replace(" @", "@")

    email = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    return email[0] if email else None


def extract_phone(text):
    phone = re.findall(
        r'\d{10}',
        text
    )

    return phone[0] if phone else None


def extract_name(text):
    email = extract_email(text)

    if email:
        before_email = text.split(email)[0].strip()

        words = before_email.split()

        if len(words) >= 2:
            return words[0] + " " + words[1]

    return None


def extract_skills(text):

    skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            skills.append(skill)

    return skills


import re

def extract_education(education_lines):
    education = []

    if not education_lines:
        return education

    if isinstance(education_lines, str):
        lines = [line.strip() for line in education_lines.split("\n") if line.strip()]
    else:
        lines = [line.strip() for line in education_lines if line.strip()]

    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect the start of an education record
        if (
            "b.tech" in line.lower()
            or "btech" in line.lower()
            or "class 12" in line.lower()
            or "class xii" in line.lower()
            or "class 10" in line.lower()
            or "class x" in line.lower()
        ):

            degree = line
            college = lines[i - 1] if i > 0 else ""

            year = ""
            cgpa = ""

            if i + 1 < len(lines):
                year_match = re.search(
                    r"(20\d{2}\s*[-–]\s*20\d{2}|20\d{2})",
                    lines[i + 1]
                )
                if year_match:
                    year = year_match.group(1)

            j = i + 1
            while j < min(i + 5, len(lines)):
                cgpa_match = re.search(
                    r"(CGPA|GPA)\s*[:\-]?\s*(\d+(\.\d+)?)",
                    lines[j],
                    re.IGNORECASE,
                )

                if cgpa_match:
                    cgpa = cgpa_match.group(2)
                    break

                j += 1

            education.append({
                "degree": degree,
                "college": college,
                "year": year,
                "cgpa": cgpa,
            })

        i += 1

    return education

def extract_projects(project_lines):

    projects = []

    if not project_lines:
        return projects

    title = project_lines[0].strip()

    projects.append({
        "title": title,
        "description": project_lines[1:]
    })

    return projects


def parse_resume(text):

    sections = extract_sections(text)

    skills = extract_skills(
        "\n".join(sections.get("skills", []))
    )

    projects = extract_projects(
        sections.get("projects", [])
    )

    training = sections.get("training", [])

    analyzed_skills = []

    for skill in skills:
        analyzed_skills.append(
            check_skill_evidence(
                skill,
                projects,
                training
            )
        )

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": analyzed_skills,
        "education": extract_education(
            "\n".join(sections.get("education", []))
        ),
        "projects": projects,
        "training": training
    }
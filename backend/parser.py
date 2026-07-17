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
def extract_education(text):

    education = []

    keywords = [
        "B.Tech",
        "BTech",
        "CGPA",
        "CBSE",
        "ICSE"
    ]

    for keyword in keywords:
        if keyword.lower() in text.lower():
            education.append(keyword)

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
    print(skills)
    print(type(skills[0]))

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
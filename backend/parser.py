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




def extract_education(education_lines):

    education = []

    if not education_lines:
        return education

    if isinstance(education_lines, str):
        lines = [line.strip() for line in education_lines.split("\n") if line.strip()]
    else:
        lines = [line.strip() for line in education_lines if line.strip()]

    degree_keywords = [
        "b.tech", "btech", "b.e", "be", "m.tech", "mtech",
        "class 12", "class xii", "class 10", "class x"
    ]

    current = None

    for line in lines:

        lower = line.lower()

        # Start of a new education entry
        if any(keyword in lower for keyword in degree_keywords):

            if current:
                education.append(current)

            current = {
                "degree": line,
                "college": "",
                "year": "",
                "cgpa": ""
            }

        elif current is not None:

            if current["year"] == "":
                year_match = re.search(
                    r"(20\d{2}\s*[-–]\s*20\d{2}|20\d{2})",
                    line
                )

                if year_match:
                    current["year"] = year_match.group(1)

            if current["cgpa"] == "":
                cgpa_match = re.search(
                    r"(CGPA|GPA)\s*[:\-]?\s*(\d+(\.\d+)?)",
                    line,
                    re.IGNORECASE
                )

                if cgpa_match:
                    current["cgpa"] = cgpa_match.group(2)

            if (
                current["college"] == ""
                and "cgpa" not in lower
                and "board" not in lower
                and "%" not in line
                and not re.search(r"20\d{2}", line)
            ):
                current["college"] = line

    if current:
        education.append(current)

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
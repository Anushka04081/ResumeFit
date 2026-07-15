import re


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

        # Usually first two words are the person's name
        if len(words) >= 2:
            return words[0] + " " + words[1]

    return None


def extract_skills(text):

    skills_list = [
        "C++",
        "Python",
        "SQL",
        "DSA",
        "Git",
        "GitHub",
        "OOP",
        "DBMS"
    ]

    found = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found.append(skill)

    return found
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


def extract_projects(text):

    projects = []

    if "Student Management System" in text:
        projects.append("Student Management System")

    return projects


def parse_resume(text):

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "projects": extract_projects(text)
    }
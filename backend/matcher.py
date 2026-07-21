SKILLS = [
    "python",
    "java",
    "c++",
    "javascript",
    "react",
    "node",
    "express",
    "fastapi",
    "html",
    "css",
    "sql",
    "mongodb",
    "git",
    "github",
    "docker",
    "aws",
    "machine learning",
    "data structures",
    "algorithms",
]


def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))


def compare(resume_skills, job_description):
    jd_skills = extract_skills(job_description)

    extracted_resume_skills = set()

    for skill in resume_skills:
        if isinstance(skill, dict):
            extracted_resume_skills.add(skill["name"].lower())
        else:
            extracted_resume_skills.add(skill.lower())

    jd_skills = set(jd_skills)

    matched = sorted(list(extracted_resume_skills & jd_skills))
    missing = sorted(list(jd_skills - extracted_resume_skills))
    extra = sorted(list(extracted_resume_skills - jd_skills))

    if jd_skills:
        score = round((len(matched) / len(jd_skills)) * 100)
    else:
        score = 100

    skill_score = int((score / 100) * 20)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra,
        "skill_score": skill_score,
    }
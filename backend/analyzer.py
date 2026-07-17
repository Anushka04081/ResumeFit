def calculate_score(resume_data):

    breakdown = {
        "contact": 0,
        "skills": 0,
        "projects": 0,
        "experience": 0,
        "education": 0,
        "achievements": 0
    }

    strengths = []
    improvements = []
    missing_sections = []

    # ---------------- Contact ----------------
    if resume_data.get("name"):
        breakdown["contact"] += 3

    if resume_data.get("email"):
        breakdown["contact"] += 4

    if resume_data.get("phone"):
        breakdown["contact"] += 3

    if breakdown["contact"] == 10:
        strengths.append("Complete contact information")
    else:
        improvements.append("Complete your contact information")

    # ---------------- Skills ----------------
    skills = resume_data.get("skills", [])

    implemented_skills = 0

    for skill in skills:
        if skill["implemented"]:
            implemented_skills += 1

    if implemented_skills >= 8:
        breakdown["skills"] = 20
        strengths.append("Excellent practical technical skills")

    elif implemented_skills >= 5:
        breakdown["skills"] = 15
        strengths.append("Good practical technical skills")

    elif implemented_skills >= 3:
        breakdown["skills"] = 10
        strengths.append("Basic practical technical skills")
        improvements.append("Implement more listed skills in projects")

    elif implemented_skills >= 1:
        breakdown["skills"] = 5
        improvements.append("Strengthen technical projects")

    else:
        improvements.append("Add practical implementation of your skills")
    # ---------------- Projects ----------------
    projects = resume_data.get("projects", [])

    if len(projects) >= 2:
        breakdown["projects"] = 20
        strengths.append("Multiple projects included")

    elif len(projects) == 1:
        breakdown["projects"] = 10
        strengths.append("At least one project included")
        improvements.append("Add one more strong project")

    else:
        missing_sections.append("Projects")
        improvements.append("Add practical projects")

    # ---------------- Education ----------------
    education = resume_data.get("education", [])

    if education:
        breakdown["education"] = 10
        strengths.append("Education section present")
    else:
        missing_sections.append("Education")

    # ---------------- Experience ----------------
    experience_keywords = [
        "internship",
        "experience",
        "work",
        "company"
    ]

    has_experience = any(
        word in str(resume_data).lower()
        for word in experience_keywords
    )

    if has_experience:
        breakdown["experience"] = 20
        strengths.append("Experience included")
    else:
        improvements.append("Add internship or work experience")
        missing_sections.append("Experience")

    # ---------------- Achievements ----------------
    breakdown["achievements"] = 0
    improvements.append("Add certifications or achievements")
    missing_sections.append("Achievements")

    overall_score = sum(breakdown.values())

    return {
        "overall_score": overall_score,
        "score_breakdown": breakdown,
        "strengths": strengths,
        "improvements": improvements,
        "missing_sections": missing_sections
    }
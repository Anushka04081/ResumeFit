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

    # ---------- Contact (10) ----------
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

    # ---------- Skills (30) ----------
    skills = resume_data.get("skills", [])
    print("Skills:", resume_data.get("skills"))
    implemented = sum(1 for skill in skills if skill.get("implemented"))
    mentioned = sum(1 for skill in skills if skill.get("mentioned"))

    breakdown["skills"] = min(30, implemented * 5 + (mentioned - implemented) * 2)

    if breakdown["skills"] >= 20:
        strengths.append("Good practical technical skills")
    else:
        improvements.append("Implement more listed skills in projects")

    # ---------- Projects (20) ----------
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

    # ---------- Education (10) ----------
    education = resume_data.get("education", [])

    if education:
        breakdown["education"] = 10
        strengths.append("Education section present")
    else:
        missing_sections.append("Education")

    # ---------- Experience (20) ----------
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

    # ---------- Achievements (10) ----------
    achievement_keywords = [
        "certificate",
        "certification",
        "achievement",
        "award",
        "hackathon"
    ]

    has_achievement = any(
        word in str(resume_data).lower()
        for word in achievement_keywords
    )

    if has_achievement:
        breakdown["achievements"] = 10
        strengths.append("Certifications/Achievements included")
    else:
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
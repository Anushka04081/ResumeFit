def calculate_score(resume_data):

    score = 0
    strengths = []
    improvements = []

    # Skills (40 points)
    skills = resume_data.get("skills", [])

    if len(skills) >= 5:
        score += 40
        strengths.append("Good technical skill set")
    elif len(skills) > 0:
        score += 25
        improvements.append("Add more technical skills")


    # Projects (25 points)
    projects = resume_data.get("projects", [])

    if len(projects) >= 2:
        score += 25
        strengths.append("Multiple projects included")

    elif len(projects) == 1:
        score += 15
        strengths.append("Project included")
        improvements.append("Add more projects")

    else:
        improvements.append("Add practical projects")


    # Education (20 points)
    education = resume_data.get("education", [])

    if len(education) > 0:
        score += 20
        strengths.append("Education details provided")

    else:
        improvements.append("Add education details")


    # Training/Experience (15 points)
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
        score += 15
        strengths.append("Experience mentioned")

    else:
        improvements.append("Add internship or work experience")


    return {
        "resume_score": score,
        "strengths": strengths,
        "improvements": improvements
    }
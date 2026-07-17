from skills_database import SKILL_EVIDENCE


def check_skill_evidence(skill, projects, training):

    evidence = []

    project_text = ""

    for project in projects:
        project_text += project.get("title", "") + " "
        project_text += " ".join(project.get("description", [])) + " "

    training_text = " ".join(training)

    combined_text = (project_text + training_text).lower()

    keywords = SKILL_EVIDENCE.get(skill, [skill.lower()])

    for keyword in keywords:
        if keyword.lower() in combined_text:
            evidence.append(keyword)

    return {
        "name": skill,
        "mentioned": True,
        "implemented": len(evidence) > 0,
        "evidence": list(set(evidence))
    }
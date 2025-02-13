def draft_comment(score: int) -> str:
    if score >= 15:
        return "High-risk PR: recommend deep review and targeted tests."
    if score >= 8:
        return "Medium-risk PR: review key logic and regression paths."
    return "Low-risk PR: standard review should be sufficient."

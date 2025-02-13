from .models import ChangeSummary


def risk_score(change: ChangeSummary) -> int:
    return change.files_changed * 2 + (change.lines_added + change.lines_deleted) // 50

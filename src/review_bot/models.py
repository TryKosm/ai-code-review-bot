from dataclasses import dataclass


@dataclass
class ChangeSummary:
    files_changed: int
    lines_added: int
    lines_deleted: int

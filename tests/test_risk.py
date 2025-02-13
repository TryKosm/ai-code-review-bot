from review_bot.models import ChangeSummary
from review_bot.risk import risk_score


def test_risk_score_increases_with_size() -> None:
    assert risk_score(ChangeSummary(1, 10, 5)) < risk_score(ChangeSummary(8, 300, 200))

import pytest
from backend.app.tools.data_tools import calculate_percentage, summarize_ticket_fares

def test_calculate_percentage():
    assert calculate_percentage(50, 200) == 25.0
    assert calculate_percentage(0, 100) == 0.0
    assert calculate_percentage(100, 0) == 0.0  # Edge case: division by zero

def test_summarize_ticket_fares():
    fares = [10, 20, 30, 40, 50]
    summary = summarize_ticket_fares(fares)
    assert summary['mean'] == 30.0
    assert summary['median'] == 30.0
    assert summary['min'] == 10
    assert summary['max'] == 50
    assert summary['std_dev'] == pytest.approx(15.81, rel=1e-2)  # Allowing for floating point precision
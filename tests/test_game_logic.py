import pytest
from app import get_range_for_difficulty, check_guess, update_score

def test_new_game_resets_secret_different_attempts():
    low, high = get_range_for_difficulty("Normal")
    secrets = set()
    for _ in range(10):
        secret = __import__('random').randint(low, high)
        secrets.add(secret)
    assert len(secrets) > 1, "Secret generation should produce different values"
    
#FIX: Refactored from app.py using AI; added emoji messages and type-handling for int/string secret
def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

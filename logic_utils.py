def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""

    if difficulty == "Easy":
        return (1, 20)
    elif difficulty == "Normal":
        return (1, 100)
    elif difficulty == "Hard":
        return (1, 50)
    else:
        return (1, 100)


def parse_guess(raw: str): #FIX: Added AI suggestion to handle invalid input gracefully
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """

    try:
        guess = int(raw)
        return (True, guess, None)
    except ValueError:
        return (False, None, "That is not a number.")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """

    if guess == secret:
        return ("Win", "Correct!")
    elif guess > secret:
        return ("Too High", "Too high!")
    else:
        return ("Too Low", "Too low!")

#FIX: Refactored scoring logic using AI; ensures minimum 10 points on win
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points
    else:
        return current_score
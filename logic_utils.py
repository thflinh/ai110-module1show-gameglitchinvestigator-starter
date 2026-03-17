def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    # FIX: Refactored difficulty range logic into logic_utils.py with AI assistance.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)

    # FIX: Refactored parse_guess into logic_utils.py using Agent mode.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"

    # FIX: Moved check_guess here and corrected high/low hint logic with AI guidance.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # Ensure numeric comparison and consistent messages.
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = int(guess)
        s = int(secret)
        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    # FIX: Refactored scoring logic into logic_utils.py using AI as a collaborator.
    """
    if outcome == "Win":
        # Simple scoring: earlier wins get more points.
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        # Penalize incorrect guesses consistently.
        return current_score - 5

    return current_score

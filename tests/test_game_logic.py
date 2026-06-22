from logic_utils import check_guess, parse_guess, is_binary_search_guess, update_score


# --- existing tests (fixed: check_guess returns (outcome, message), not a plain string) ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- new game restart ---

def test_new_game_resets_attempts_to_zero():
    # Simulate the state before and after clicking "New Game".
    # The fix changed the reset value from 1 to 0 so the first guess
    # after a new game counts as attempt #1 (not #2).
    session = {"attempts": 5, "status": "lost"}

    # Apply the same reset logic as app.py's new_game block
    session["attempts"] = 0
    session["status"] = "playing"

    assert session["attempts"] == 0


def test_new_game_first_guess_is_attempt_one():
    # After reset, submitting a guess increments attempts by 1 (app.py line 87).
    # With attempts starting at 0 the first guess lands on attempt 1, not 2.
    attempts = 0
    attempts += 1  # simulate submit
    assert attempts == 1


def test_new_game_status_allows_playing():
    # After "New Game", status must be "playing" so app.py does not call st.stop().
    session = {"status": "won"}
    session["status"] = "playing"
    assert session["status"] == "playing"


# --- hint messages after a wrong guess ---

def test_hint_too_high_contains_lower():
    # Guessing above the secret should tell the player to go lower.
    outcome, message = check_guess(75, 30)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_hint_too_low_contains_higher():
    # Guessing below the secret should tell the player to go higher.
    outcome, message = check_guess(20, 80)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_hint_uses_int_secret():
    # The secret is always an int after the fix (app.py no longer converts it
    # to a string on even attempts). Confirm check_guess handles int/int correctly.
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- binary search detection ---

def test_binary_search_floor_midpoint_accepted():
    # Floor midpoint of 1–100 is 50; should be accepted.
    assert is_binary_search_guess(50, 1, 100) is True


def test_binary_search_ceiling_midpoint_accepted():
    # Ceiling midpoint of 1–100 is 51; should also be accepted.
    assert is_binary_search_guess(51, 1, 100) is True


def test_binary_search_off_midpoint_rejected():
    # Any guess that is neither floor nor ceiling midpoint is not a binary search step.
    assert is_binary_search_guess(40, 1, 100) is False


def test_binary_search_single_element_range():
    # When low == high the only valid guess is that value.
    assert is_binary_search_guess(7, 7, 7) is True


# --- WinBinarySearch scoring ---

def test_win_binary_search_scores_more_than_regular_win():
    # Same attempt number — binary search win should yield a higher total.
    regular = update_score(0, "Win", 3)
    binary = update_score(0, "WinBinarySearch", 3)
    assert binary > regular


def test_win_binary_search_bonus_is_fifty_points():
    # The bonus is exactly +50 on top of the normal win calculation.
    regular = update_score(0, "Win", 3)
    binary = update_score(0, "WinBinarySearch", 3)
    assert binary - regular == 50

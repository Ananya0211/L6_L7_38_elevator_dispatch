import pytest
from elevator_dispatch import next_direction, door_action, pick_elevator


# --- Comprehensive Branch Tests for door_action ---
def test_door_emergency_branch():
    assert door_action(700, True, True) == "hold_open"


def test_door_overload_boundary_and_branch():
    # Exactly at 630 kg (False branch of load_kg > 630)
    assert door_action(630, False, False) == "close"
    # Over 630 kg (True branch of load_kg > 630)
    assert door_action(631, False, False) == "overload"


def test_door_blocked_branch():
    # Blocked True
    assert door_action(500, True, False) == "reopen"
    # Blocked False
    assert door_action(500, False, False) == "close"


# --- Comprehensive Branch Tests for next_direction ---
def test_next_direction_branch_evaluations():
    # Covers f == current, f > current, and f < current in generator comprehensions
    reqs_mixed = [1, 3, 5]

    # direction == "up"
    assert next_direction(3, "up", reqs_mixed) == "up"     # above=True
    assert next_direction(3, "up", [1]) == "down"          # above=False, below=True
    assert next_direction(3, "up", [3]) == "idle"          # above=False, below=False

    # direction == "down"
    assert next_direction(3, "down", reqs_mixed) == "down" # below=True
    assert next_direction(3, "down", [5]) == "up"          # below=False, above=True
    assert next_direction(3, "down", []) == "idle"         # below=False, above=False

    # direction != "up" and direction != "down" (e.g. "idle" or unknown)
    assert next_direction(3, "idle", [5]) == "up"          # above=True
    assert next_direction(3, "idle", [1]) == "down"        # above=False, below=True
    assert next_direction(3, "idle", []) == "idle"         # above=False, below=False


# --- Comprehensive Branch Tests for pick_elevator ---
def test_pick_elevator_branches():
    # 1. Empty cars list (loop does not execute)
    assert pick_elevator([], 1) is None

    # 2. Loop branch conditions:
    # - Car 1: best is None (initializes best and best_gap)
    # - Car 2: not is_idle is True (adds +5 penalty), gap is larger (gap < best_gap is False)
    # - Car 3: not is_idle is False, gap is strictly smaller (gap < best_gap is True with best not None)
    cars = [
        ("Alpha", 5, True),   # gap = 5 - 4 = 1 (best initialized)
        ("Beta", 4, False),   # gap = |4 - 4| + 5 = 5 (5 < 1 is False)
        ("Gamma", 4, True),   # gap = |4 - 4| = 0 (0 < 1 is True, best updated)
    ]
    assert pick_elevator(cars, 4) == "Gamma"
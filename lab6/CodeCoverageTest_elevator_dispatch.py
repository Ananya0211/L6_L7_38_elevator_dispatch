import pytest
from elevator_dispatch import next_direction, door_action, pick_elevator


# --- Tests for door_action ---
def test_door_action_emergency():
    assert door_action(100, False, True) == "hold_open"


def test_door_action_overload():
    assert door_action(650, False, False) == "overload"


def test_door_action_blocked():
    assert door_action(300, True, False) == "reopen"


def test_door_action_close():
    assert door_action(300, False, False) == "close"


# --- Tests for next_direction ---
def test_next_direction_up_has_above():
    assert next_direction(2, "up", [1, 2, 4]) == "up"


def test_next_direction_up_only_below():
    assert next_direction(4, "up", [1, 2]) == "down"


def test_next_direction_up_no_calls():
    assert next_direction(3, "up", [3]) == "idle"


def test_next_direction_down_has_below():
    assert next_direction(5, "down", [2, 6]) == "down"


def test_next_direction_down_only_above():
    assert next_direction(1, "down", [3, 4]) == "up"


def test_next_direction_down_no_calls():
    assert next_direction(2, "down", []) == "idle"


def test_next_direction_idle_has_above():
    assert next_direction(2, "idle", [5]) == "up"


def test_next_direction_idle_only_below():
    assert next_direction(4, "idle", [1]) == "down"


def test_next_direction_idle_no_calls():
    assert next_direction(3, "idle", []) == "idle"


# --- Tests for pick_elevator ---
def test_pick_elevator_empty():
    assert pick_elevator([], 3) is None


def test_pick_elevator_idle_and_moving():
    # Car A is idle at floor 2 (gap = |2 - 5| = 3)
    # Car B is busy at floor 4 (gap = |4 - 5| + 5 = 6)
    # Car C is idle at floor 9 (gap = |9 - 5| = 4, gap not smaller than 3)
    cars = [("CarA", 2, True), ("CarB", 4, False), ("CarC", 9, True)]
    assert pick_elevator(cars, 5) == "CarA"
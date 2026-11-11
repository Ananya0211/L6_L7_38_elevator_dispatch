import pytest
from hypothesis import given, strategies as st
from elevator_dispatch import parse_request, total_travel, load_percent


# --- Fuzz Tests: Ensure arbitrary string or None never causes an unhandled crash ---

@given(st.text() | st.none())
def test_parse_request_no_crash(s):
    parse_request(s)


@given(st.text() | st.none())
def test_total_travel_no_crash(s):
    total_travel(s)


@given(st.text() | st.none())
def test_load_percent_no_crash(s):
    load_percent(s)


# --- Valid Input Property Tests (verifies correct functionality) ---

@given(st.integers(min_value=-1000, max_value=1000), st.integers(min_value=-1000, max_value=1000))
def test_parse_request_valid(start, end):
    req_str = f"{start}->{end}"
    assert parse_request(req_str) == (start, end)


@given(st.integers(min_value=0, max_value=10000), st.integers(min_value=1, max_value=10000))
def test_load_percent_valid(load, capacity):
    text = f"{load} of {capacity}"
    expected = (load * 100) // capacity
    assert load_percent(text) == expected
import hashlib

from nlr_psm3_2_epw.validation import (
    API_KEY_LENGTH,
    is_api_key_valid,
    is_api_key_verified,
    normalize_api_key,
)


def _key(n: int) -> str:
    return "a" * n


# --- normalize_api_key -------------------------------------------------------


def test_normalize_api_key_handles_none():
    assert normalize_api_key(None) == ""


def test_normalize_api_key_strips_surrounding_whitespace():
    assert normalize_api_key("  abc\n") == "abc"


# --- is_api_key_verified -----------------------------------------------------


def test_is_api_key_verified_true_for_matching_hash():
    key = _key(API_KEY_LENGTH)
    digest = hashlib.sha256(key.encode()).hexdigest()
    assert is_api_key_verified(key, digest) is True


def test_is_api_key_verified_ignores_surrounding_whitespace():
    key = _key(API_KEY_LENGTH)
    digest = hashlib.sha256(key.encode()).hexdigest()
    # a stray trailing newline must not change verification
    assert is_api_key_verified(f"  {key}\n", digest) is True


def test_is_api_key_verified_false_for_mismatch():
    assert is_api_key_verified(_key(API_KEY_LENGTH), "deadbeef") is False


def test_is_api_key_verified_false_for_empty():
    assert is_api_key_verified("   ", "deadbeef") is False
    assert is_api_key_verified(None, "deadbeef") is False


# --- is_api_key_valid --------------------------------------------------------


def test_is_api_key_valid_empty_is_false():
    assert is_api_key_valid("") is False
    assert is_api_key_valid(None) is False
    assert is_api_key_valid("   ") is False


def test_is_api_key_valid_exact_length():
    assert is_api_key_valid(_key(API_KEY_LENGTH)) is True


def test_is_api_key_valid_wrong_length():
    assert is_api_key_valid(_key(API_KEY_LENGTH - 1)) is False
    assert is_api_key_valid(_key(API_KEY_LENGTH + 1)) is False


def test_is_api_key_valid_trims_before_length_check():
    # Regression: a 40-char key with a trailing newline (as delivered by
    # st.secrets / env vars) was read as 41 chars and disabled the button.
    assert is_api_key_valid(f"{_key(API_KEY_LENGTH)}\n") is True


def test_is_api_key_valid_verified_default_bypasses_length():
    assert is_api_key_valid(_key(10), is_verified=True) is True


def test_is_api_key_valid_verified_but_empty_is_false():
    assert is_api_key_valid("", is_verified=True) is False

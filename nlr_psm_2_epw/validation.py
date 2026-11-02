"""Pure, UI-free validation helpers for the NLR -> EPW app.

These rules live in the library package (rather than in ``app/streamlit_app.py``)
so they can be unit-tested directly. The Streamlit UI module is hard to exercise
end-to-end and is excluded from coverage, so a length-check regression once
shipped there unnoticed and disabled the request button. Keeping the logic here
means the test suite actually covers it.
"""

import hashlib
from typing import Optional

# NLR / api.data.gov keys are exactly this many characters.
API_KEY_LENGTH = 40


def normalize_api_key(raw: Optional[str]) -> str:
    """Trim surrounding whitespace, treating ``None`` as an empty key.

    Keys read from ``st.secrets`` or environment variables frequently carry a
    trailing newline; normalizing once keeps every downstream check honest.
    """
    return (raw or "").strip()


def is_api_key_verified(api_key: Optional[str], valid_hash: str) -> bool:
    """True if the whitespace-trimmed key hashes to ``valid_hash``."""
    key = normalize_api_key(api_key)
    if not key:
        return False
    return hashlib.sha256(key.encode()).hexdigest() == valid_hash


def is_api_key_valid(api_key: Optional[str], *, is_verified: bool = False) -> bool:
    """Whether a key is usable for an NLR request.

    A key is valid if it is the verified default key, or if it is exactly
    :data:`API_KEY_LENGTH` characters after trimming whitespace. The trim is the
    point: a verified key with a stray trailing newline used to read as 41
    characters and silently disable the request button.
    """
    key = normalize_api_key(api_key)
    if not key:
        return False
    if is_verified:
        return True
    return len(key) == API_KEY_LENGTH

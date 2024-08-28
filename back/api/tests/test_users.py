"""
Tests for the users app.
"""

import pytest


@pytest.mark.django_db
def test_addition():
    """Test that 1 + 1 equals 2."""
    assert 1 + 1 == 2

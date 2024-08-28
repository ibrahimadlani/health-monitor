""" Tests for the users app. """

import pytest


@pytest.mark.django_db
def test_addition():
    assert 1 + 1 == 2

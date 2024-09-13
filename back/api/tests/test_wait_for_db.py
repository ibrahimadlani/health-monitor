"""
Wait for database command tests.
"""

from unittest.mock import patch
import pytest
from django.core.management import call_command
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


@pytest.mark.django_db
class TestWaitForDatabaseCommand:
    """
    Test the wait_for_db command
    """

    @patch("time.sleep")  # To skip real time.sleep calls and speed up tests
    def test_wait_for_db_ready(self, patched_sleep):  # pylint: disable=unused-argument
        """Test waiting for the database when the database is available immediately."""
        with patch("django.core.management.base.BaseCommand.check") as mock_check:
            mock_check.return_value = True  # Simulate database is available

            call_command("wait_for_db")

            mock_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")  # To skip real time.sleep calls and speed up tests
    def test_wait_for_db_delay(self, patched_sleep):  # pylint: disable=unused-argument
        """Test waiting for the database with OperationalError raised multiple times."""
        with patch("django.core.management.base.BaseCommand.check") as mock_check:
            # Raise errors the first two times, then succeed
            mock_check.side_effect = [Psycopg2OpError, OperationalError, True]

            call_command("wait_for_db")

            assert (
                mock_check.call_count == 3
            )  # The command should retry twice before succeeding
            mock_check.assert_called_with(databases=["default"])

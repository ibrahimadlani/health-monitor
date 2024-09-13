"""
Test the urls of the api app
"""

from django.urls import reverse, resolve
from django.test import TestCase
from api.views import UserDetailView, UserListView


class TestUrls(TestCase):
    """
    Test the urls of the api app
    """

    def test_user_list_create_url(self):
        """
        Check if the user list and create url is correct
        """
        url = reverse("user-list")
        self.assertEqual(resolve(url).func.view_class, UserListView)

    def test_user_retrieve_update_destroy_url(self):
        """
        Check if the user retrieve, update and destroy url is correct
        """
        url = reverse("user-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, UserDetailView)

import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
# from django.core.urlresolvers import reverse (article code, outdated maybe)

from rest_framework.test import APIClient
from rest_framework import status

from .models import Pomo

class ModelTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.pomo_name = "Personal Project - Pomo API"
        self.pomo_observation = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        self.pomo_start = timezone.now()
        self.pomo_end = timezone.now() + datetime.timedelta(minutes=30)
        self.pomo = Pomo(name=self.pomo_name, observation=self.pomo_observation, start=self.pomo_start, end=self.pomo_end)

    def test_model_can_create_a_pomo(self):
        """Test the pomo model can create a pomo."""
        old_count = Pomo.objects.count()
        self.pomo.save()
        new_count = Pomo.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.pomo_data = {
                'name': 'Sketch1 - gamedev',
                'observation': 'Project setup',
                'start': timezone.now(),
                'end': timezone.now() + datetime.timedelta(minutes=30)
            }
        self.response = self.client.post(
            reverse('create'),
            self.pomo_data,
            format="json")

    def test_api_can_create_a_pomo(self):
        """Test the api has pomo creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_pomo(self):
        """Test the api can get a given pomo."""
        pomo = Pomo.objects.get()
        response = self.client.get(
            reverse('detail', kwargs={'pk': pomo.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, pomo.id)

    def test_api_can_update_pomo(self):
        """Test the api can update a given pomo."""
        pomo = Pomo.objects.get()
        change_pomo = {"name":"Personal Project - Pomo API 2"}
        res = self.client.put(reverse('detail', kwargs={'pk': pomo.id}),
            change_pomo, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_pomo(self):
        """Test the api can delete a pomo."""
        pomo = Pomo.objects.get()
        response = self.client.delete(
            reverse('detail', kwargs={'pk': pomo.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
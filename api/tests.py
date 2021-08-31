import datetime
from django.test import TestCase
from django.utils import timezone
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

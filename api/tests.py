from django.test import TestCase
from .models import Pomo

class ModelTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.pomo_name = "Personal Project - Pomo API"
        self.pomo = Pomo(name=self.pomo_name)

    def test_model_can_create_a_pomo(self):
        """Test the pomo model can create a pomo."""
        old_count = Pomo.objects.count()
        self.pomo.save()
        new_count = Pomo.objects.count()
        self.assertNotEqual(old_count, new_count)

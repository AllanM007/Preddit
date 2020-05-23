from django.test import TestCase
from red1.models import Subweddit


class SubwedditTestCase(TestCase):
    def testSubweddit(self):
        subweddit = Subweddit(name="w/cars", created_on="2020-4-20", bio="I am Odin", guidelines="OdinForce", slug="cars")
        self.assertEqual(subweddit.name, "w/cars")
        self.assertEqual(subweddit.created_on, "2020-4-20")
        self.assertEqual(subweddit.bio, "I am Odin")
        self.assertEqual(subweddit.guidelines, "OdinForce")
        self.assertEqual(subweddit.slug, "cars")
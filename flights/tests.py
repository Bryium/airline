from django.test import TestCase
from django.test import Client, TestCase

from .models import Airport, Flight, Paasenger

# Create your tests here.

class FlightTestCase(TestCase):

  def setUp(self):

    #Create airports
    a1 = Airport.objects.create(code="AAA", city="City A")
    a2 = Airport.objects.create(code="BBB", city="City B")

    #Create flights.
    Flight.objects.create(origin=a1, destination=a2, duration=100)
    Flight.objects.create(origin=a1, destination=a1, duration=200)
    Flight.objects.create(origin=a1, destination=a2, duration=100)

  def test_departures_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.departures.count(), 3)

  def test_arrival_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.arrival.count(), 1)


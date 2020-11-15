from django.test import TestCase, Client
from django.urls import resolve
from .models import Testi
#from .views import testi, tampilan
from .apps import TestiConfig

class TestModels(TestCase):
    def test_model_can_create(self):
        new_activity = Testi.objects.create(nama="Lary", institusi="Bikiny bottom", testimoni="Tuan Krabs peelit")
        counting_all_available_todo = Testi.objects.all().count()
        self.assertEqual(counting_all_available_todo, 1)

    def test_model_can_print(self):
        kegiatan = Testi.objects.create(nama="Lary", institusi="Bikiny bottom", testimoni="Tuan Krabs peelit")
        self.assertEqual(kegiatan.__str__(), "Lary")

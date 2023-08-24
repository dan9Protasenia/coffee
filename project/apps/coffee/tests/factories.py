import factory

from project.apps.coffee.models import Coffee
from project.apps.coffee.tests.constants import (
    Title,
    Description,
    Price,
    Test_Image,
    Info)


class CoffeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Coffee

    title = Title
    description = Description
    price = Price
    pictures = Test_Image
    info = Info

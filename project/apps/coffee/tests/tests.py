import pytest
from django.urls import reverse

from project.apps.coffee.models import Coffee
from project.apps.coffee.tests.constants import (
    Title,
    Description,
    Price,
    Test_Image,
    Info,
    Update_Title,
    Updated_Description,
    Update_Price,
    Updated_Info
)
from .factories import CoffeeFactory

pytestmark = pytest.mark.django_db


def test_connect(client):
    response = client.get(reverse('coffee'))
    assert response.status_code == 200


def test_create(client):
    response = client.get(reverse('create'))
    assert response.status_code == 200

    data = {
        'title': Title,
        'description': Description,
        'price': Price,
        'pictures': Test_Image,
        'info': Info
    }

    response = client.post(reverse('create'), data)

    assert response.status_code == 302
    assert Coffee.objects.exists()


def test_info(client):
    coffee_object = CoffeeFactory()
    url = reverse('info', kwargs={'pk': coffee_object.pk})

    response = client.get(url)

    assert response.status_code == 200
    assert coffee_object.info.encode() \
           and coffee_object.title.encode() in response.content

    non_existent_pk = coffee_object.pk + 1
    url = reverse('info', kwargs={'pk': non_existent_pk})
    response = client.get(url)
    assert response.status_code == 404


def test_update(client):
    coffee_object = CoffeeFactory()
    url = reverse('update', kwargs={'pk': coffee_object.pk})

    response = client.get(url)
    assert response.status_code == 200

    update_data = {
        'title': Update_Title,
        'description': Updated_Description,
        'price': Update_Price,
        'info': Updated_Info
    }

    response = client.post(url, update_data)

    coffee_object.refresh_from_db()

    assert coffee_object.title == update_data.get('title')
    assert coffee_object.description == update_data.get('description')
    assert coffee_object.price == update_data.get('price')
    assert coffee_object.info == update_data.get('info')

    assert response.status_code == 302


def test_delete(client):
    coffee_object = CoffeeFactory()
    url = reverse('delete', kwargs={'pk': coffee_object.pk})

    response = client.post(url)
    assert response.status_code == 302

    assert not Coffee.objects.exists()

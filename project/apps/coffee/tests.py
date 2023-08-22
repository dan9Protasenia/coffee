import pytest
from django.urls import reverse

from .models import Coffee


@pytest.mark.django_db
def test_connect(client):
    response = client.get(reverse('coffee'))
    assert response.status_code == 200


@pytest.fixture
def create_coffee():
    coffee_object = Coffee.objects.create(
        title='Test Coffee',
        description='Test Description',
        price=10,
        pictures='test_image.jpg',
        info='Test Info'
    )
    return coffee_object


@pytest.mark.django_db
def test_create(client):
    response = client.get(reverse('create'))
    assert response.status_code == 200

    data = {
        'title': 'Title',
        'description': 'Description',
        'price': 10,
        'pictures': 'my_image.jpg',
        'info': 'Info'
    }

    response = client.post(reverse('create'), data)

    assert response.status_code == 302
    assert Coffee.objects.exists()


@pytest.mark.django_db
def test_info(client, create_coffee):
    coffee_object = create_coffee
    url = reverse('info', kwargs={'pk': coffee_object.pk})

    response = client.get(url)

    assert response.status_code == 200
    assert coffee_object.info.encode() \
           and coffee_object.title.encode() in response.content

    non_existent_pk = coffee_object.pk + 1
    url = reverse('info', kwargs={'pk': non_existent_pk})
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_update(client, create_coffee):
    coffee_object = create_coffee
    url = reverse('update', kwargs={'pk': coffee_object.pk})

    response = client.get(url)
    assert response.status_code == 200

    update_data = {
        'title': 'Updated Coffee',
        'description': 'Updated Description',
        'price': 15,
        'info': 'Updated Info'
    }

    response = client.post(url, update_data)

    coffee_object.refresh_from_db()

    assert coffee_object.title == update_data['title']
    assert coffee_object.description == update_data['description']
    assert coffee_object.price == update_data['price']
    assert coffee_object.info == update_data['info']

    assert response.status_code == 302


@pytest.mark.django_db
def test_delete(client, create_coffee):
    coffee_object = create_coffee
    url = reverse('delete', kwargs={'pk': coffee_object.pk})

    response = client.post(url)
    assert response.status_code == 302

    assert not Coffee.objects.exists()

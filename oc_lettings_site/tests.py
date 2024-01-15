from django.test import Client
from django.urls import reverse


def test_index():
    client = Client()
    response = client.get(reverse('index'))
    assert response.request['PATH_INFO'] == '/'
    assert response.status_code == 200
    assert 'Welcome to the new Holiday Homes' in response.content.decode()
    assert 'Profiles' in response.content.decode()
    assert 'Lettings' in response.content.decode()

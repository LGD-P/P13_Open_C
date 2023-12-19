from django.test import TestCase, Client
from django.urls import reverse


from lettings.models import Letting, Address


class LettingsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('lettings_index')
        self.address_1 = Address.objects.create(
            number=123, street="northenlight street", city="Tromso",
            state="Norway", zip_code=9000, country_iso_code="NOR")

        self.address_2 = Address.objects.create(
            number=456, street="Eyjafjallajökull street",
            city="Reykjavík", state="Island",
            zip_code=101, country_iso_code="ISL")

        self.letting_1 = Letting.objects.create(title='Under the Light',
                                                address=self.address_1)
        self.letting_2 = Letting.objects.create(title='Unpronounceable',
                                                address=self.address_2)

        self.letting_1_url = reverse('letting', args=['1'])
        self.letting_2_url = reverse('letting', args=['2'])

    def test_lettings_index_view(self):
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('lettings_list', response.context)
        self.assertIn('1', response.content.decode())
        self.assertIn('2', response.content.decode())
        lettings_list = response.context['lettings_list']
        self.assertEqual(lettings_list.count(), 2)
        self.assertEqual(lettings_list.first(), self.letting_1)

    def test_index_view_no_lettings(self):
        Letting.objects.all().delete()
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn('lettings_list', response.context)
        lettings_list = response.context['lettings_list']
        self.assertEqual(lettings_list.count(), 0)
        self.assertIn("No lettings are available", response.content.decode())

    def test_lettings_view(self):
        response = self.client.get(self.letting_1_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        assert response.request['PATH_INFO'] == '/lettings/lettings/1/'
        self.assertIn('Under the Light', response.content.decode())
        self.assertIn('123 northenlight street', response.content.decode())
        self.assertContains(response, '<p>Tromso, Norway 9000</p>')
        response_letting_2 = self.client.get(self.letting_2_url)
        self.assertEqual(response_letting_2.status_code, 200)
        self.assertTemplateUsed(response_letting_2, 'lettings/letting.html')
        assert response_letting_2.request['PATH_INFO'] == '/lettings/lettings/2/'
        self.assertIn('Unpronounceable', response_letting_2.content.decode())
        self.assertIn('Eyjafjallajökull street', response_letting_2.content.decode())
        self.assertContains(response_letting_2, '<p>Reykjavík, Island 101</p>')

    def test_no_lettings_view(self):
        Letting.objects.all().delete()
        response = self.client.get(self.letting_1_url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        self.assertIn('ERROR 404', response.content.decode())
        self.assertIn('the requested page could not be found',
                      response.content.decode())

    def test_model_method(self):

        self.assertEqual(str(self.address_1), "123 northenlight street")
        self.assertEqual(str(self.address_2), "456 Eyjafjallajökull street")
        self.assertEqual(str(self.letting_1), 'Under the Light')
        self.assertEqual(str(self.letting_2), 'Unpronounceable')

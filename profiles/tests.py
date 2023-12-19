from django.test import TestCase, Client
from django.urls import reverse


from profiles.models import Profile
from django.contrib.auth.models import User


class ProfilesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('profiles_index')
        self.user_1 = User.objects.create_user(username='user_1',
                                               first_name='John',
                                               last_name='Doe',
                                               email='JohnDoe@gmail.com')
        self.user_2 = User.objects.create_user(username='user_2',
                                               first_name='Neo',
                                               last_name='Anderson',
                                               email='whiterabbit@gmx.com')
        self.profile_1 = Profile.objects.create(user=self.user_1,
                                                favorite_city='Paris')
        self.profile_2 = Profile.objects.create(user=self.user_2,
                                                favorite_city='Luang PraBang')
        self.profile_1_url = reverse('profile', args=['user_1'])
        self.profile_2_url = reverse('profile', args=['user_2'])

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn('profiles_list', response.context)
        self.assertIn('user_1', response.content.decode())
        self.assertIn('user_2', response.content.decode())
        profiles_list = response.context['profiles_list']
        self.assertEqual(profiles_list.count(), 2)
        self.assertEqual(profiles_list.first(), self.profile_1)

    def test_profiles_index_view_no_profiles(self):
        Profile.objects.all().delete()
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn('profiles_list', response.context)
        profiles_list = response.context['profiles_list']
        self.assertEqual(profiles_list.count(), 0)
        self.assertIn("No profiles are available", response.content.decode())

    def test_profile_view(self):
        response = self.client.get(self.profile_1_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        assert response.request['PATH_INFO'] == '/profiles/profiles/user_1/'
        self.assertIn('John', response.content.decode())
        self.assertIn('Doe', response.content.decode())
        self.assertIn('JohnDoe@gmail.com', response.content.decode())
        self.assertContains(response, '<p><strong>Favorite city :</strong> Paris</p>')
        resonse_profile_2 = self.client.get(self.profile_2_url)
        self.assertEqual(resonse_profile_2.status_code, 200)
        self.assertTemplateUsed(resonse_profile_2, 'profiles/profile.html')
        self.assertIn('Neo', resonse_profile_2.content.decode())
        self.assertIn('Anderson', resonse_profile_2.content.decode())
        self.assertIn('whiterabbit@gmx.com', resonse_profile_2.content.decode())
        self.assertContains(resonse_profile_2,
                            '<p><strong>Favorite city :</strong> Luang PraBang</p>')

    def test_profile_view_no_profile(self):
        Profile.objects.all().delete()
        response = self.client.get(self.profile_1_url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        self.assertIn('ERROR 404', response.content.decode())
        self.assertIn('the requested page could not be found',
                      response.content.decode())

    def test_model_method(self):
        self.assertEqual(str(self.profile_1), 'user_1')
        self.assertEqual(str(self.profile_2), 'user_2')

from http.client import responses
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', email='<EMAIL>', password='<PASSWORD>')
        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_urls_exist_at_correct_location_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_urls_exist_at_incorrect_location_detailview(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response, 'home.html')
    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail',
            kwargs={'pk': self.post.pk}))
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

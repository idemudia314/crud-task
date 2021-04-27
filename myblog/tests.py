from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email= 'test@gmail.com',
            password='secret'

        )
        self.post = Post.objects.create(
            title= 'a good little child',
            body= 'Nice body',
            author= self.user
        )
    def test_post_representation(self):
        post= Post(title=' a simple little')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'a good little child'),
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response= self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_views(self):
        response= self.client.get('/post/5/')
        no_response= self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'a good little child')
        self.assertTemplateUsed(response, 'post_detail.html')


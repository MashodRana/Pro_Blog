from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import ArticleModel
from django.utils import timezone

# Create your tests here.
class ArticleTests(TestCase):
    """ Test the article app """
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret#$12',
            age = 20,
            profession = 'tester'
        )

        self.article = ArticleModel.objects.create(
            title='test title',
            article_writer = self.user,
            body = 'testing body',
            created_date = timezone.now(),
            published_date = timezone.now()
        )
    
    def test_article_content(self):
        self.assertEqual(str(self.article.title), 'test title'),
        self.assertEqual(str(self.article.body), 'testing body'),
        self.assertEqual(str(self.article.article_writer), 'testuser'),
    
    def test_home_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
    
    def test_home_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
class TestArticleCreateView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret#$12',
            age = 20,
            profession = 'tester'
        )

        self.article = ArticleModel.objects.create(
            title='test title',
            article_writer = self.user,
            body = 'testing body',
            created_date = timezone.now(),
            published_date = timezone.now()
        )

    def test_request(self):
        resp = self.client.get(reverse('new_article'))
        self.assertEqual(resp.status_code, 302)
        resp = self.client.get('/article/new/')
        self.assertEqual(resp.status_code, 302)
    
    def test_article_ceation(self):
        all_article = ArticleModel.objects.all()
        self.assertEqual(len(all_article), 1)
        self.assertEqual(all_article[0].article_writer,self.user)
        self.assertEqual(all_article[0].title,self.article.title)
        self.assertEqual(all_article[0].body,self.article.body)
    


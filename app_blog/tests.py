from django.test import TestCase
from django.urls import reverse, resolve
from app_blog.views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail
from datetime import date
from app_blog.models import Article, Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створення об'єкта категорії, який використовується у всіх тестах
        Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/articles/category/innovations')


class URLTests(TestCase):
    def setUp(self):
        # Створення тестових даних
        self.category = Category.objects.create(category='Test Category', slug='test-category')
        self.article = Article.objects.create(
            title='Test Article',
            slug='test-article',
            description='Test description',
            pub_date=date(2023, 12, 25),
            category=self.category
        )

    # Головна сторінка
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_resolve_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    # Список статей
    def test_articles_list_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_resolve_view(self):
        view = resolve('/articles')
        self.assertEqual(view.func.view_class, ArticleList)

    # Список статей за категорією
    def test_articles_category_list_status_code(self):
        url = reverse('articles-category-list', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_category_list_resolve_view(self):
        view = resolve(f'/articles/category/{self.category.slug}')
        self.assertEqual(view.func.view_class, ArticleCategoryList)

    # Детальний перегляд статті
    def test_article_detail_status_code(self):
        url = reverse('article-detail', kwargs={
            'year': self.article.pub_date.strftime('%Y'),
            'month': self.article.pub_date.strftime('%m'),
            'day': self.article.pub_date.strftime('%d'),
            'slug': self.article.slug,
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_resolve_view(self):
        path = f"/articles/{self.article.pub_date.strftime('%Y')}/{self.article.pub_date.strftime('%m')}/{self.article.pub_date.strftime('%d')}/{self.article.slug}"
        view = resolve(path)
        self.assertEqual(view.func.view_class, ArticleDetail)

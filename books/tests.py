from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Game Of Thrones',
            author='I dont know',
            price='150.50'
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Game Of Thrones')
        self.assertEqual(f'{self.book.author}', 'I dont know')
        self.assertEqual(f'{self.book.price}', '150.50')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Game Of Thrones')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12354')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Game Of Thrones')
        self.assertTemplateUsed(response, 'books/book_detail.html')

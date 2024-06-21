"""
Tests for the Sticky Notes application.

This module defines test cases for the models and views of the Sticky Notes
application, ensuring correct functionality for creating, updating,
and deleting notes and posts.
"""
from django.test import TestCase
from django.urls import reverse
from .models import Note, Post, Author


class AuthorModelTest(TestCase):
    """
    Test case for the Author model.
    """

    def setUp(self):
        """
        Set up a test author.
        """
        self.author = Author.objects.create(name="Test Author")

    def test_author_creation(self):
        """
        Test the creation of an author.
        """
        self.assertEqual(self.author.name, "Test Author")


class NoteModelTest(TestCase):
    """
    Test case for the Note model.
    """

    def setUp(self):
        """
        Set up a test note and author.
        """
        self.author = Author.objects.create(name="Test Author")
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            author=self.author
        )

    def test_note_creation(self):
        """
        Test the creation of a note.
        """
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note.")
        self.assertEqual(self.note.author.name, "Test Author")
        self.assertIsNotNone(self.note.created_at)


class PostModelTest(TestCase):
    """
    Test case for the Post model.
    """

    def setUp(self):
        """
        Set up a test post and author.
        """
        self.author = Author.objects.create(name="Test Author")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.author
        )

    def test_post_creation(self):
        """
        Test the creation of a post.
        """
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.author.name, "Test Author")
        self.assertIsNotNone(self.post.created_at)


class NoteViewTest(TestCase):
    """
    Test case for the Note views.
    """

    def setUp(self):
        """
        Set up a test note and author.
        """
        self.author = Author.objects.create(name="Test Author")
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            author=self.author
        )

    def test_note_list_view(self):
        """
        Test the note list view.
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_detail_view(self):
        """
        Test the note detail view.
        """
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertTemplateUsed(response, 'notes/note_detail.html')

    def test_note_create_view(self):
        """
        Test the note create view.
        """
        response = self.client.post(reverse('note_new'), {
            'title': 'New Test Note',
            'content': 'This is a new test note.',
            'author': self.author.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.last().title, 'New Test Note')

    def test_note_update_view(self):
        """
        Test the note update view.
        """
        response = self.client.post(
            reverse('note_edit', args=[self.note.id]),
            {
                'title': 'Updated Test Note',
                'content': 'This is an updated test note.',
                'author': self.author.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Test Note')

    def test_note_delete_view(self):
        """
        Test the note delete view.
        """
        response = self.client.post(
            reverse('note_delete', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())


class PostViewTest(TestCase):
    """
    Test case for the Post views.
    """

    def setUp(self):
        """
        Set up a test post and author.
        """
        self.author = Author.objects.create(name="Test Author")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.author
        )

    def test_post_list_view(self):
        """
        Test the post list view.
        """
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, 'posts/post_list.html')

    def test_post_detail_view(self):
        """
        Test the post detail view.
        """
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, 'posts/post_detail.html')

    def test_post_create_view(self):
        """
        Test the post create view.
        """
        response = self.client.post(reverse('post_new'), {
            'title': 'New Test Post',
            'content': 'This is a new test post.',
            'author': self.author.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New Test Post')

    def test_post_update_view(self):
        """
        Test the post update view.
        """
        response = self.client.post(
            reverse('post_edit', args=[self.post.id]),
            {
                'title': 'Updated Test Post',
                'content': 'This is an updated test post.',
                'author': self.author.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Test Post')

    def test_post_delete_view(self):
        """
        Test the post delete view.
        """
        response = self.client.post(
            reverse('post_delete', args=[self.post.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

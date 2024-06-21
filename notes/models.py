"""
Models for the Sticky Notes application.

This module defines the data models for authors, notes, and posts
in the Sticky Notes application.
"""
from django.db import models


class Author(models.Model):
    """
    Model representing an author of notes and posts.
    """
    name = models.CharField(max_length=255)
    objects = models.Manager()  # Explicit manager

    def __str__(self):
        """
        String representation of the Author object.
        """
        return str(self.name)


class Note(models.Model):
    """
    Model representing a sticky note.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True
    )
    objects = models.Manager()  # Explicit manager

    def __str__(self):
        """
        String representation of the Note object.
        """
        return str(self.title)


class Post(models.Model):
    """
    Model representing a bulletin board post.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True
    )
    objects = models.Manager()  # Explicit manager

    def __str__(self):
        """
        String representation of the Post object.
        """
        return str(self.title)

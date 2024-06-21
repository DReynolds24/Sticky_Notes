"""
Forms for the Sticky Notes application.

This module defines forms for creating and updating notes and posts
in the Sticky Notes application.
"""
from django import forms
from .models import Note, Post


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating notes.
    """
    class Meta:
        """
        Meta options for the NoteForm.
        """
        model = Note
        fields = ['title', 'content']


class PostForm(forms.ModelForm):
    """
    Form for creating and updating a post.
    """
    class Meta:
        """
        Meta options for the PostForm.
        """
        model = Post
        fields = ['title', 'content', 'author']

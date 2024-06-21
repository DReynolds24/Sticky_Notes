"""
Views for the Sticky Notes application.

This module defines the views for displaying, creating, updating,
and deleting notes and posts in the Sticky Notes application.
"""
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Note, Post
from .forms import NoteForm, PostForm


class NoteListView(ListView):
    """
    View to list all notes.
    """
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    """
    View to display a specific note.
    """
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'


class NoteCreateView(CreateView):
    """
    View to create a new note.
    """
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_edit.html'

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        note = form.save(commit=False)
        note.save()
        return redirect('note_detail', pk=note.pk)


class NoteUpdateView(UpdateView):
    """
    View to edit an existing note.
    """
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_edit.html'

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        note = form.save(commit=False)
        note.save()
        return redirect('note_detail', pk=note.pk)


class NoteDeleteView(DeleteView):
    """
    View to delete a note.
    """
    model = Note
    template_name = 'notes/note_delete.html'
    success_url = reverse_lazy('note_list')


class PostListView(ListView):
    """
    View to list all posts.
    """
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """
    View to display a specific post.
    """
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    """
    View to create a new post.
    """
    model = Post
    form_class = PostForm
    template_name = 'posts/post_edit.html'

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        post = form.save(commit=False)
        post.save()
        return redirect('post_detail', pk=post.pk)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('post_detail', pk=post.pk)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
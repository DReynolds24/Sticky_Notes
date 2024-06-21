"""
URL configuration for the notes app.

This module maps URL paths to view functions for
the CRUD operations of the notes application.
"""
from django.urls import path
from .views import (
    NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView,
    NoteDeleteView, PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path(
        'note/<int:pk>/',
        NoteDetailView.as_view(),
        name='note_detail'
    ),
    path(
        'note/new/',
        NoteCreateView.as_view(),
        name='note_new'
    ),
    path(
        'note/<int:pk>/edit/',
        NoteUpdateView.as_view(),
        name='note_edit'
    ),
    path(
        'note/<int:pk>/delete/',
        NoteDeleteView.as_view(),
        name='note_delete'
    ),
    path(
        'posts/',
        PostListView.as_view(),
        name='post_list'
    ),
    path(
        'post/<int:pk>/',
        PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'post/new/',
        PostCreateView.as_view(),
        name='post_new'
    ),
    path(
        'post/<int:pk>/edit/',
        PostUpdateView.as_view(),
        name='post_edit'
    ),
    path(
        'post/<int:pk>/delete/',
        PostDeleteView.as_view(),
        name='post_delete'
    ),
]

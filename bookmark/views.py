from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.

# ListView
class BookmarkLV(ListView):
    model=Bookmark

    # template_name = 'bookmark/bookmark_list.html' #[app_name]/[model_name]_list.html
    # context_object_name = 'object_list' #object_list

# DetailView
class BookmarkDV(DetailView):
    model=Bookmark
    # template_name = 'bookmark/bookmark_detail.html' #[app_name]/[model_name]_detail.html
        # context_object_name = 'object' #object
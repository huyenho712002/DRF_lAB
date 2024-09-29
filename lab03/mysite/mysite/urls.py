from django.urls import path
from mysite.polls.views import PublisherBookListView
from mysite.polls.views import AuthorDetailView
from mysite.polls.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView
from mysite.polls.views import RecordInterestView
urlpatterns = [
    path("books/<publisher>/", PublisherBookListView.as_view()),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("author/add/", AuthorCreateView.as_view(), name="author-add"),
    path("author/<int:pk>/", AuthorUpdateView.as_view(), name="author-update"),
    path("author/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),
    path(
        "author/<int:pk>/interest/",
        RecordInterestView.as_view(),
        name="author-interest",
    ),
]
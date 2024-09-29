from django.views.generic import DetailView
from mysite.polls.models import Publisher

from django.utils import timezone
class PublisherDetailView(DetailView):
    context_object_name = "publisher"
    queryset = Publisher.objects.all()

from mysite.polls.models import Author


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj
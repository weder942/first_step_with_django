from ..models import Question
from django.views import generic
from django.utils import timezone


class DetailView(generic.DetailView):
    """"""

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
from django.shortcuts import get_object_or_404, render
from ..models import Question
from django.views import generic


class ResultsView(generic.DetailView):
    """"""

    model = Question
    template_name = 'polls/results.html'

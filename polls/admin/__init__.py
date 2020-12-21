from django.contrib import admin
from .AdminChoice import ChoiceInline
from .AdminQuestion import QuestionAdmin
from ..models import Question

admin.site.register(Question, QuestionAdmin)
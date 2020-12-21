import datetime
from django.utils import timezone
from ..models import Question


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and publish the give number of `days` offset to now
    (negative for questions published in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
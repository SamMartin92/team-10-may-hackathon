from django.shortcuts import render
from .models import Quiz

# Create your views here.
def quiz_page(request):
    """Return Quiz Page"""
    quiz = Quiz.objects.all()

    return render(request, 'quiz/quiz-page.html', {'quiz': quiz})
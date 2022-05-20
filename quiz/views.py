from django.shortcuts import render

# Create your views here.
def quiz_page(request):
    """Return Quiz Page"""

    return render(request, 'quiz/quiz-page.html')
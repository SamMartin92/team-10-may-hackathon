from django.contrib import admin
from .models import Quiz

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'optionOne',
        'optionTwo',
        'optionThree',
        'optionFour',
        'optionFive',
        'result',
    )

admin.site.register(Quiz, QuizAdmin)

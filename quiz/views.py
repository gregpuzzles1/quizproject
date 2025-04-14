# Create your views here.
# quiz/views.py

from django.shortcuts import render, redirect
from .models import Question, Choice

def quiz_view(request):
    if request.method == 'POST':
        total = 0
        correct = 0
        for question in Question.objects.all():
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(id=int(selected))
                total += 1
                if choice.is_correct:
                    correct += 1
        score = int((correct / total) * 100) if total > 0 else 0
        return render(request, 'quiz/result.html', {'score': score, 'correct': correct, 'total': total})
    else:
        questions = Question.objects.all()
        return render(request, 'quiz/quiz.html', {'questions': questions})

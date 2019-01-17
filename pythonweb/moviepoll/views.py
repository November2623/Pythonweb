from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.
def index(request):
    question_lists = Question.objects.order_by('pub_date')
    context = {'question_lists': question_lists}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return render(request,'polls/result.html',{'question': question})
from django.shortcuts import render,redirect
from .models import Question, Choice
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
             form_instance = form.save(commit=False) 
             form_instance.save()
             return redirect('feedback_success')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback_form.html', {'form': form})

def feedback_success_view(request):
    return render(request, 'feedback_success.html')

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    return render(request, 'vote.html', {'question':question, 'options': options })

def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 5
        selection_option.save()
    return render(request, 'result.html', {'question': question, 'options': options})



from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone


from .forms import NameForm

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
     model = Question
     template_name = "polls/detail.html"

     def get_queryset(self):
         return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    



def get_name(request):
    
    if request.method == "POST":
        
        form = NameForm(request.POST)
        
        if form.is_valid():
           print(form.cleaned_data)
           q = Question()
           q.question_text = form.cleaned_data["Your_Question"]
           q.pub_date = timezone.now()
           q.save()
           c1 = Choice(question = q)
           c1.choice_text = form.cleaned_data["Choice_1"]
           c1.save()
           c2 = Choice(question = q)
           c2.choice_text = form.cleaned_data["Choice_2"]
           c2.save()
           c3 = Choice(question = q)
           c3.choice_text = form.cleaned_data["Choice_3"]
           c3.save()
           c4 = Choice(question = q)
           c4.choice_text = form.cleaned_data["Choice_4"]
           c4.save()
           form = NameForm()
           return redirect("polls:index")

    
    else:
        form = NameForm()

    return render(request, "polls/question.html", {"form": form})

def delete_question(request, pk):
	queryset = Question.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect("polls:index")
	return render(request, 'polls/delete_question.html')
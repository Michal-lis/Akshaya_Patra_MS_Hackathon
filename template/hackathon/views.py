from django.shortcuts import render
from hackathon.models import Question
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        feedback = Feedback()
        feedback.title = request.POST['school']
        feedback.opinion = request.POST['opinion']
        feedback.save()
        return HttpResponse("Thank you for filling the form.")
    else:
        return render(request, "main_form.html")

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForms 

# Create your views here.

def review(request):
    if request.method == "POST":
        #entered_username = request.POST['username']
        form = ReviewForms(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
            


        # if entered_username == "" and len(entered_username) >= 100:
        #     return render(request, "reviews/review.html", {
        #         "has_error": True
        #     })
        # print(entered_username)
        # return HttpResponseRedirect("/thank-you")

    form = ReviewForms()

    return render(request, "reviews/review.html", {
        #"has_error": False
        "form": form
    })



def thank_you(request):
    return render(request, "reviews/thank_you.html")


    

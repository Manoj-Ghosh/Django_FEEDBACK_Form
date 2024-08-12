from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForms 

# Create your views here.

class ReviewView(View):
    def get(self, request):
        #Review.objects.all()
             
        form = ReviewForms()

        return render(request, "reviews/review.html", {
        #"has_error": False
        "form": form
    })

    def post(self, request):
        form = ReviewForms(request.POST)

        if form.is_valid():
            form.save()    
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
        #"has_error": False
        "form": form
    })
    
    



# def review(request):
#     if request.method == "POST":
#         #existing_model = Review.objects.get(pk=1)
#         #entered_username = request.POST['username']
#         #form = ReviewForms(request.POST, instance=existing_model)
#         form = ReviewForms(request.POST)

#         if form.is_valid():
#             form.save()
#             # print(form.cleaned_data)
#             # review = Review(user_name = form.cleaned_data['user_name'], 
#             #                 review_text = form.cleaned_data['review_text'], 
#             #                 rating = form.cleaned_data['rating'])
#             # review.save()
#             return HttpResponseRedirect("/thank-you")
            


#         # if entered_username == "" and len(entered_username) >= 100:
#         #     return render(request, "reviews/review.html", {
#         #         "has_error": True
#         #     })
#         # print(entered_username)
#         # return HttpResponseRedirect("/thank-you")
#     else:

#         form = ReviewForms()

#     return render(request, "reviews/review.html", {
#         #"has_error": False
#         "form": form
#     })


# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"



# def thank_you(request):
#     return render(request, "reviews/thank_you.html")


    

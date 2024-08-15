from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView

from .forms import ReviewForms 
from .models import Review

# Create your views here.

class ReviewView(FormView):
    form_class = ReviewForms
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    



# class ReviewView(View):
#     def get(self, request):
#         #Review.objects.all()
             
#         form = ReviewForms()

#         return render(request, "reviews/review.html", {
#         #"has_error": False
#         "form": form
#     })

#     def post(self, request):
#         form = ReviewForms(request.POST)

#         if form.is_valid():
#             form.save()    
#             return HttpResponseRedirect("/thank-you")
        
#         return render(request, "reviews/review.html", {
#         #"has_error": False
#         "form": form
#     })


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works !"
        return context



# def thank_you(request):
#     return render(request, "reviews/thank_you.html")


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_quary = super().get_queryset()
    #     data = base_quary.filter(rating__gt= 4)
    #     return data
    


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk = review_id)
#         context["reviews"] = selected_review
#         return context
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "reviews"

  
    

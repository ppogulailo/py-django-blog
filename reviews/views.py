from urllib import request

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm


# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('thank-you/')
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(req):
    return render(req, "reviews/thank-you.html")

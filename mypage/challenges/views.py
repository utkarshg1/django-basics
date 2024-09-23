from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no pizza during entire month",
    "february": "Walk for 20 minutes everyday",
    "march": "Learn Rust programming 20 minutes daily",
    "april": "Learn inline skating",
    "may": "Learning Piano Music piece",
    "june": "Learn Javascript",
    "july": "Learn Langchain",
    "august": "Diet no street food allowed",
    "september": "Learn to cook cheese balls",
    "october": "Learn to bake bread from scratch using yeast",
    "november": "Watch manufacturing engineering documentary",
    "december": None
}


def get_months():
    return list(monthly_challenges.keys())


def index(request):
    months = get_months()
    return render(request, "challenges/index.html", {
        "months_list": months
    })


def monthly_challenge_by_number(request, month):
    try:
        months = get_months()
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()

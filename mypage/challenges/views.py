from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    "december": "Cycling from home to Lonavala"
}


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
    except:
        return HttpResponseNotFound("Please enter valid month between 1 to 12")


def monthly_challenge(request, month):
    challenge_text = monthly_challenges.get(month)
    if challenge_text is not None:
        return HttpResponse(challenge_text)
    else:
        return HttpResponseNotFound("Please enter valid month!")

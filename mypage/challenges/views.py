from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Cycling from home to Lonavala"
}


def get_months():
    return list(monthly_challenges.keys())


def index(request):
    list_items = ""
    months = get_months()
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href={month_path}>{capitalized_month}</li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    try:
        months = get_months()
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>Please enter valid month between 1 to 12</h1>")


def monthly_challenge(request, month):
    challenge_text = monthly_challenges.get(month)
    if challenge_text is not None:
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    else:
        return HttpResponseNotFound("<h1>Please enter valid month!</h1>")

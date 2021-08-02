from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 30 min every day",
    "april": "April month challenge!",
    "may": "May month challenge!",
    "june": "June month challenge!",
    "july": "July month challenge!",
    "august": "August month challenge!",
    "september": "September month challenge!",
    "october": "October month challenge!",
    "november": "November month challenge!",
    "december": "December month challenge!"
}


def challenges(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month number: No challenge define")
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenge", args=[redirect_month])  # /challenges/january
    return HttpResponseRedirect(redirect_path)

    # challenge_text = None
    # if month == 1:
    #     challenge_text = "Eat no meat for the entire month"
    # elif month == 2:
    #     challenge_text = "Walk for at least 20 minutes every day!"
    # elif month == 3:
    #     challenge_text = "Learn Django for at least 30 min every day"
    # elif month == 4:
    #     challenge_text = "April month challenge!"
    # elif month == 5:
    #     challenge_text = "May month challenge!"
    # elif month == 6:
    #     challenge_text = "June month challenge!"
    # elif month == 7:
    #     challenge_text = "July month challenge!"
    # elif month == 8:
    #     challenge_text = "August month challenge!"
    # elif month == 9:
    #     challenge_text = "September month challenge!"
    # elif month == 10:
    #     challenge_text = "October month challenge!"
    # elif month == 11:
    #     challenge_text = "November month challenge!"
    # elif month == 12:
    #     challenge_text = "December month challenge!"
    # else:
    #     challenge_text = "Invalid month number: No challenge define"
    #     return HttpResponseNotFound(challenge_text)
    #
    # return HttpResponse(challenge_text)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except KeyError as e:
        challenge_text = "Invalid month: No challenge define"
        return HttpResponseNotFound(challenge_text)

    # challenge_text = None
    # if month.lower() == 'january':
    #     challenge_text = "Eat no meat for the entire month"
    # elif month.lower() == 'february':
    #     challenge_text = "Walk for at least 20 minutes every day!"
    # elif month.lower() == 'march':
    #     challenge_text = "Learn Django for at least 30 min every day"
    # elif month.lower() == 'april':
    #     challenge_text = "April month challenge!"
    # elif month.lower() == 'may':
    #     challenge_text = "May month challenge!"
    # elif month.lower() == 'june':
    #     challenge_text = "June month challenge!"
    # elif month.lower() == 'july':
    #     challenge_text = "July month challenge!"
    # elif month.lower() == 'august':
    #     challenge_text = "August month challenge!"
    # elif month.lower() == 'september':
    #     challenge_text = "September month challenge!"
    # elif month.lower() == 'october':
    #     challenge_text = "October month challenge!"
    # elif month.lower() == 'november':
    #     challenge_text = "November month challenge!"
    # elif month.lower() == 'december':
    #     challenge_text = "December month challenge!"
    # else:
    #     challenge_text = "Invalid month: No challenge define"
    #     return HttpResponseNotFound(challenge_text)
    #
    # return HttpResponse(challenge_text)

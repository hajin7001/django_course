from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.
challenges = {
    "january": "Eat no meat for an entire month",
    "februrary": "try to exercise",
    "march": "find a clover",
    "april": "buy an umbrella",
    "may": "smell roses",
    "june": "prepare summer clothes",
    "july": "get ready for heavy rain",
    "august": "more than halfway through the year",
    "september": "you have to get to school",
    "october": "halloween",
    "november": "i am not a fan of this season",
    "december": None,
}

def index(request):
    list_items = ""
    months = list(challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months":months
    })

# challenges/month 가 들어오게 되면은 문자열이 들어왔을 때로 redirect가 된다
def monthly_challenges_number(request, month):
    months = list(challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


# challenges/month 에서 month가 string의 형태로 들어오면 해당 challenge를 명시한다
def monthly_challenges(request, month):
    try:
        challenge_text = challenges[month]
        
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name" : month
        })
    except:
        raise Http404()
    
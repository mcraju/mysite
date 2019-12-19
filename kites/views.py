from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {"name": "Sivareddy",
               "marks": 518,
               "schools": ["Shantinikethan", "Sandeepa Public High School", "Nagarjuna"],
               "Working": [{"company": "Menlo", "exp": 1.9},
                           {"company": "Fossileye", "exp": 1.2},
                           {"company": "Brisa", "exp": 0.2},
                           {"company": "teamstreamz", "exp": 2.11}]}
    return render(request, "kites/index.html", context)

def show_details(request):
    return HttpResponse("Name: {},<br>Email: {},<br>Number: {}".format(
        "vijay","varunmcvijju@gmail.com","9076543214"))
def family_details(request):
    return HttpResponse("father: {},<br>mother: {},<br>brother: {},<br>".format(
        "govindu","ramadevi","prasad"))
def college_details(request):
    return HttpResponse("collName: {},<br>Branch: {},<br>code: {}<br>,phone: {}".format(
        "kuppam engeering college","ECE","kupm","040-234567"))

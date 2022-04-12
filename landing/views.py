from urllib import response
from django.shortcuts import render

# Create your views here.

def index(req):
    context = {'name':req.user}
    return render(req, "index.html", context)
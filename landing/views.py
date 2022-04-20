from django.shortcuts import render, redirect

from account.models import UserMeta

# Create your views here.

def index(req):
    if req.user.is_authenticated:
        if(UserMeta.objects.filter(user = req.user).exists()):
            can_post = True
        else:
            can_post = False

        context = {'name':req.user, 'can_post': can_post}
        return render(req, "index.html", context)
    else:
        return redirect("account:login")
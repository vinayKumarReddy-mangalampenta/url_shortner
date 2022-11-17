
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect,HttpResponse
from shortner.models import ShortUrl
from shortner.forms import CreateUrlForm
from django.contrib import messages

import string
import secrets


def shortner(request):

    form = CreateUrlForm()
    if request.method == "POST":
        data = CreateUrlForm(request.POST)
        if data.is_valid():
            url = ''.join(secrets.choice(string.ascii_letters +
                          string.digits+"-"+"_") for x in range(7))
            res = ShortUrl.objects.create(
                short_url=url, link=request.POST.get('link'))
            res.save() 
            messages.success(request, url)

    return render(request, "main.html", {'form': form})


def redirector(request, pk):
    try:
        data = ShortUrl.objects.get(short_url=pk)
        print("data", data)
        if not data.link.startswith("http") :
            link ="https://" + data.link
            return redirect(link)
        return HttpResponseRedirect(data.link)
    except:
        return HttpResponse("Url Broken")

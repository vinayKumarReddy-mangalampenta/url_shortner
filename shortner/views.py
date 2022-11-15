
from django.shortcuts import redirect, render

from shortner.models import ShortUrl
from shortner.forms import CreateUrlForm
# Create your views here.

import string
import secrets


def shortner(request):

    form = CreateUrlForm()
    url = None
    if request.method == "POST":
        data = CreateUrlForm(request.POST)
        if data.is_valid():
            url = ''.join(secrets.choice(string.ascii_letters +
                          string.digits+"-"+"_") for x in range(7))
            res = ShortUrl.objects.create(
                short_url=url, link=request.POST.get('link'))
            res.save()

    return render(request, "main.html", {'form': form, 'url': url})


def redirector(request, pk):
    try:
        data = ShortUrl.objects.get(short_url=pk)
        print("data", data)
        return redirect(data.link)
    except:
        return redirect('shortner')

from django.shortcuts import render, get_object_or_404, redirect
from . forms import URLforms
from . models import URL

def home(request):
    if request.method == 'POST':
        form = URLforms(request.POST)
        if form.is_valid():
            url = form.save()
            return render(request, 'success.html', {'short_url': url.short_url})
    else:
        form = URLforms()
    return render(request, 'home.html', {'form':form})

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)

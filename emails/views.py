from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
# Model -> View -> Template

from .models import EmailEntry
from .forms import EmailEntryForm

html_str = "<!doctype html><html><body><h1>{email}</h1></body></html>"

def email_entry_get_view(request, id=None, *args, **kwargs):
    #get a single item stored in the database
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    #my_html = html.str.format(email=obj.email)
    #return HttpResponse(f"<h1>Hello {obj.email}</h1>")
    return render(request, "get.html", 
    {"object": obj, "email": "abc@gmail.com"})

#def email_entry_list_view():

#    return

def email_entry_create_view(request, *args, **kwargs):
    print(request.user, request.user.is_authenticated)
    form = EmailEntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EmailEntryForm()
    return render(request, "form.html", {"form": form})

#def email_entry_update_view():

#    return

#def email_entry_destroy_view():

#    return
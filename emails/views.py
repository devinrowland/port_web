from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Model -> View -> Template

def email_entry_get_view(request, *args, **kwargs):
    #get a single item stored in the database
    return HttpResponse("<h1>Hello World</h1>")

#def email_entry_list_view():

#    return

#def email_entry_create_view():

#    return

#def email_entry_update_view():

#    return

#def email_entry_destroy_view():

#    return
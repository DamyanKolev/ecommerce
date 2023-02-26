from django.template import loader
from django.http import HttpResponse

def store(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

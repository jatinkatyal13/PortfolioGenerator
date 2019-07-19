from django.shortcuts import render
from django.conf import settings
from io import StringIO, BytesIO
import json

with open(settings.PORTFOLIO_DATA, "r") as file:
  data = json.load(file)

# Create your views here.
def index(request):
  return render(request, 'main/index.html', data["main"])

def projects(request):
  return render(request, 'main/projects.html')
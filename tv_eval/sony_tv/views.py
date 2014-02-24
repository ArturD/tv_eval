from django.shortcuts import render

# Create your views here.

def run_list(req):
  return render(req, 'runs/list.html')

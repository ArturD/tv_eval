from django.shortcuts import render

from models import *

def run_list(req):
  runs = Run.objects.all()
  return render(req, 'runs/list.html', {'runs': runs})

def run_details(req, run_id):
  run = Run.objects.get(pk=int(run_id))
  results_with_value = run.result_set.filter(success=True).all()
  return render(req, 'runs/details.html', {'run':run, 'results_with_value': results_with_value})

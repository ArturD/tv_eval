from django.shortcuts import render
from django.utils import simplejson
from django.http.response import HttpResponse

from models import *

def run_list(req):
  runs = Run.objects.all()
  return render(req, 'runs/list.html', {'runs': runs})

def run_details(req, run_id):
  run = Run.objects.get(pk=int(run_id))
  results_with_value = run.result_set.filter(success=True).all()
  return render(req, 'runs/details.html', {'run':run, 'results_with_value': results_with_value})

def evaluate_result(req, result_id):
  if req.method == 'POST':
    result = Result.objects.get(pk=result_id)
    wrong_wiki = req.POST['wrong_wiki'] == 'true'
    wrong_page = req.POST['wrong_page'] == 'true'
    result.evaluate(wrong_wiki, wrong_page)

    return HttpResponse(simplejson.dumps({'ok': True, 'wrong_page': wrong_page, 'wrong_wiki': wrong_wiki}), mimetype='application/json')

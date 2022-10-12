from django.shortcuts import render,HttpResponse
from .tasks import generate
from django.views.generic.edit import FormView
from celery import current_task
from .forms import csvform
from .models import Task
from celery.result import AsyncResult

# def test(result):
#     res=AsyncResult(result).state
#     return HttpResponse(result)

class ReviewCsvForm(FormView):
    template_name='csv_home.html'
    form_class=csvform
    def form_valid(self,form):
        name=form.cleaned_data['name']
        count=form.cleaned_data['count']
        count=int(count)
        result=generate.delay(name,count)
        result_id=result.task_id
        res = AsyncResult(result_id).state
        t=Task(file_name=name,count=count,task_id=result,task_status=res)
        t.save()
        return HttpResponse(AsyncResult(result_id))

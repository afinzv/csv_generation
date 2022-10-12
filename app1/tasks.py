from __future__ import absolute_import,unicode_literals
from multiprocessing import Value
from celery import shared_task
from celery import Celery
import csv
from .models import Task
from celery.result import AsyncResult
app=Celery()


@app.task(bind=True)
def generate(self,value,count):
    rowData=[value]
    with open(f'C:/Users/HP/Desktop/project/celery_sample/sample/app1/data/{value}.csv', 'a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        for _ in range(count):
            writer.writerow(rowData)
    print(self.AsyncResult(self.request.id).state)
    return 'success'


  # path=f'C:/Users/HP/Desktop/project/celery_sample/sample/app1/data/{value}.csv'
    # f= open(path,'w',newline='')
    # writer=csv.writer(f)
    # row=value
    # for i in range(count):
    #     writer.writerow(row)
    # f.close()
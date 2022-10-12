from django.db import models

class Task(models.Model):
    file_name = models.CharField(max_length=50)
    count = models.IntegerField()
    task_id=models.CharField(max_length=200)
    task_status=models.CharField(max_length=100)
    def __str__(self):
        return self.file_name +"  "+"("+self.task_id+")"

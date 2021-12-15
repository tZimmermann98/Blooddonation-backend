from django.db import models
from backend.models.person import person
from backend.models.request import request
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
import json

class appointment(models.Model):
    #date = models.DateField()
    #time = models.TimeField()
    start = models.DateTimeField()
    #duration = models.DurationField()
    duration = models.IntegerField()
    person = models.ForeignKey(person, on_delete=models.CASCADE, blank = True, null = True)
    request = models.ForeignKey(request, on_delete=models.CASCADE, blank = True, null = True)

    def get_id(self):
        return self.id

    def get_start(self):
        return self.start

    def get_time_hour(self):
        return self.time.hour

    def get_duration(self):
        return int(self.duration)

    def save(self, *args, **kwargs):
        if self.pk is None:  # create
            self.request = request.objects.create(created = datetime.now(), status = "pending")
        super().save(*args, **kwargs)  # Call the "real" save() method.

    #def post(self, request, format = json)
    #    serializer = app



from django.db import models

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=50)
    submittedBy = models.CharField(max_length=50)
    submittedDate = models.DateField()
    fields = models.JSONField()

class BogieChecksheet(models.Model):
    formNumber = models.CharField(max_length=50)
    inspectionBy = models.CharField(max_length=50)
    inspectionDate = models.DateField()
    bogieDetails = models.JSONField()
    bogieChecksheet = models.JSONField()
    bmbcChecksheet = models.JSONField()
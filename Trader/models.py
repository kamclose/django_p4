from django.db import models

class Record(models.Model):
    stock = models.CharField(max_length=50)
    quantity = models.IntegerField()
    value = models.DecimalField(decimal_places=2, max_digits=10)

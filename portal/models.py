  
from django.db import models

# Create your models here.

class Result(models.Model):
    rollno = models.CharField(max_length=10)
    working_days = models.IntegerField()
    present_days =  models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    lessthan_85  = models.BooleanField(default = False) 
    lessthan_65 = models.BooleanField(default = False) 

    def __str__(self):
        return 'Rollno: {0} Total: {1}  Present: {2}  Percentage: {3}   '.format(self.rollno, self.price, self.present_days, self.working_days)

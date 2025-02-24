from django.db import models

# Create your models here.
class Player(models.Model):
  jno=models.IntegerField(primary_key=True)
  pname=models.CharField(max_length=100)
  runs=models.IntegerField()
  wickets=models.IntegerField()
  tname=models.CharField(max_length=50)

  def __str__(self):
    return self.pname

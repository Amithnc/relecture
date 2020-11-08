from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    organization=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,editable=False)
    subject=models.CharField(max_length=30,default='',help_text="fill the subjects in which experts need to be good at ")
    


    def __str__(self):
        return str(self.organization)+" "+self.subject
from django.db import models

class EvaluateForm(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.name

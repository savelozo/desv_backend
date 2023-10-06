from django.db import models

class EvaluateForm(models.Model):
    name = models.CharField(max_length=100, 
                            verbose_name="Name")
    last_name = models.CharField(max_length=100, 
                                 verbose_name="Last Name",)
    email = models.EmailField(verbose_name="Email")
    date_of_birth = models.DateField(null=True, 
                                     verbose_name="Date of birth",)
    nationality = models.CharField(max_length=100, 
                                   verbose_name="Nationality", 
                                   null=True)
    address = models.CharField(max_length=200, 
                               verbose_name="Address", 
                               null=True)
    education_level = models.CharField(max_length=100, 
                                       verbose_name="Education Level", 
                                       null=True)
    employment_status = models.CharField(max_length=100, 
                                         verbose_name="Employment Status", 
                                         null=True)
    industry_type = models.CharField(max_length=100, 
                                     verbose_name="Industry Type", 
                                     null=True)
    monthly_income = models.DecimalField(max_digits=10, 
                                         decimal_places=2, 
                                         verbose_name="Monthly Income",
                                         null=True)

    def __str__(self):
        return self.name + self.last_name

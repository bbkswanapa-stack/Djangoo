from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=True, blank= True, help_text="Student full name", verbose_name="Student Name")
    DOB = models.DateField()
    number = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
    class Meta:
     db_table = "student"  #To overwrite the name of table

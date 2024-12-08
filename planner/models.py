from django.db import models
from django.utils.timezone import now

class Note(models.Model):
    content = models.TextField(verbose_name="Nota del día")
    date = models.DateField(default=now, unique=True, verbose_name="Fecha")
    
    def __str__(self):
        return f"Notas del {self.date}"
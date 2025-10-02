from django.db import models

# Create your models here.
class Pacjent(models.Model):
    nazwisko = models.CharField(max_length=20)
    imie = models.CharField(max_length=20)
    miasto = models.CharField(max_length = 30, default="Białystok")
    ulica = models.CharField(max_length=20)
    wiek = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.nazwisko} {self.imie}"

class Wizyta(models.Model):
    data = models.DateTimeField("date published")
    zalecenia = models.CharField(max_length=200)
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wizyta: {self.pacjent}"
        
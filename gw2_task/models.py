from django.db import models

class Task(models.Model):
    PERIODS = [
        ('daily', 'Quotidienne'),
        ('weekly', 'Hebdomadaire'),
        ('custom', 'Objectif'),
    ]
    uid = models.CharField(max_length=100, verbose_name="ID unique")
    title = models.CharField(max_length=200, verbose_name="Intitulé")
    description = models.TextField(blank=True)
    period = models.CharField(max_length=10, choices=PERIODS, blank=True, verbose_name="Période")
    start_date = models.DateField(blank=True, null=True, verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")

    class Meta:
        verbose_name = 'tâche'
        verbose_name_plural = 'tâches'

    def __str__(self):
        return self.title
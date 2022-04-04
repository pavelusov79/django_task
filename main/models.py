from django.db import models


class Logs(models.Model):
    ip_field = models.CharField(verbose_name="IP адрес", max_length=32)
    datetime_field = models.DateTimeField(verbose_name="дата")
    status = models.PositiveSmallIntegerField(verbose_name="статус код")

    class Meta:
        verbose_name_plural = 'Logs'
        ordering = ['-datetime_field']
    


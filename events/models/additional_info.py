from django.db import models

from events.models import Event


class AdditionalInfo(models.Model):
    class Condition(models.IntegerChoices):
        FREE_PARKING = 1
        FREE_MEAL = 2
        PUBLIC_TRANSIT = 3
        FREE_WIFI = 4

    event = models.OneToOneField(Event, null=False, on_delete=models.CASCADE)
    condition = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Additional Info"

    def get_conditions(self):
        result = ""
        con_str = str(self.condition)
        for con in range(len(con_str)):
            result += self.Condition.names[int(con_str[con])].capitalize().replace("_", " ") + ", "

        return result

    def __str__(self):
        return self.get_conditions()























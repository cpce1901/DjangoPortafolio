from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=16)

    class Meta:
        verbose_name='Lugar'
        verbose_name_plural='Lugares'

    def __repr__(self) -> str:
        return f'<Place : {self.name}>'
    
    def __str__(self) -> str:
        return f'{self.name}'
    

class Sensor(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=16)

    class Meta:
        verbose_name='Sensor'
        verbose_name_plural='Sensores'

    def __repr__(self) -> str:
        return f'<Sensor : {self.name}>'
    
    def __str__(self) -> str:
        return f'{self.name}'
from django.db import models

class Veiculo(models.Model):
  nome = models.CharField(max_length=125)
  marca = models.CharField(max_length=125)
  foto = models.ImageField(upload_to='uploads/')

  def __str__(self):
    pass

  class Meta:
    db_table = 'veiculos'
    managed = True
    verbose_name = 'Veiculo'
    verbose_name_plural = 'Veiculos'
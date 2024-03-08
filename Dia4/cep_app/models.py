from django.db import models

class ViaCepModel(models.Model):
    cep = models.CharField(verbose_name="Cep do usuário", max_length=20)
    logradouro = models.CharField(verbose_name="Logradouro", max_length=100, blank=True, null=True)
    complemento = models.CharField(verbose_name="Complemento", max_length=100, blank=True, null=True)
    bairro = models.CharField(verbose_name="Bairro", max_length=100, blank=True, null=True)
    localidade = models.CharField(verbose_name="Localidade", max_length=100, blank=True, null=True)
    uf = models.CharField(verbose_name="UF", max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.cep}'

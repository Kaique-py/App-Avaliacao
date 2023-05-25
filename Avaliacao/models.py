from django.db import models
#from users.models import User
#from core.models import Anuncio

"""Vou deixar alguns campos comentados (#) apenas para rodar o servidor, tenho que apagar antes de repassar."""

class Avaliacao(models.Model):
    #Usuario que está sendo avaliado (vendedor)
    #usuario_avaliado = models.ForeignKey(User, on_delete=models.CASCADE)

    #Usuario que está avaliando (comprador)
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    nota = models.IntegerField(default=0) #Como você avalia o vendedor.
    notaNegociacao = models.IntegerField(default=5) #Como a negociação fluiu.
    notaClickAutos = models.IntegerField(default=5) #Como você avalia a ClickAutos.
    aprovada = models.BooleanField(default=False)

    #anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)
    expira_em = models.DateTimeField(blank=True)

    class Meta:
        ordering = ('usuario_avaliado',) #Aqui ordenamos as categorias em ordem alfabética.
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return self.usuario_avaliado
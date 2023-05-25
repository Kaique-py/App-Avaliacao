from rest_framework.serializers import ModelSerializer
from Avaliacao.models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'usuario_avaliado', 'usuario', 'nota', 'notaNegociacao', 'notaClickAutos', 'comentario', 'aprovada', 'criado_em', 'expira_em') 
        #Aqui eu inseri todos os campos do app, porque não sei como vai ser utilizado o arquivo JSON, mas não seria interessante inserir muitos campos pois o serializer vai ficar muito pesado e fica lento de abrir no celular ou outro dispositivo.

from rest_framework.viewsets import ModelViewSet
from Avaliacao.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Session
from .serializers import SessionSerializer


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

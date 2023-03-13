from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers, permissions


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = models.Tutorial.objects.all()
    serializer_class = serializers.TutorialSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

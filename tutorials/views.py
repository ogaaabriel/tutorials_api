from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers, permissions


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = models.Tutorial.objects.all()
    serializer_class = serializers.TutorialSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    filterset_fields = ["owner__username"]
    search_fields = ["title", "description"]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

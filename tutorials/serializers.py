from rest_framework import serializers

from . import models


class TutorialSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Tutorial
        fields = "__all__"

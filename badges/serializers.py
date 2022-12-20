from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from badges.models import Badges

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badges
        fields = ('__all__')
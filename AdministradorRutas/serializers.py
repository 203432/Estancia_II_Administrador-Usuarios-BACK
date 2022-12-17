from rest_framework import routers, serializers, viewsets
# Importación de modelos
from AdministradorRutas.models import Rutas
class rutasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = ['id', 'shortname', 'fullname', 'services', 'schedule', 'importantPlaces', 'validate', 'score']
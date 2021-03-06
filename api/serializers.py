from rest_framework import serializers
from .models import Pomo

class PomoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Pomo
        fields = ('id', 'name', 'observation', 'start', 'end', 'owner')
from rest_framework import serializers
from .models import livre, emprunt, user

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class livreSerializer(serializers.ModelSerializer):
    class Meta:
        model = livre
        fields = '__all__'

class empruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = emprunt
        fields = '__all__'
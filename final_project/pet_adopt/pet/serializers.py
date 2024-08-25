from rest_framework import serializers
from .models import Pet,PetType

class PetSerializer(serializers.ModelSerializer):
    pet_type = serializers.StringRelatedField(many=False)
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = Pet
        fields = ['id','author','name','description','image','adoption_status','gender','pet_type','age','price',]
        read_only_fields = ['author','id','created_on',]

class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'
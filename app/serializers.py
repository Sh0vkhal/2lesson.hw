from rest_framework import  serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from .models import Car,Football,Ufc

class CarSerializer(serializers.Serializer):
     model = serializers.CharField(max_length=50)


     def create(self,validated_data):
          return Car.objects.create(**validated_data)
     

     def update(self, instance, validated_data):
          instance.model = validated_data.get('model', instance.model)
          instance.save()
          return instance
     
     def delete(self, instance):
          instance.delete()
          return True
     



class FootballSerializer(serializers.ModelSerializer):
     name = serializers.CharField(max_length=30)
     team = serializers.CharField()


     def create(self,validated_data):
          return Football.objects.create(**validated_data)
     

     def update(self, instance, validated_data):
          instance.name = validated_data.get('name', instance.name)
          instance.team = validated_data.get('team', instance.team)
          instance.save()
          return instance
     

     def delete(self, instance):
          instance.delete()
          return True
     



class UfcSerializer(serializers.ModelSerializer):
    fighter = serializers.CharField(max_length=50)
   

    def create(self, validated_data):
         return Ufc.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
         instance.fighter = validated_data.get('fighter', instance.fighter)
         instance.save()
         return instance
    

    def delete(self, instance):
         instance.delete()
         return True

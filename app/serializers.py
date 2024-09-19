from rest_framework import  serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

class Car:
    def __init__(self, model):
        self.model = model

car = Car({"model":"BWM"})

class CarSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=30)
    

def convert_to_json():
    serializer = CarSerializer(car)
    print(serializer.data)
    
    json = JSONRenderer().render(serializer.data)
    print(json)

def json_to_python():
    json = b'{"model":"BWM"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)



class Football:
    def __init__(self, name):
        self.name = name
      

football = Football({"name":"Ronaldo"}) 



class FootballSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
   

def convert_to_json_2():
    serializer = CarSerializer(football)
    print(serializer.data)
    
    json = JSONRenderer().render(serializer.data)
    print(json)

def json_to_python_2():
    json = b'{"name":"Cristiano"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)


class Ufc:
  def __init__(self, fighter):
      self.fighter = fighter


  class UfcSerializer(serializers.Serializer):
      fighter = serializers.CharField(max_length=50)    


ufc = Ufc({"fighter":"Islam Makhachev"})      
   

def convert_to_json_3():
    serializer = CarSerializer(ufc)
    print(serializer.data)
    
    json = JSONRenderer().render(serializer.data)
    print(json)


def json_to_python_2():
    json = b'{"fighter":"Islam Makhachev"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
    
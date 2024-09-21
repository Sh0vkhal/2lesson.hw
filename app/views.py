from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Car, Football, Ufc
from .serializers import CarSerializer,FootballSerializer, UfcSerializer

class CarAPI(APIView):
    def get(self, request: Request) -> Response:
         car = Car.objects.all()
         return Response(CarSerializer(car,many=True).data)
    
    def post(self, request: Request) -> Response:
        serializer = CarSerializer (data=request. data)
        serializer.is_valid(raise_exception=True)
        car = serializer.save()
        return Response (CarSerializer (car).data)
    
    def put(self, request: Request,pk):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request: Request, pk):
        car = Car.objects.get(pk=pk)
        car.delete()
        return Response(status=204)


    

class FootballAPI(APIView):
   def get(self, request: Request) -> Response:
         football = Football.objects.all()
         return Response(CarSerializer(football,many=True).data)
    
   def post(self, request: Request) -> Response:
        serializer = FootballSerializer (data=request. data)
        serializer.is_valid(raise_exception=True)
        football = serializer.save()
        return Response (CarSerializer (football).data)
    
   def put(self, request: Request,pk):
        football = Football.objects.get(pk=pk)
        serializer = FootballSerializer(football, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
   def delete(self, request: Request, pk):
        football = Football.objects.get(pk=pk)
        football.delete()
        return Response(status=204)
   



class UfcAPI(APIView):
   def get(self, request: Request) -> Response:
         ufc = Ufc.objects.all()
         return Response(UfcSerializer(ufc,many=True).data)
    
   def post(self, request: Request) -> Response:
        serializer = UfcSerializer (data=request. data)
        serializer.is_valid(raise_exception=True)
        ufc = serializer.save()
        return Response (UfcSerializer (ufc).data)
    
   def put(self, request: Request,pk):
        ufc = Ufc.objects.get(pk=pk)
        serializer = UfcSerializer(ufc, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
   def delete(self, request: Request, pk):
        ufc = Ufc.objects.get(pk=pk)
        ufc.delete()
        return Response(status=204)
   
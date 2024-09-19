from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Car, Football, Ufc

class CarAPI(APIView):
    def get(self, request: Request) -> Response:
        car = Car.objects.all()
        a = []
        for i in car:
            a.append({ "model": i.model, "price": i.price})
        return Response(a)
    

class FootballAPI(APIView):
    def get(self, request: Request) -> Response:
        football = Football.objects.all()
        b = []
        for i in football:
            b.append({ "name": i.name, "team": i.team})
        return Response(b)
    

class UfcAPI(APIView):
    def get(self, request: Request) -> Response:   
        ufc = Ufc.objects.all()
        c = []
        for i in ufc:
            c.append({ "fighter": i.fighter, "rating": i.rating})
        return Response(c)
    
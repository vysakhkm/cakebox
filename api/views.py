from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,GenericViewSet,ModelViewSet
from django.contrib.auth.models import User
from api.serializers import Usercreate,CakeSerializer,CartSerializer,OrderSerializer,ReviewSerializer
from rest_framework import authentication,permissions
from cake.models import Cakes,Carts,Reviews
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.decorators import action

# Create your views here.
class Createuserviw(ViewSet):

    def create(self,request,*args,**kwargs):
        serializer=Usercreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class Cakelistview(GenericViewSet,RetrieveModelMixin,ListModelMixin):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    serializer_class=CakeSerializer
    queryset=Cakes.objects.all()
    # def list(self,request,*args,**kwargs):
    #     qs=Cakes.objects.all()
    #     serializer=CakeSerializer(qs,many=True)
    #     return Response(serializer.data)
    # def retrieve(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Cakes.objects.get(id=id)
    #     serializer=CakeSerializer(qs,many=False)
    #     return Response(serializer.data)
    
    def get_queryset(self):
        qs=Cakes.objects.all()

        if "layers" in self.request.query_params:
            lay=self.request.query_params.get("layers")
            qs=qs.filter(layers=lay)
       
        
        if "shape" in self.request.query_params:
            sh=self.request.query_params.get("shape")
            qs=qs.filter(shape=sh)

        return qs

    @action(methods=["post"],detail=True)
    def addto_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=Cakes.objects.get(id=id)
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            # qs=Carts.objects.create(cake=cake,user=request.user,quantity=serializer.validated_data.get("qty"))
            # serializer=CartSerializer(qs)
            serializer.save(cake=cake,user=request.user)
            return Response(data=serializer.data)
        else:
    
            return Response(data=serializer.errors)
    
    @action(methods=["post"],detail=True)
    def make_order(self,request,*args,**kwargs):
        cake=self.get_object()
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cake=cake,user=request.user)
            # qs=Order.objects.create(cake=cake,
            #                         user=request.user,
            #                         address=serializer.validated_data.get("address"),
            #                         matter=serializer.validated_data.get("matter"),

            #                         )
            # serializer=OrderSerializer(qs)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    @action(methods=["post"],detail=True)
    def add_review(self,reuest,*args,**kwargs):
        id=kwargs.get("pk")
        cak=Cakes.objects.get(id=id)
        serializer=ReviewSerializer(data=reuest.data)
        if serializer.is_valid():
            serializer.save(cake=cak,user=reuest.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class Cartlistview(GenericViewSet,ListModelMixin):
    serializer_class=CartSerializer
    queryset=Carts.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)
    

class Reviewlistview(GenericViewSet,ListModelMixin):
    serializer_class=ReviewSerializer
    queryset=Reviews.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Reviews.objects.filter(user=self.request.user)
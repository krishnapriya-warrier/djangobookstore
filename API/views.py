from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet

from API.models import Books
from API.serializers import BooksSerializer,BooksModelSerializer,UserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import action
# class BooksView(APIView):
#     def get(self,request,*args,**kw):
#         qs=Books.objects.all()
#         serializer = BooksSerializer(qs,many=True)
#         return Response(data=serializer.data)
#     def post(self,request,*args,**kw):
#         serializer = BooksSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             Books.objects.create(**serializer.validated_data)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
# class BooksViewSetView(ViewSet):
#     def list(self,request,*args,**kw):
#         qs = Books.objects.all()
#         serializer = BooksModelSerializer(qs,many=True)
#         return Response(data=serializer.data)
    
#     def create(self,request,*args,**kw):
#         serializer = BooksModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
# class BooksDetailView(APIView):
#     def get(self,request,*args,**kw):
#         print(kw)
#         id = kw.get('id')
#         qs = Books.objects.get(id=id)
#         serializer = BooksSerializer(qs)
#         return Response(data=serializer.data)
#     def put(self,request,*args,**kw):
#         serializer = BooksSerializer(data=request.data)
#         if serializer.is_valid():
#             id = kw.get('id')
#             qs = Books.objects.filter(id=id).update(**request.data)
#             print(serializer.validated_data)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#     def delete(self,request,*args,**kw):
#         id = kw.get('id')
#         qs = Books.objects.filter(id=id).delete()
#         return Response(data='item successfully deleted')
    
# class BooksDetailViewSetView(ViewSet):
#     def retrieve(self,request,*args,**kw):
#         id = kw.get('pk')
#         qs = Books.objects.get(id=id)
#         serializer=BooksModelSerializer(qs)
#         return Response(data=serializer.data)
#     def destroy(self,request,*args,**kw):
#         id = kw.get('pk')
#         qs = Books.objects.filter(id=id).delete()
#         return Response(data="item deleted")
#     def update(self,request,*args,**kw):
#          id = kw.get('pk')
#          obj = Books.objects.get(id=id)
#          serializer = BooksModelSerializer(data=request.data,instance=obj)
#          if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#          else:
#             return Response(data=serializer.errors)
         
# class UserView(ViewSet):
#     def create(self,request,*args,**kw):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)

class BooksViewSetView(ModelViewSet):
    
    serializer_class = BooksModelSerializer
    queryset = Books.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=["GET"],detail=False)
    def categories(self,request,*args,**kw):
        qs = Books.objects.values_list('category',flat=True).distinct()
        return Response(data=qs)
    
    @action(methods=["POST"],detail=True)
    def add_to_cart(self,request,*args,**kw):
        id = kw.get('pk')

        user = request.user
        item = Books.objects.get(id=id)

        user.carts_set.create(product=item)
        return Response(data="item successfully added to cart")


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CartView(APIView):

    def post(self,request,*args,**kw):
        id = kw.get('pk')

        user = request.user
        item = Books.objects.get(id=id)

        user.carts_set.create(Book=item)
        return Response(data="item successfully added to cart")






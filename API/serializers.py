from rest_framework import serializers
from API.models import Books,Carts,Review
from django.contrib.auth.models import User

class BooksSerializer(serializers.Serializer):

    Book_name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()

class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:

        model = Books
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ["first_name","last_name","email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)
    
class CartSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only = True)
    user = serializers.CharField(read_only = True)
    Book = serializers.CharField(read_only = True)
    date = serializers.CharField(read_only = True)
    class Meta:

        model = Carts
        fields = "__all__"

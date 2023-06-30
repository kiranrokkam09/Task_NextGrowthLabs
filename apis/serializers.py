from rest_framework import serializers
from .models import User, Profile,App
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('username','email','password')
        def create(self, validated_data):
            user = User.objects.create(
                username = validated_data["username"]
            )
            user.set_password(validated_data["password"])
            user.save()
            return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = Profile
        fields = '__all__'


class AdminAppSerializer(serializers.ModelSerializer):
    class Meta :
        model = App
        fields = ('id','name','points')


class UserAppSerializer(serializers.ModelSerializer):
    class Meta :
        model = App
        fields = ('file',)


class CreateAppSerializer(serializers.ModelSerializer):
    class Meta :
        model = App
        fields = '__all__'

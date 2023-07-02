from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer,ProfileSerializer,AdminAppSerializer, UserAppSerializer,CreateAppSerializer
from rest_framework import generics
from .models import User
from django.contrib.auth import authenticate,logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import App
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from .models import Profile
from rest_framework.authtoken.models import Token
# Create your views here.


def index(request):
    print(request.headers)
    return HttpResponse("Hello API !!")

# Register a new user
@permission_classes((AllowAny,))
class register(generics.CreateAPIView):
    serializer_class = UserSerializer

# login user
@permission_classes((AllowAny,))
class login(APIView):
    def post(self, request):
        if not request.data:   #validation
            return Response({
                "ERROR": "Please provide a username and password"
            },status = status.HTTP_400_BAD_REQUEST)
        username = request.data['username']
        password = request.data['password']
        if username is None or password is None:    #validation
            return Response({
                "ERROR": "Required fields are not provided"
            }, status = status.HTTP_400_BAD_REQUEST)
        user = authenticate(username = username, password = password)
        token,_ = Token.objects.get_or_create(user= user)
        return Response({
            "Messege" : "Succesfullly logged in",
            "Token": token.key
        }, status = status.HTTP_200_OK)

@permission_classes((AllowAny, ))
@api_view(["GET"])
def logout_view(request):
    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')

'''admin creates a task without file '''
@permission_classes((IsAdminUser,))
class app(generics.CreateAPIView):
    serializer_class = AdminAppSerializer
    queryset = App.objects.all()
    serializer = AdminAppSerializer
    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

'''lists all tasks posted by admin'''
@permission_classes((AllowAny,))
class listapp(generics.ListAPIView):
    serializer_class = AdminAppSerializer
    queryset = App.objects.filter(user__is_staff = True)

'''retrives app by id, this method is used for single task full display'''
@permission_classes((IsAuthenticated,))
class getapp(generics.RetrieveAPIView):
    serializer_class = UserAppSerializer
    queryset = App.objects.all()

'''create a new post'''
@permission_classes((IsAuthenticated, ))
class saveapp(generics.CreateAPIView):
    serializer_class = CreateAppSerializer

@permission_classes((IsAuthenticated,))
class profile(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
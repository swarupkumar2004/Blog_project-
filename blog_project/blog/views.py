from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, PostSerializer
from .models import Post
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

# User Signup
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user=user)
            return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff
    
class PostPagination(PageNumberPagination):
    page_size = 5

# Create and List Posts
class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    pagination_class = PostPagination
    filter_backends = [SearchFilter]
    search_fields = ['title','content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Retrieve, Update, Delete a Post
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrAdmin]
    authentication_classes = [TokenAuthentication]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("You can only update your own post.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("You can only delete your own post.")
        instance.delete()


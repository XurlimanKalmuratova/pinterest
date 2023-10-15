from rest_framework.decorators import api_view,permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from .permission import UserDetailPermission, UserPermission, PostDetailPermission, PostPermission, CategoryDetailPermission, CategoryPermission

from app.models import CustomUser
from .serializer import UserSerializer

@api_view(['GET', 'POST'])
@permission_classes([UserPermission])
def user(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = UserSerializer(users, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([UserDetailPermission])
def user_detail(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete() 
        return Response(status=HTTP_204_NO_CONTENT)



from app.models import Post
from .serializer import PostSerializer

@api_view(['GET', 'POST'])
@permission_classes([PostPermission])
def post(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PostSerializer(posts, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([PostDetailPermission])
def post_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete() 
        return Response (status=HTTP_204_NO_CONTENT)
    

from app.models import Category
from .serializer import CategorySerializer

@api_view(['GET', 'POST'])
@permission_classes([CategoryPermission])
def category(request):
    category = Category.objects.all()
    if request.method == 'GET':
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CategoryDetailPermission])
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CategorySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete() 
        return Response(status=HTTP_204_NO_CONTENT)


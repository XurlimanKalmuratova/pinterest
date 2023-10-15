from django.urls import path, include
from .views import user, category, post,  user_detail, post_detail, category_detail

urlpatterns = [
    path('user/', user),
    path('user/<int:pk>', user_detail),
    path('post/', post),
    path('post/<int:pk>/', post_detail),
    path('category/', category),
    path('category/<int:pk>', category_detail),

    path('auth/', include('dj_rest_auth.urls'))
]

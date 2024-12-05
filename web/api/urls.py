from django.urls import path
from api import views
from .views import (        
    GameListCreate, GameDetailUpdateDelete, GameSearch,
    UserModelListCreate, UserModelDetailUpdateDelete, UserModelSearch
)
app_name = 'api'

urlpatterns = [        
    path('api/games', GameListCreate.as_view()),  
    path('api/game/<int:pk>', GameDetailUpdateDelete.as_view()),  
    path('api/game/search/', GameSearch.as_view()),  
    path('api/users', UserModelListCreate.as_view()),  
    path('api/user/<int:pk>', UserModelDetailUpdateDelete.as_view()),  
    path('api/user/search/', UserModelSearch.as_view()),  
]


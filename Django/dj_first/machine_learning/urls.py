from django.urls import path
from . import views


urlpatterns = [ 
    path('ml/',views.mlearning),
    path('ml/',views.Dlearning)
]
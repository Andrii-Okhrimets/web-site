from django.urls import path

from . import views

urlpatterns = [
    path('', views.MoviesVies.as_view()),
    path('<slug:slug>/', views.MoviesDetaliVies.as_view(), name='moviesingle'),
    path('review/<int:pk>/', views.AddReviews.as_view(), name='addreview'),
]

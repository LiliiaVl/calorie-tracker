from django.urls import include, path
from myapp import views
from myapp.views import IndexView

urlpatterns =[
     path('', views.IndexView.as_view(), name="index"),
    path('delete/<int:id>/', views.DeleteView.as_view(), name="delete"),
]

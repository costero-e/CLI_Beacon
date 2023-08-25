from django.urls import path
#from .views import HomePageView
from . import views
app_name = 'bash'

urlpatterns = [
    path('', views.bash_view, name='index'),
    path('true',views.bash_true_view, name='true'),
    path('false',views.bash_false_view, name='false'),
]
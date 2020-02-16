from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import', views.import_jobs, name='import'),
    path('update', views.update, name='update'),
]

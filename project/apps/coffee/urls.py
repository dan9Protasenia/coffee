from django.urls import path

from . import views

urlpatterns = [
    path('', views.coffee, name='coffee'),
    path('create', views.Create.as_view(), name='create'),
    path('<int:pk>', views.Info.as_view(), name='info'),
    path('<int:pk>/update', views.Update.as_view(), name='update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete')
]

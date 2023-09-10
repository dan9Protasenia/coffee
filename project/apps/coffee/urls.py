from django.urls import path

import project.apps.about.views
from . import views

app_name = 'coffee'

urlpatterns = [
    path('', views.coffee, name='coffee'),
    path('create', views.Create.as_view(), name='create'),
    path('<int:pk>', views.Info.as_view(), name='info'),
    path('<int:pk>/update', views.Update.as_view(), name='update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete'),
    path('about', project.apps.about.views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<int:pk>/add_feedback/', views.CreateFeedback.as_view(), name='add_feedback')


]

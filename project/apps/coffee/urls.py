import django.views.generic
from django.urls import path
from django.views.decorators.cache import cache_page
import project.apps.about.views
from . import views
from .views import *
app_name = 'coffee'

urlpatterns = [
    path('', cache_page(60)(CoffeeList.as_view()), name='coffee'),
    path('create', Create.as_view(), name='create'),
    path('<int:pk>', Info.as_view(), name='info'),
    path('<int:pk>/update', Update.as_view(), name='update'),
    path('<int:pk>/delete', Delete.as_view(), name='delete'),
    path('about', project.apps.about.views.about, name='about'),
    path('contact', contact, name='contact'),
    path('<int:pk>/add_feedback/', CreateFeedback.as_view(), name='add_feedback'),
    path('registration/', SignUp.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),


]

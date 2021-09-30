from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailView

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')), 
    path('', CreateView.as_view(), name="create"),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('get-token/', obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)
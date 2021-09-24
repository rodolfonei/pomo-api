from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailView

urlpatterns = [
    path('', CreateView.as_view(), name="create"),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')), 
]

urlpatterns = format_suffix_patterns(urlpatterns)
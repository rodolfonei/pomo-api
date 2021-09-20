from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailView

urlpatterns = [
    path('', CreateView.as_view(), name="create"),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
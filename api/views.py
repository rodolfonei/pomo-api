from rest_framework import generics
from .serializers import PomoSerializer
from .models import Pomo

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Pomo.objects.all()
    serializer_class = PomoSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new pomo."""
        serializer.save()

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Pomo.objects.all()
    serializer_class = PomoSerializer
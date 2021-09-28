from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import PomoSerializer
from .models import Pomo

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Pomo.objects.all()
    serializer_class = PomoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new pomo."""
        serializer.save(owner=self.request.user)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Pomo.objects.all()
    serializer_class = PomoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
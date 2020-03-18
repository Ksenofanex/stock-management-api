from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import RawMaterial
from .serializers import MaterialSerializer


class MaterialList(generics.ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = MaterialSerializer


class MaterialDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RawMaterial.objects.all()
    serializer_class = MaterialSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.blog.serializers import AurthorSerializer
from apps.blog.models import AuthorModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class AurthorListApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AuthorModel.objects.filter(is_active=True)
    serializer_class = AurthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ["display_name"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AurthorUpdateApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AuthorModel.objects.filter(is_active=True)
    serializer_class = AurthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ["display_name"]

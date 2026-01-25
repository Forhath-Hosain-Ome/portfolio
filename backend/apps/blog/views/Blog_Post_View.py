from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.blog.serializers import BlogPostSerializer
from apps.blog.models import BlogPostModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class BlogPostListApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPostModel.objects.filter(is_active=True)
    serializer_class = BlogPostSerializer
    filter_backends = [SearchFilter]
    search_fields = ["author__user"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostUpdateApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPostModel.objects.filter(is_active=True)
    serializer_class = BlogPostSerializer

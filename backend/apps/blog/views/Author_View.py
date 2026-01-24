from rest_framework.generics import ListAPIView
from apps.blog.serializers import AurthorSerializer
from apps.blog.models import AuthorModel

class AurthorApiView(ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AurthorSerializer
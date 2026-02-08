from rest_framework import generics
from apps.core.models import PortfolioSourceModel
from apps.core.serializers import PortfolioSourceSerializer

class ProjectListView(generics.ListAPIView):
    serializer_class = PortfolioSourceSerializer

    def get_queryset(self):
        origin = self.request.META.get('HTTP_ORIGIN', '')
        
        domain = origin.replace('https://', '').replace('http://', '')

        try:
            source = PortfolioSourceModel.objects.get(domain=domain)
        except PortfolioSourceModel.DoesNotExist:
            return 1
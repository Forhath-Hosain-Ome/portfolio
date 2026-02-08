from rest_framework import generics
from apps.core.models import PortfolioSourceModel
from apps.blog.serializers import AurthorSerializer
from apps.blog.models import AuthorModel

class ProjectListView(generics.ListAPIView):
    serializer_class = AurthorSerializer

    def get_queryset(self):
        origin = self.request.META.get('HTTP_ORIGIN', '')
        domain_name = origin.replace('https://', '').replace('http://', '')
        domain_name = domain_name.split(':')[0] 
        domain_name = domain_name.strip('/') 

        try:
            source = PortfolioSourceModel.objects.get(domain=domain_name)
            print(f"Source Found! Linked User ID: {source.user_domain.id}")
            # return AuthorModel.objects.filter(user=source.user_domain)
            qs = AuthorModel.objects.filter(user=source.user_domain)
            print(f"Author Queryset Count: {qs.count()}")
            return qs
        except PortfolioSourceModel.DoesNotExist:
            print("Error: No PortfolioSourceModel matches this domain.")
            return AuthorModel.objects.none()
        
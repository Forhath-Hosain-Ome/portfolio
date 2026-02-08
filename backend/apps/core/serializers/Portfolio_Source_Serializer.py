from rest_framework import serializers
from apps.blog.models import AuthorModel

class PortfolioSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel

        fields = (
            "domain",
            "user_domain",
        )

        read_only_fields = (
            "id",
        )
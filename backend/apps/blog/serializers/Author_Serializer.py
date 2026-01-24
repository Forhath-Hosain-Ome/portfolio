from rest_framework import serializers
from apps.blog.models import AuthorModel

class AurthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel

        fields = (
            "id",
            "user",
            "display_name",
            "bio",
            "avatar",
            "website",
            "twitter",
            "linkedin",
            "github",
        )

        read_only_fields = (
            "id",
        )
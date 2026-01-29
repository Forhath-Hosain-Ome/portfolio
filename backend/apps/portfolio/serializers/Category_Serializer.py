from rest_framework import serializers
from apps.portfolio.models import CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel

        fields = (
            "id",
            "name",
            "slug",
            "type",
            "description",
            "parent",
        )

        read_only_fields = (
            "id",
        )
from rest_framework import serializers
from apps.blog.models import BlogPostModel

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel

        fields = (
            "BlogPostModel",
            "slug",
            "author",
            "featured_image",
            "excerpt",
            "content",
            "content_extended",
            "read_time_minutes",
            "views_count",
            "likes_count",
            "comments_count",
            "is_featured",
            "categories",
            "tags",
            "is_featured",
        )

        read_only_fields = (
            "id",
        )
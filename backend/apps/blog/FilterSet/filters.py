# import django_filters
# from .models import BlogPostModel


# class BlogPostFilter(django_filters.FilterSet):
#     author = django_filters.NumberFilter(field_name="author__id")
#     is_active = django_filters.BooleanFilter()
#     created_after = django_filters.DateFilter(
#         field_name="created_at", lookup_expr="gte"
#     )

#     class Meta:
#         model = BlogPostModel
#         fields = ["author", "is_active"]

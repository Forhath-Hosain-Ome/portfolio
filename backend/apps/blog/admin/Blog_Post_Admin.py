from django.contrib import admin
from apps.blog.models import BlogPostModel

@admin.register(BlogPostModel)
class BlogPostAdmin(admin.ModelAdmin):
    list_filter = (
        "is_active",
        "created_at",
        "updated_at",
    )

    list_editable = ("is_active",)

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_display = (
        "title",
        "slug",
        "featured_image",
        "thumbnail",
        "excerpt",
        "content",
        "content_extended",
        "read_time_minutes",
        "views_count",
        "likes_count",
        "comments_count",
        "is_featured",
        "is_active"
    )

    list_display_links = ("title", "slug", "is_featured")

    search_fields = (
        "title",
        "categories",
        "tags",
    )

    search_help_text = "Search by title, category or tag"

    fieldsets = (
        ("Blog Information", {
            "fields": ("title", "slug", "author",),
        }),
        ("Media", {
            "fields": ("featured_image", "thumbnail",),
        }),
        ("Content", {
            "fields": ("excerpt", "content", "content_extended",),
        }),
        ("Utility Data", {
            "fields": ("read_time_minutes", "views_count", "likes_count", "comments_count",),
        }),
        ("Status", {
            "fields": ("is_active",),
        }),
        ("System Information", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    save_on_top = True
    preserve_filters = True

    actions = ["make_active", "make_inactive"]

    @admin.action(description="Mark selected authors as Active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected authors as Inactive")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    def has_delete_permission(self, request, obj=None):
        # Example: prevent delete for non-superusers
        if not request.user.is_superuser:
            return False
        return True

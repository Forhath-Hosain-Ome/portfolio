from django.contrib import admin
from apps.services.models import ServiceModel

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "icon_name",
        "short_description",
        "full_description",
        "bg_color",
        "text_color",
        "is_featured",
        "is_active",
    )

    list_display_links = ("title",)

    list_filter = (
        "title",
        "slug",
        "is_featured",
        "is_active",
    )

    list_editable = ("is_active", "is_featured",)

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    search_fields = (
        "title",
        "slug",
    )

    search_help_text = "Search by title, slug"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Service Information", {
            "fields": ("title", "slug", "short_description", "full_description"),
        }),
        ("Style", {
            "fields": ("icon_name", "bg_color", "text_color", "is_featured"),
        }),
        ("Status", {
            "fields": ("is_active",),
        }),
        ("System Information", {
            "fields": ("created_at", "updated_at"),
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

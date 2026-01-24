from django.contrib import admin
from apps.testimonials.models import TestimonialModel
@admin.register(TestimonialModel)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "client_name",
        "client_position",
        "client_company",
        "client_image",
        "testimonial_text",
        "rating",
        "is_featured",
        "is_active",
        "related_project"
    )

    list_display_links = ("client_company",)

    list_filter = (
        "rating",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_editable = ("is_active",)

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    search_fields = (
        "client_name",
        "client_position",
        "client_company",
        "client_image",
    )

    search_help_text = "Search by client name"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Author Information", {
            "fields": ("client_name", "client_position", "client_company", "client_image"),
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

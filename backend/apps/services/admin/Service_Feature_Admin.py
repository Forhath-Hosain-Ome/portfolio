from django.contrib import admin
from apps.services.models import ServiceFeatureModel

@admin.register(ServiceFeatureModel)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = (
        "feature_text",
        "service",
    )

    list_display_links = ("feature_text",)

    list_filter = (
        "feature_text",
    )

    list_editable = ("service",)

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-feature_text",)

    search_fields = (
        "feature_text",
    )

    search_help_text = "Search by degree, institute"

    # readonly_fields = (
    #     "created_at",
    #     "updated_at",
    # )

    fieldsets = (
        ("Service Information", {
            "fields": ("feature_text", 'service'),
        }),
        # ("Degree Info", {
        #     "fields": ("degree_title", "start_date", "end_date", "is_current", "gpa", "description"),
        # }),
        # ("Status", {
        #     "fields": ("is_active",),
        # }),
        # ("System Information", {
        #     "fields": ("created_at", "updated_at"),
        # }),
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

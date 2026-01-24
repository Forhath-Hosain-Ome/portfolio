from django.contrib import admin
from apps.site_config.models import PartnerModel

@admin.register(PartnerModel)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "partner_name",
        "logo_default",
        "logo_hover",
        "website_url",
        "is_active"
    )

    list_display_links = ("partner_name",)

    list_filter = (
        "is_active",
        "partner_name",
    )


    list_editable = ("is_active", )

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    search_fields = (
        "partner_name",
        "website_url",
        "is_active"
    )

    search_help_text = "Search by title, slug"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Partner Information", {
            "fields": ("partner_name", "logo_default", "logo_hover", "website_url"),
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

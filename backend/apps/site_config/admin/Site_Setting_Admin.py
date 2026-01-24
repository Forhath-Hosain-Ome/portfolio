from django.contrib import admin
from apps.site_config.models import SiteSettingModel

@admin.register(SiteSettingModel)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = (
        "setting_key",
        "setting_value",
        "setting_type",
        "setting_group",
        "description",
        "is_active",
    )

    list_display_links = ("setting_type",)

    list_filter = (
        "setting_type",
        "setting_group",
    )

    list_editable = ("is_active", )

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    search_fields = (
        "setting_key",
    )

    search_help_text = "Search by title, slug"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Site Information", {
            "fields": ("setting_key", "setting_value", "setting_type", "setting_group"),
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

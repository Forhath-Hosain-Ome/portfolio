from django.contrib import admin
from apps.core.models import PortfolioSourceModel

@admin.register(PortfolioSourceModel)
class PortfolioSourceAdmin(admin.ModelAdmin):
    list_display = (
        "domain",
        "user_domain",
        "is_active",
    )

    list_display_links = ("user_domain",)

    list_filter = (
        "domain",
    )

    list_editable = ("is_active",)

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-user_domain",)

    search_fields = (
        "domain",
    )

    search_help_text = "Search by user name"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Domain Information", {
            "fields": ("domain",),
        }),
        ("User Information", {
            "fields": ("user_domain",),
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

from django.contrib import admin
from apps.portfolio.models import PortfolioImageModel
# Register your models here.

@admin.register(PortfolioImageModel)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = (
        "portfolio_item",
        "image",
        "caption",
        "is_primary",
        "is_active",
    )

    list_display_links = ("portfolio_item",)

    list_filter = (
        "portfolio_item",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_editable = ("is_active",)

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    search_fields = (
        "portfolio_item",
    )

    search_help_text = "Search by user name"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Catagory Information", {
            "fields": ("portfolio_item",),
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

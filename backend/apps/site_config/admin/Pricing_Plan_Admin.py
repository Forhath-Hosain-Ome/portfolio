from django.contrib import admin
from apps.site_config.models import PricingPlanModel

@admin.register(PricingPlanModel)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = (
        "plan_name",
        "price",
        "currency",
        "billing_period",
        "description",
        "is_featured",
        "is_active",
        "bg_color",
        "text_color",
    )

    list_display_links = ("plan_name",)

    list_filter = (
        "plan_name",
        "price",
        "currency",
        "is_featured",
        "is_active",
    )


    list_editable = ("is_active", )

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    search_fields = (
        "plan_name",
        "price",
        "currency",
    )

    search_help_text = "Search by title, slug"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Pricing Information", {
            "fields": ("plan_name", "description", "is_featured"),
        }),
        ("Billing Information", {
            "fields": ("price", "currency", "billing_period"),
        }),
        ("Style", {
            "fields": ("bg_color", "text_color"),
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

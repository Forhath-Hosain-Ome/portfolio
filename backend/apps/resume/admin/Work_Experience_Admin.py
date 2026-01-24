from django.contrib import admin
from apps.resume.models import WorkExperienceModel

@admin.register(WorkExperienceModel)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "job_title",
        "company_name",
        "location",
        "start_date",
        "end_date",
        "is_current",
        "description",
        "company_logo",
        "company_website",
        "is_active",
    )

    list_display_links = ("job_title",)

    list_filter = (
        "job_title",
        "company_name",
        "start_date",
        "end_date",
        "is_current",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_editable = ("is_active",)

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    search_fields = (
        "job_title",
        "company_name",
    )

    search_help_text = "Search by job title, company name"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Job Information", {
            "fields": ("job_title", "description"),
        }),
        ("Company Information", {
            "fields": ("company_name", "location", "company_logo", "company_website"),
        }),
        ("Job duration", {
            "fields": ("start_date", "end_date", "is_current"),
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

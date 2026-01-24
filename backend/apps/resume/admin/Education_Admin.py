from django.contrib import admin
from apps.resume.models import EducationModel

@admin.register(EducationModel)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree_title",
        "institution",
        "location",
        "start_date",
        "end_date",
        "is_current",
        "description",
        "gpa",
        "institution_logo",
        "is_active"
    )

    list_display_links = ("institution",)

    list_filter = (
        "degree_title",
        "institution",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_editable = ("is_active",)

    list_per_page = 25
    list_max_show_all = 200

    ordering = ("-created_at",)

    search_fields = (
        "degree_title",
        "institution",
    )

    search_help_text = "Search by degree, institute"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Institute Information", {
            "fields": ("institution", "location", "institution_logo"),
        }),
        ("Degree Info", {
            "fields": ("degree_title", "start_date", "end_date", "is_current", "gpa", "description"),
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

from django.contrib import admin
from .models import SiteSetting, Service, Project, Property, Testimonial, ContactMessage, QuoteRequest

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("company_name", "phone", "email")
    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_editable = ("is_active", "order")
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "featured", "completion_year")
    list_filter = ("category", "featured")
    search_fields = ("title", "location")
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "property_type", "status", "price", "location", "available", "featured")
    list_filter = ("property_type", "status", "available", "featured")
    search_fields = ("title", "location")
    prepopulated_fields = {"slug": ("title",)}
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "rating", "is_active")
    list_editable = ("is_active",)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    readonly_fields = ("name", "email", "phone", "subject", "message", "created_at")
@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "project_type", "phone", "created_at")
    readonly_fields = ("name", "email", "phone", "project_type", "location", "budget", "details", "created_at")

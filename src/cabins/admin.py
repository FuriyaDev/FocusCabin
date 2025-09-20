from django.contrib import admin
from .models import (
    CabineClass,
    Cabine,
    CabineMedia,
    CabineAmenity,
    CabineBooking,
)

# Inline для медиа (чтобы удобно добавлять фото прямо из админки Cabine)
class CabineMediaInline(admin.TabularInline):
    model = CabineMedia.cabine.through  # для ManyToMany
    extra = 1


# Inline для удобств (amenities)
class CabineAmenityInline(admin.TabularInline):
    model = CabineAmenity
    extra = 1


@admin.register(CabineClass)
class CabineClassAdmin(admin.ModelAdmin):
    list_display = ["cabine_class", "description", "created_at", "updated_at"]
    search_fields = ["cabine_class", "description"]
    ordering = ["-pk"]


@admin.register(Cabine)
class CabineAdmin(admin.ModelAdmin):
    list_display = ["number", "cabine_class", "price", "capacity", "created_at", "updated_at"]
    search_fields = ["number", "description"]
    list_filter = ["cabine_class", "capacity"]
    ordering = ["-pk"]
    inlines = [CabineMediaInline, CabineAmenityInline]


@admin.register(CabineMedia)
class CabineMediaAdmin(admin.ModelAdmin):
    list_display = ["id", "media", "created_at", "updated_at"]
    search_fields = ["cabine__number"]
    ordering = ["-pk"]


@admin.register(CabineAmenity)
class CabineAmenityAdmin(admin.ModelAdmin):
    list_display = ["cabine", "amenity", "price", "created_at", "updated_at"]
    search_fields = ["amenity", "description"]
    list_filter = ["cabine"]
    ordering = ["-pk"]


@admin.register(CabineBooking)
class CabineBookingAdmin(admin.ModelAdmin):
    list_display = ["cabine", "user", "start_date", "end_date", "total_price", "created_at"]
    search_fields = ["cabine__number", "user__username"]
    list_filter = ["start_date", "end_date", "cabine"]
    ordering = ["-pk"]

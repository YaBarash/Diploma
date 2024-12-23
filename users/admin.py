from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    list_display = (
        "id",
        "email",
        "is_staff",
    )

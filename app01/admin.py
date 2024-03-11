from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from app01.models import *


# Register your models here.


class UserInfoAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "tel", "sex", "role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "name", "tel", "sex", "role", "is_staff")

    list_filter = ("is_staff", "is_superuser", "is_active")

    search_fields = ("username", "name", "tel")


class RecordAdmin(admin.ModelAdmin):
    list_display = ['nid', 'avatars', 'user', 'result_url', 'create_date']

    list_filter = ['user__username', 'create_date']

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Avatars)
admin.site.register(Record, RecordAdmin)

admin.site.site_header = '遥感影像地块分割管理系统'

admin.site.site_title = '遥感影像地块分割管理系统'

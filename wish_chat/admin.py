from django.contrib import admin
from django import forms

from . import models


class GroupUsersAdminForm(forms.ModelForm):

    class Meta:
        model = models.GroupUsers
        fields = "__all__"


class GroupUsersAdmin(admin.ModelAdmin):
    form = GroupUsersAdminForm
    list_display = [
        "group",
        "user",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class GroupAdminForm(forms.ModelForm):

    class Meta:
        model = models.Group
        fields = "__all__"


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    list_display = [
        "created",
        "group_name",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = "__all__"


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class MessageAdminForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = "__all__"


class MessageAdmin(admin.ModelAdmin):
    form = MessageAdminForm
    list_display = [
        "created",
        "last_updated",
        "Anonymous",
        "Text",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "Text",
    ]


admin.site.register(models.GroupUsers, GroupUsersAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Message, MessageAdmin)

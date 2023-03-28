from django import forms
from wish_chat.models import User
from wish_chat.models import Group
from django.contrib.auth.models import User
from wish_chat.models import Group
from wish_chat.models import GroupUsers
from . import models


class GroupUsersForm(forms.ModelForm):
    class Meta:
        model = models.GroupUsers
        fields = [
            "user",
            "group",
        ]

    def __init__(self, *args, **kwargs):
        super(GroupUsersForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.all()
        self.fields["group"].queryset = Group.objects.all()



class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
        fields = [
            "group_name",
        ]
        def __init__(self, *args, **kwargs):
            super(GroupForm, self).__init__(*args, **kwargs)
            self.fields["group_name"].queryset = Group.objects.all()


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "django_user",
        ]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["django_user"].queryset = User.objects.all()



class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = [
            "Anonymous",
            "Text",
            "group",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields["Anonymous"].widget = forms.CheckboxInput()
        self.fields["group"].queryset = Group.objects.all()
        self.fields["user"].queryset = GroupUsers.objects.all()


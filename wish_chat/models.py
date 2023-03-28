from django.db import models
from django.urls import reverse


class GroupUsers(models.Model):

    # Relationships
    user = models.ForeignKey("wish_chat.User", on_delete=models.CASCADE)
    group = models.ForeignKey("wish_chat.Group", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("wish_chat_GroupUsers_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("wish_chat_GroupUsers_update", args=(self.pk,))



class Group(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    group_name = models.TextField(max_length=20)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("wish_chat_Group_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("wish_chat_Group_update", args=(self.pk,))



class User(models.Model):

    # Relationships
    django_user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("wish_chat_User_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("wish_chat_User_update", args=(self.pk,))



class Message(models.Model):

    # Relationships
    group = models.ForeignKey("wish_chat.Group", on_delete=models.CASCADE)
    user = models.ForeignKey("wish_chat.GroupUsers", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Anonymous = models.BooleanField("Anonymous message? (y/n)",default=0, null=True, blank=True)
    Text = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("wish_chat_Message_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("wish_chat_Message_update", args=(self.pk,))


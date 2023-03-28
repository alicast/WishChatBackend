from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class GroupUsersListView(generic.ListView):
    model = models.GroupUsers
    form_class = forms.GroupUsersForm


class GroupUsersCreateView(generic.CreateView):
    model = models.GroupUsers
    form_class = forms.GroupUsersForm


class GroupUsersDetailView(generic.DetailView):
    model = models.GroupUsers
    form_class = forms.GroupUsersForm


class GroupUsersUpdateView(generic.UpdateView):
    model = models.GroupUsers
    form_class = forms.GroupUsersForm
    pk_url_kwarg = "pk"


class GroupUsersDeleteView(generic.DeleteView):
    model = models.GroupUsers
    success_url = reverse_lazy("wish_chat_GroupUsers_list")


class GroupListView(generic.ListView):
    model = models.Group
    form_class = forms.GroupForm


class GroupCreateView(generic.CreateView):
    model = models.Group
    form_class = forms.GroupForm


class GroupDetailView(generic.DetailView):
    model = models.Group
    form_class = forms.GroupForm


class GroupUpdateView(generic.UpdateView):
    model = models.Group
    form_class = forms.GroupForm
    pk_url_kwarg = "pk"


class GroupDeleteView(generic.DeleteView):
    model = models.Group
    success_url = reverse_lazy("wish_chat_Group_list")


class UserListView(generic.ListView):
    model = models.User
    form_class = forms.UserForm


class UserCreateView(generic.CreateView):
    model = models.User
    form_class = forms.UserForm


class UserDetailView(generic.DetailView):
    model = models.User
    form_class = forms.UserForm


class UserUpdateView(generic.UpdateView):
    model = models.User
    form_class = forms.UserForm
    pk_url_kwarg = "pk"


class UserDeleteView(generic.DeleteView):
    model = models.User
    success_url = reverse_lazy("wish_chat_User_list")


class MessageListView(generic.ListView):
    model = models.Message
    form_class = forms.MessageForm


class MessageCreateView(generic.CreateView):
    model = models.Message
    form_class = forms.MessageForm


class MessageDetailView(generic.DetailView):
    model = models.Message
    form_class = forms.MessageForm


class MessageUpdateView(generic.UpdateView):
    model = models.Message
    form_class = forms.MessageForm
    pk_url_kwarg = "pk"


class MessageDeleteView(generic.DeleteView):
    model = models.Message
    success_url = reverse_lazy("wish_chat_Message_list")

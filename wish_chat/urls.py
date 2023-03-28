from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("GroupUsers", api.GroupUsersViewSet)
router.register("Group", api.GroupViewSet)
router.register("User", api.UserViewSet)
router.register("Message", api.MessageViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("wish_chat/GroupUsers/", views.GroupUsersListView.as_view(), name="wish_chat_GroupUsers_list"),
    path("wish_chat/GroupUsers/create/", views.GroupUsersCreateView.as_view(), name="wish_chat_GroupUsers_create"),
    path("wish_chat/GroupUsers/detail/<int:pk>/", views.GroupUsersDetailView.as_view(), name="wish_chat_GroupUsers_detail"),
    path("wish_chat/GroupUsers/update/<int:pk>/", views.GroupUsersUpdateView.as_view(), name="wish_chat_GroupUsers_update"),
    path("wish_chat/GroupUsers/delete/<int:pk>/", views.GroupUsersDeleteView.as_view(), name="wish_chat_GroupUsers_delete"),
    path("wish_chat/Group/", views.GroupListView.as_view(), name="wish_chat_Group_list"),
    path("wish_chat/Group/create/", views.GroupCreateView.as_view(), name="wish_chat_Group_create"),
    path("wish_chat/Group/detail/<int:pk>/", views.GroupDetailView.as_view(), name="wish_chat_Group_detail"),
    path("wish_chat/Group/update/<int:pk>/", views.GroupUpdateView.as_view(), name="wish_chat_Group_update"),
    path("wish_chat/Group/delete/<int:pk>/", views.GroupDeleteView.as_view(), name="wish_chat_Group_delete"),
    path("wish_chat/User/", views.UserListView.as_view(), name="wish_chat_User_list"),
    path("wish_chat/User/create/", views.UserCreateView.as_view(), name="wish_chat_User_create"),
    path("wish_chat/User/detail/<int:pk>/", views.UserDetailView.as_view(), name="wish_chat_User_detail"),
    path("wish_chat/User/update/<int:pk>/", views.UserUpdateView.as_view(), name="wish_chat_User_update"),
    path("wish_chat/User/delete/<int:pk>/", views.UserDeleteView.as_view(), name="wish_chat_User_delete"),
    path("wish_chat/Message/", views.MessageListView.as_view(), name="wish_chat_Message_list"),
    path("wish_chat/Message/create/", views.MessageCreateView.as_view(), name="wish_chat_Message_create"),
    path("wish_chat/Message/detail/<int:pk>/", views.MessageDetailView.as_view(), name="wish_chat_Message_detail"),
    path("wish_chat/Message/update/<int:pk>/", views.MessageUpdateView.as_view(), name="wish_chat_Message_update"),
    path("wish_chat/Message/delete/<int:pk>/", views.MessageDeleteView.as_view(), name="wish_chat_Message_delete"),

)

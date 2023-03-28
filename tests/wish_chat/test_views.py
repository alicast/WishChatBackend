import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_GroupUsers_list_view(client):
    instance1 = test_helpers.create_wish_chat_GroupUsers()
    instance2 = test_helpers.create_wish_chat_GroupUsers()
    url = reverse("wish_chat_GroupUsers_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_GroupUsers_create_view(client):
    user = test_helpers.create_wish_chat_User()
    group = test_helpers.create_wish_chat_Group()
    url = reverse("wish_chat_GroupUsers_create")
    data = {
        "user": user.pk,
        "group": group.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_GroupUsers_detail_view(client):
    instance = test_helpers.create_wish_chat_GroupUsers()
    url = reverse("wish_chat_GroupUsers_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_GroupUsers_update_view(client):
    user = test_helpers.create_wish_chat_User()
    group = test_helpers.create_wish_chat_Group()
    instance = test_helpers.create_wish_chat_GroupUsers()
    url = reverse("wish_chat_GroupUsers_update", args=[instance.pk, ])
    data = {
        "user": user.pk,
        "group": group.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Group_list_view(client):
    instance1 = test_helpers.create_wish_chat_Group()
    instance2 = test_helpers.create_wish_chat_Group()
    url = reverse("wish_chat_Group_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Group_create_view(client):
    url = reverse("wish_chat_Group_create")
    data = {
        "group_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Group_detail_view(client):
    instance = test_helpers.create_wish_chat_Group()
    url = reverse("wish_chat_Group_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Group_update_view(client):
    instance = test_helpers.create_wish_chat_Group()
    url = reverse("wish_chat_Group_update", args=[instance.pk, ])
    data = {
        "group_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_list_view(client):
    instance1 = test_helpers.create_wish_chat_User()
    instance2 = test_helpers.create_wish_chat_User()
    url = reverse("wish_chat_User_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_User_create_view(client):
    django_user = test_helpers.create_User()
    url = reverse("wish_chat_User_create")
    data = {
        "django_user": django_user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_detail_view(client):
    instance = test_helpers.create_wish_chat_User()
    url = reverse("wish_chat_User_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_User_update_view(client):
    django_user = test_helpers.create_User()
    instance = test_helpers.create_wish_chat_User()
    url = reverse("wish_chat_User_update", args=[instance.pk, ])
    data = {
        "django_user": django_user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Message_list_view(client):
    instance1 = test_helpers.create_wish_chat_Message()
    instance2 = test_helpers.create_wish_chat_Message()
    url = reverse("wish_chat_Message_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Message_create_view(client):
    group = test_helpers.create_wish_chat_Group()
    user = test_helpers.create_wish_chat_GroupUsers()
    url = reverse("wish_chat_Message_create")
    data = {
        "Anonymous": true,
        "Text": "text",
        "group": group.pk,
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Message_detail_view(client):
    instance = test_helpers.create_wish_chat_Message()
    url = reverse("wish_chat_Message_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Message_update_view(client):
    group = test_helpers.create_wish_chat_Group()
    user = test_helpers.create_wish_chat_GroupUsers()
    instance = test_helpers.create_wish_chat_Message()
    url = reverse("wish_chat_Message_update", args=[instance.pk, ])
    data = {
        "Anonymous": true,
        "Text": "text",
        "group": group.pk,
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302

import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from wish_chat import models as wish_chat_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_wish_chat_GroupUsers(**kwargs):
    defaults = {}
    if "user" not in kwargs:
        defaults["user"] = create_wish_chat_User()
    if "group" not in kwargs:
        defaults["group"] = create_wish_chat_Group()
    defaults.update(**kwargs)
    return wish_chat_models.GroupUsers.objects.create(**defaults)
def create_wish_chat_Group(**kwargs):
    defaults = {}
    defaults["group_name"] = ""
    defaults.update(**kwargs)
    return wish_chat_models.Group.objects.create(**defaults)
def create_wish_chat_User(**kwargs):
    defaults = {}
    if "django_user" not in kwargs:
        defaults["django_user"] = create_User()
    defaults.update(**kwargs)
    return wish_chat_models.User.objects.create(**defaults)
def create_wish_chat_Message(**kwargs):
    defaults = {}
    defaults["Anonymous"] = ""
    defaults["Text"] = ""
    if "group" not in kwargs:
        defaults["group"] = create_wish_chat_Group()
    if "user" not in kwargs:
        defaults["user"] = create_wish_chat_GroupUsers()
    defaults.update(**kwargs)
    return wish_chat_models.Message.objects.create(**defaults)

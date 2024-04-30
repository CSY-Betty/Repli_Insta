from typing import Any
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

# Create your models here.


# 建立有創建 user 及 superuser 函式的 class，繼承自 UserManager
class CustomUserManager(UserManager):
    # 定義 email 驗證及使用者名稱跟密碼
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    # 定義創建一般使用者的函式
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    # 定義創建管理員的函式
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        name = name or "Admin"
        return self._create_user(name, email, password, **extra_fields)


# 定義 User 的資料表內容、資料類型及相關設定
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, default="")
    avatar = models.ImageField(
        upload_to="avatars", blank=True, null=True, default="avatars/default_avatar.jpg"
    )
    friends = models.ManyToManyField("self")
    friends_count = models.IntegerField(default=0)

    posts_count = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    # 將 CustomUserManager 指派到 User model 中
    objects = CustomUserManager()

    # 指定使用上面的哪個欄位作為 username
    # # 指定使用 email 當作 username
    USERNAME_FIELD = "email"
    # 指定使用 email 當作 email
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def posts_count(self):
        return self.posts.count()

    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return ""


class FriendshipRequest(models.Model):
    SENT = "sent"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    STATUS_CHOICES = ((SENT, "Sent"), (ACCEPTED, "Accepted"), (REJECTED, "Rejected"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_for = models.ForeignKey(
        User, related_name="received_friendshiprequests", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_friendshiprequests", on_delete=models.CASCADE
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=SENT)

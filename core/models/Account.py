from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

USER_TYPE = (
    ('1', "Low"),
    ('2', "Middle"),
    ('3', "High"),
)


class AccountManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            user = self.model(
                email=AccountManager.normalize_email(email),
                nickname=nickname
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email, nickname, password=None):
        if not email:
            user = self.model(
                email=AccountManager.normalize_email(email),
                nickname=nickname
            )
            user.is_admin = True
            user.set_password(password)
            user.save(using=self._db)
            return user


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "account"

    id = models.AutoField(primary_key=True)
    nickname = models.CharField(
        verbose_name="nick_name",
        max_length=30,
        blank=False,
        unique=True,
    )

    email = models.EmailField(
        verbose_name="email",
        max_length=25,
        unique=True
    )
    password = models.CharField(_("password"), max_length=128, blank=False, null=False)

    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    ## Required Field
    is_active = models.BooleanField(default=True)

    objects = AccountManager

    level = models.CharField(max_length=2, choices=USER_TYPE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}:{self.nickname}"

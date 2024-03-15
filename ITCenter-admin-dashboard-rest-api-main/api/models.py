from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Base manager for User mode"""
    def create_user(self, fullname, email, password=None):
        """Create a user profile"""
        if not email:
            raise ValueError("User should have an email")
        user = self.model(
            fullname=fullname,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return self.user

    def create_superuser(self, fullname, email, password):
        """Create a superuser profile"""
        superuser = self.create_user(fullname, email, password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """Base user model"""
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']
    objects = UserManager()

    def get_email(self):
        """Return email of a user"""
        return self.email

    def get_fullname(self):
        """Return fullname of a user"""
        return self.fullname

    def __str__(self):
        """String representation of a User object"""
        return self.fullname

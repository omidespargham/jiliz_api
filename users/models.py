# """
# Custom user model
# """
# from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     BaseUserManager,
#     PermissionsMixin
# )


# class UserManager(BaseUserManager):
#     """ Manger for users """

#     def create_user(self, email=None, username=None, phone_number=None, name=None, last_name=None, password=None,
#                     **extra_fields):
#         """ Create and return new user"""
#         user = self.model(email=email, username=username, phone_number=phone_number, name=name, last_name=last_name,
#                           **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, phone_number, name, last_name, password):
#         user = self.create_user(email=None, username=None, phone_number=phone_number, name=name, last_name=last_name,
#                                 password=password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self.db)
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     """ User in system"""
#     name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
#     username = models.CharField(max_length=200, blank=True, null=True, unique=True)
#     phone_number = models.IntegerField(unique=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     objects = UserManager()
#     REQUIRED_FIELDS = ['name', 'last_name']
#     USERNAME_FIELD = 'phone_number'
#     phone_verify = models.BooleanField(default=False)
#     email_verify = models.BooleanField(default=False)





#     def __str__(self):
#         return str(f'Profile os user {self.phone_number}')


# class UserCode(models.Model):
#     code = models.IntegerField()
#     phone_number = models.IntegerField()
#     created_time = models.DateTimeField(auto_now_add=True)
#     expired_time = models.DateTimeField(blank=True, null=True)


#     def __str__(self):
#         return str(f' code for {self.phone_number}')

#     # def save( # Comment these code because of the money staff
#     #         self, force_insert=False, force_update=False, using=None, update_fields=None
#     # ):
#     #     """" Send otp code automatic when object is saved"""
#         # send_opt_code(phone_number=self.phone_number, code=self.code)



#         # super(UserCode, self).save(force_insert=force_insert, force_update=force_update, using=None, update_fields=None)



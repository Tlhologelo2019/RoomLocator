from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin , BaseUserManager, User 



    

class UserAccountManager(BaseUserManager):
    def create_user(self , email, first_name , last_name , cellphone  , password =None):
        if not email:
            raise ValueError("User must have email address")

        email =self.normalize_email(email)
        user = self.model(email = email , first_name = first_name , last_name = last_name , cellphone = cellphone )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,first_name, last_name,cellphone,email, password):
        user = self.create_user(email, first_name , last_name , cellphone , password)

        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user

class UserAccount(AbstractBaseUser , PermissionsMixin):

    email           = models.EmailField(max_length=255, unique = True)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50) 
    cellphone       = models.CharField(max_length=15, unique = True)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    # type_of_user    = models.ForeignKey(TypeOfUser,on_delete=models.CASCADE)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','cellphone']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email



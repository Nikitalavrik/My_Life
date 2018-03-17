from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
    
    
    def get_absolute_url(self):
        return reverse(
            "user_page",
            kwargs={
                "username": self.username,
            
            }
        )

from django.contrib import admin
from account.models import *
from django.contrib.auth import get_user_model


admin.site.register(CustomUser)

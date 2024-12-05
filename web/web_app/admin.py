from django.contrib import admin
from web_app.models import (
    User, Game, UserModel
)

admin.site.register(User)
admin.site.register(Game)
admin.site.register(UserModel)


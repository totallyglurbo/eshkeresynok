from django.contrib import admin

from posts.models import Post, ReallyUser

admin.site.register(ReallyUser)
admin.site.register(Post)


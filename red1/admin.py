from django.contrib import admin
from .models import Post, Comment, Subweddit, Follow

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class FollowAdmin(admin.ModelAdmin):
    pass

@admin.register(Subweddit)
class SubwedditAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",)}

admin.site.register(Follow, FollowAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
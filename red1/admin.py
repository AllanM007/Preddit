from django.contrib import admin
from .models import Post, Comment, Subweddit

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class SubwedditAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subweddit, SubwedditAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
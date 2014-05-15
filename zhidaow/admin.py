from django.contrib import admin
from zhidaow.models import Post, Author, Column, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title', 'author', 'column', 'status', 'content', 'tag', 'description']}),
		('Info', {'fields': ['date'], 'classes': ['collapse']})
	]
	list_display = ('title', 'author', 'column', 'status', 'date')
	list_filter = ['date']
	search_fields = ['content', 'title', 'description']

admin.site.register(Post, PostAdmin)

admin.site.register(Author)
admin.site.register(Column)
admin.site.register(Tag)

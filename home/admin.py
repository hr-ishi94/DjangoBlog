from django.contrib import admin
from .models import * 

class TagTabularInline(admin.TabularInline):
    model= Tag

class PostAdmin(admin.ModelAdmin):
    inlines=[TagTabularInline]
    list_display=('title','category','author','date','status','section','mainpost')
    list_editable=('status','section','mainpost')
    search_fields=('title','section')



admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)

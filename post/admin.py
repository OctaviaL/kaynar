from django.contrib import admin
from post.models import *

class PetPost(admin.ModelAdmin):
    inlines = (PetImage,)

    list_display = ('name', 'owner','age', 'gender')
    list_filter = ('owner',)
    search_fields = ('name',)

    def post_count(self, obj):
        return obj.likes.filter(is_like=True).count()
    
    
class PetImage(admin.TabularInline):
    model = PetImage
    fields = ('Фотографии',)
    max_num = 4

admin.site.register(PetPost)
admin.site.register(PetImage)

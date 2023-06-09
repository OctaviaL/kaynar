from django.contrib import admin
from post.models import * 

class PetImageAdminInline(admin.TabularInline):
    model = PetImage
    max_num = 6
    min_num = 1

@admin.register(PetPost)
class PetPostAdmin(admin.ModelAdmin):
    inlines = [PetImageAdminInline,]
    list_display = ('category', 'gender', 'owner')
    list_filter = ('category', )
    list_filter = ('category',)

    def post_count(self, obj):
        return obj.likes.filter(is_like=True).count()

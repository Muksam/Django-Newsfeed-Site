from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name', 'status']
    search_fields = ['cat_name']
    actions = ['update_status_active', 'update_status_inactive']


    def update_status_active(self, request, query):
          return query.update(status=True)
    update_status_active.short_description = 'Active'


    def update_status_inactive(self, request, query):
          return query.update(status=False)
    update_status_inactive.short_description = 'Inactive'


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['name','title','category ']
    list_display = ['name','status','category','posted_by']
    actions = ['update_status_active', 'update_status_inactive']



    def update_status_active(self, request, query):
          return query.update(status=True)
    update_status_active.short_description = 'Active'


    def update_status_inactive(self, request, query):
          return query.update(status=False)
    update_status_inactive.short_description = 'Inactive'


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}




@admin.register(LNews)
class AdminLNews(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Contact)

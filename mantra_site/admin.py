from django.contrib import admin

from .models import Cover, Tiles, Section2, Videos, About

# Register your models here.


class CoverModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super(CoverModelAdmin, self).has_add_permission(request)


class TilesModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super(TilesModelAdmin, self).has_add_permission(request)


class Section2ModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super(Section2ModelAdmin, self).has_add_permission(request)


class VideosModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super(VideosModelAdmin, self).has_add_permission(request)


class AboutModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super(AboutModelAdmin, self).has_add_permission(request)


admin.site.register(Cover, CoverModelAdmin)
admin.site.register(Tiles, TilesModelAdmin)
admin.site.register(Section2, Section2ModelAdmin)
admin.site.register(Videos, VideosModelAdmin)
admin.site.register(About, AboutModelAdmin)

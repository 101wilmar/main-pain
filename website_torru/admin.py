from django.contrib import admin
from .models import GraphicDesign, MotionDesign, TreeD_Design



@admin.register(GraphicDesign)
class GraphicDesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'image_preview')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)
    readonly_fields = ('uploaded_at',)
    
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return "Нет изображения"
    image_preview.allow_tags = True
    image_preview.short_description = 'Предпросмотр'

@admin.register(MotionDesign)
class MotionDesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'cover_preview', 'video1')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)
    readonly_fields = ('uploaded_at',)
    
    def cover_preview(self, obj):
        if obj.cover:
            return f'<img src="{obj.cover.url}" width="100" height="100" />'
        return "Нет обложки"
    cover_preview.allow_tags = True
    cover_preview.short_description = 'Предпросмотр обложки'

@admin.register(TreeD_Design)
class TreeD_DesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'image_preview')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)
    readonly_fields = ('uploaded_at',)
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return "Нет изображения"
    image_preview.allow_tags = True
    image_preview.short_description = 'Предпросмотр'
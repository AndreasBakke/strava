from django.contrib import admin

from .models import Club, Distances, Secret
# Register your models here.

@admin.action(description='Reset distance back to 0')
def resetDistance(modeladmin, request, queryset):
    queryset.update(distance=0)
    
class DistanceAdmin(admin.ModelAdmin):
    actions = [resetDistance]

admin.site.register(Club)
admin.site.register(Distances, DistanceAdmin)
admin.site.register(Secret)
 
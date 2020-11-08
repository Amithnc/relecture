from django.contrib import admin
from .models import post

class postAdmin(admin.ModelAdmin):
    list_display=('organization','subject')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organization=request.user)


    def save_model(self, request, obj, form, change):
        obj.organization = request.user
        obj.save()


admin.site.register(post,postAdmin)



admin.site.index_title="RElecture"
admin.site.site_title="Admin-Portal"
admin.site.site_header="Relecture- ADMIN" 
from django.contrib import admin
from django.shortcuts import render
from .models import NovaPage, NovaBlock

@admin.register(NovaPage)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "updated_at")
    change_form_template = "nova/admin_page.html"

    def change_view(self, request, object_id, form_url="", extra_context=None):
        page = NovaPage.objects.get(pk=object_id)
        extra_context = {"page": page}
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


@admin.register(NovaBlock)
class BlockAdmin(admin.ModelAdmin):
    list_display = ("page", "type", "order")


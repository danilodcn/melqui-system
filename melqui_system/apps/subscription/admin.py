from django.contrib import admin
from import_export.admin import ExportMixin
from import_export.resources import ModelResource

from melqui_system.apps.subscription.models import Subscription


class SubscriptionResource(ModelResource):
    class Meta:
        model = Subscription


class SubscriptionAdmin(admin.ModelAdmin, ExportMixin):
    resource_classes = (SubscriptionResource,)
    autocomplete_fields = ('indicated_by',)
    search_fields = ('cpf', 'full_name')

    readonly_fields = ('created_at',)


admin.site.register(Subscription, SubscriptionAdmin)

from django.contrib import admin
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import HttpRequest
from import_export.admin import ExportActionMixin, ExportMixin
from import_export.resources import ModelResource
from rangefilter.filters import DateRangeFilter, NumericRangeFilterBuilder

from melqui_system.apps.subscription.models import Subscription


class SubscriptionResource(ModelResource):
    class Meta:
        model = Subscription
        name = 'Import/Export inscrições'


class SubscriptionAdmin(ExportActionMixin, ExportMixin, admin.ModelAdmin):
    resource_classes = SubscriptionResource
    autocomplete_fields = ('indicated_by',)
    search_fields = ('cpf', 'full_name')

    readonly_fields = ('created_at',)

    list_display = ('id', 'full_name', 'created_at', 'indicated_by_count')
    list_display_links = ('id', 'full_name')

    list_filter = (
        ('created_at', DateRangeFilter),
        (
            'indications',
            NumericRangeFilterBuilder(title='Numero de indicações'),
        ),
    )

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super().get_queryset(request)
        qs = qs.annotate(indications_count=Count('indications'))
        return qs

    @admin.display(
        ordering='indications_count', description='Numero de indicações'
    )
    def indicated_by_count(self, obj):
        return obj.indications_count


admin.site.register(Subscription, SubscriptionAdmin)

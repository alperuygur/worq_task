from django.contrib import admin
from .models import Report, ReportMerchants


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    fields = ('name', 'brand', 'price_selling', 'category', 'seller', 'seller_score', 'seller_city')
    list_display = ('name', 'brand', 'price_selling', 'category', 'seller', 'seller_score', 'seller_city', 'last_update')


@admin.register(ReportMerchants)
class ReportMerchantsAdmin(admin.ModelAdmin):
    fields = ('report', 'other_merchant', 'other_merchant_score', 'other_merchant_city')
    list_display = ('report', 'other_merchant', 'other_merchant_score', 'other_merchant_city')
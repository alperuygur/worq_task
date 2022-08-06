from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify


class Report(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, blank=True, null=True)
    price_selling = models.CharField(max_length=10, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    seller = models.CharField(max_length=50, blank=True, null=True)
    seller_score = models.CharField(max_length=3, blank=True, null=True)
    seller_city = models.CharField(max_length=50, blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "mdl_report"
        verbose_name_plural = "Reports"
        verbose_name = "Report"
    
    def __str__(self):
        return self.name
    


class ReportMerchants(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='report')
    other_merchant = models.CharField(max_length=50, blank=True, null=True)
    other_merchant_score = models.CharField(max_length=3, blank=True, null=True)
    other_merchant_city = models.CharField(max_length=50, blank=True, null=True)
    

    class Meta:
        db_table = "mdl_reportMerchants"
        verbose_name_plural = "Report Merchants"
        verbose_name = "Report Merchant"
    
    def __str__(self):
        return str(self.report)
    
    


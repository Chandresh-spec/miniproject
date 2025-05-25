from django.contrib import admin
from .models import chaivarirty,ChaiDetails
# Register your models here.
class ChaiDetailsInline(admin.StackedInline):
    model = ChaiDetails
    can_delete = False
    verbose_name_plural = 'Chai Details'

class ChaiVarietyAdmin(admin.ModelAdmin):
    inlines = [ChaiDetailsInline]
    list_display = ('name', 'type', 'date_added')
    search_fields = ('name',)

# Register models
admin.site.register(chaivarirty, ChaiVarietyAdmin)
admin.site.register(ChaiDetails)
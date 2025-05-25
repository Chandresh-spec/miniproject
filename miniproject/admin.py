from django.contrib import admin
from .models import chaivarirty,ChaiDetails,ChaiReview,Ingredient
# Register your models here.
class ChaiDetailsInline(admin.StackedInline):
    model = ChaiDetails
    can_delete = False
    verbose_name_plural = 'Chai Details'

class ChaiVarietyAdmin(admin.ModelAdmin):
    inlines = [ChaiDetailsInline]
    list_display = ('name', 'type', 'date_added')
    search_fields = ('name',)

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
    inlines = [ChaiReviewInline]
    list_display = ('name', 'type', 'date_added')
    search_fields = ('name',)
    filter_horizontal = ('ingredients',)

# Register models
admin.site.register(chaivarirty, ChaiVarietyAdmin)
admin.site.register(ChaiDetails)
admin.site.register(ChaiReview)
admin.site.register(Ingredient)
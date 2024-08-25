from django.contrib import admin
from .models import Pet,PetType,Adoption
# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','gender','price']

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ['customer','pet','adoption_time']

class PetTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Pet,PetAdmin)
admin.site.register(PetType,PetTypeAdmin)
admin.site.register(Adoption,AdoptionAdmin)
from django.contrib import admin
from .models import project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):    #para hacer que muestre los campos de fechas
    readonly_fields=('created','updated')



admin.site.register(project, ProjectAdmin)


#Superusuario devmcgann holahola1
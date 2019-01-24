from django.db import models

# Create your models here.
# clave superusuario gmgab hola

#si añado algun campo hay que migrar
#python manage.py makemigrations portfolio //  python manage.py migrate portfolio

class project (models.Model):
    title= models.CharField(max_length=200, verbose_name="Título")
    description= models.TextField(verbose_name="Descripción")
    image= models.ImageField(verbose_name="Imagen", upload_to = 'projects')
    link=models.URLField(null=True, blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        ordering=["-created"]

    def __str__(self):
        return self.title  #para que no aparezca "project object" y nos muestre el titulo del prj

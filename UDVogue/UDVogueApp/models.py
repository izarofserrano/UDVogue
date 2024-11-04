from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=10)
    revistas_publicadas = models.ManyToManyField('Revista', related_name='editoriales', blank=True)

    def agregar_revista(self, revista):
        """Agrega una revista a la lista de revistas publicadas"""
        self.revistas_publicadas.add(revista)
    
    def mostrar_revistas(self):
        """Muestra los títulos de las revistas publicadas por la editorial"""
        return [revista.titulo for revista in self.revistas_publicadas.all()]

    def __str__(self):
        return self.nombre

class Revista(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_publi = models.CharField(max_length=100)
    numero_edicion = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.titulo} (Edición {self.numero_edicion})"


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.PositiveIntegerField()

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto"""
        self.precio = nuevo_precio
        self.save()

    def ajustar_stock(self, cantidad):
        """Ajusta el stock disponible en función de la cantidad especificada"""
        self.stock = max(0, self.stock + cantidad)  # Evitar stock negativo
        self.save()

    def mostrar_informacion(self):
        """Muestra la información completa del producto"""
        return f"Producto: {self.nombre_producto}, Precio: {self.precio}, Stock: {self.stock}"

    def __str__(self):
        return self.nombre_producto
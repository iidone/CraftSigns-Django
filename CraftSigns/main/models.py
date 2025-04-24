from django.db import models

class Production(models.Model):
    name = models.CharField("Название продукции", max_length = 255)
    description = models.CharField("Описание", max_length = 255)
    image = models.ImageField("Изображение продукции", upload_to="", null=True, max_length=255, blank=True)
    type_object = models.CharField("Тип продукции", max_length=100)

    def __str__(self):
        return f"Название: {self.name}"
    
    class Meta:
        abstract = False
        verbose_name = "Продукция"
        verbose_name_plural = "Продукции"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        
class OurWorks(models.Model):
    name = models.CharField("Название работы", max_length = 255)
    description = models.CharField("Описание работы", max_length = 255)
    image = models.ImageField("Изображение работы", upload_to="media/", null=True, max_length = 255, blank=True)

    def __str__(self):
        return f"Название: {self.name}"
    
    class Meta:
        abstract = False
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        
class Services(models.Model):
    name = models.CharField("Услуга", max_length = 255)
    description = models.CharField("Описание услуги", max_length = 1055)
    image = models.ImageField("Изображение услуги", upload_to="media/", null=True, max_length = 255, blank = True)

    def __str__(self):
        return f"Название: {self.name}"
    
    class Meta:
        abstract = False
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
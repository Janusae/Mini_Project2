from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30 , verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    description = models.TextField(verbose_name="توضیحات محصول")
    image = models.ImageField(upload_to="media" , verbose_name="عکس محصول")
    active =models.BooleanField(default=False , verbose_name="موجود بودن محصول" , null=True , blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"
class Category(models.Model):
    category = models.ManyToManyField(Product)
    def __str__(self):
        return f"{self.category}"
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
from django.db import models



class Catalog(models.Model):


    store = models.OneToOneField('Store', on_delete=models.CASCADE, primary_key=True, related_name='catalog')





class Product(models.Model):


    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='product', blank=True, null=True)

    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products')


    @classmethod
    def create(cls, name, price, description, image, store):
        product = cls(name=name, price=price, description=description, image=image, store=store)
        return product
    







class Platform(models.Model):


    catalog = models.OneToOneField(Catalog, on_delete=models.CASCADE, primary_key=True, related_name='platform')
    name = "placeholder"

    class Meta:
        abstract = True

    @classmethod
    def create(cls, name):
        platform = cls(name=name)
        return platform
    


class Amazon(Platform):

    name = "Amazon"

    def __str__(self):
        return self.name
    

class Shopify(Platform):

    name = "Shopify"

    def __str__(self):
        return self.name
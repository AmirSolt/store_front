from django.db import models




class Store(models.Model):

    username = models.CharField(max_length=50, unique=True, primary_key=True, blank=False, null=False)
    pfp = models.ImageField(upload_to='pfp', blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)



    @classmethod
    def create(cls, username):
        store = cls(username=username)
        return store
    


class Links(models.Model):


    store = models.OneToOneField(Store, on_delete=models.CASCADE, primary_key=True, related_name='links')


    website = models.CharField(max_length=100, blank=True, null=True)
    linktree = models.CharField(max_length=100, blank=True, null=True)
    amazon = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    tiktok = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    @classmethod
    def create(cls, store):
        links = cls(store=store)
        return links
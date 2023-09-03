from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim=models.CharField(max_length=50)
    def __str__(self):
        return self.isim

class Eğitimler(models.Model):
    kategori=models.ForeignKey(Kategori,on_delete=models.CASCADE,null=True)
    isim=models.CharField(max_length=200)
    aciklama=models.TextField(max_length=400)
    fiyat=models.IntegerField()
    resim=models.FileField(upload_to="urunler/",null=True,blank=True, verbose_name="Ürün Resmi")
    tarih=models.DateField()
    def __str__(self):
        return self.isim

class Kadro(models.Model):
    isim=models.CharField(max_length=50)
    meslek=models.CharField(max_length=100)
    aciklama=models.TextField(max_length=500)
    resim=models.FileField(upload_to="kadrolar",blank=True,null=True)
    linkedn=models.URLField(blank=True,null=True)
    instagram=models.URLField(blank=True,null=True)
    github=models.URLField(blank=True,null=True)
    

    def __str__(self):
        return self.isim
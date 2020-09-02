from django.db import models

# Create your models here.


class Categorie(models.Model):
	libelle = models.CharField(max_length = 50)

	def __str__(self):
		return self.libelle


class FraisDivers(models.Model):
	libelle = models.CharField(max_length = 50)

	def __str__(self):
		return self.libelle


class Produit(models.Model):
	nom = models.CharField(max_length = 50)
	marque = models.CharField(max_length = 50)
	categorie = models.ForeignKey(Categorie , on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/produit',)
	qte_stocke = models.IntegerField(default=0 , null=True ,blank=True)
	option = models.CharField(max_length = 250, null=True ,blank=True)

	def __str__(self):
		return self.nom
		
class Achat(models.Model):
	date_achat = models.DateField() 
	qte = models.IntegerField( null=True ,blank=True)
	prix_u = models.FloatField()
	produit = models.ForeignKey(Produit , on_delete=models.CASCADE, null=True ,blank=True)
	fraisdivers = models.ForeignKey(FraisDivers , on_delete=models.CASCADE, null=True ,blank=True)
			
class Vente(models.Model):
	date_vente = models.DateField() 
	qte = models.IntegerField( null=True ,blank=True)
	prix_u = models.FloatField()
	produit = models.ForeignKey(Produit , on_delete=models.CASCADE, null=True ,blank=True)
	fraisdivers = models.ForeignKey(FraisDivers , on_delete=models.CASCADE, null=True ,blank=True)
	
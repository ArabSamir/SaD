from django import forms

from .models import *
from django.conf					import settings

class ProduitForm(forms.ModelForm):
	qte_stocke = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Quantite'}), required = True)
	categorie = forms.ModelChoiceField(widget=forms.Select(attrs={  'class':'form-control'}),queryset = Categorie.objects.all())
	nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nom'}), required = True)
	option = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Option'}), required = True)
	marque = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Marque'}), required = True)
	
	class Meta:
		model = Produit
		fields = '__all__'

class EntreeForm(forms.ModelForm):
	date_entree = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS ,widget=forms.DateInput(format='%d/%m/%Y',attrs={'class': 'form-control ','placeholder':'JJ/MM/AAAA'} ), required = True)
	qte = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Quantite'}), required = True)
	prix_u = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Prix Unitaire'}), required = True)
	produit = forms.ModelChoiceField(widget=forms.Select(attrs={  'class':'form-control'}),queryset = Produit.objects.all())
	
	class Meta:
		model = Entree
		fields = '__all__'
	

	def clean_qte(self , *args,**kwargs):
		qte = self.cleaned_data.get('qte')

		if qte < 1 :
			raise forms.ValidationError('Verifier votre quantite')
		else:
			return qte

class SortieForm(forms.ModelForm):
	date_sortie = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS ,widget=forms.DateInput(format='%d/%m/%Y',attrs={'class': 'form-control ','placeholder':'JJ/MM/AAAA'} ), required = True)
	qte = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Quantite'}), required = True)
	prix_u = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Prix Unitaire'}), required = True)
	produit = forms.ModelChoiceField(widget=forms.Select(attrs={  'class':'form-control'}),queryset = Produit.objects.all())
	

	class Meta:
		model = Sortie
		fields = '__all__'


	def clean_qte(self , *args,**kwargs):
		qte = self.cleaned_data.get('qte')

		if qte < 1 :
			raise forms.ValidationError('Verifier votre quantite')
		else:
			return qte

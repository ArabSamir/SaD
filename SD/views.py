from django.shortcuts import render
from Stock.models import *
from datetime import datetime , date
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/admin/login/')
def home(request):
 	template_name = 'home.html'
 	end_date = datetime.now()
 	start_date = date(end_date.year, end_date.month, 1)
 	# .filter(date_achat__range=(start_date, end_date))
 	nb_achat = Achat.objects.exclude(fraisdivers = None  )
 	print(nb_achat)
 	# montant_de_achat = 0
 	# for x in nb_achat:
 	# 	montant_de_achat = montant_de_achat + (x.prix_u * x.qte)



 	nb_vente = Vente.objects.filter(date_vente__range=(start_date, end_date))
 	montant_de_vente = 0
 	for x in nb_vente:
 		montant_de_vente = montant_de_vente + (x.prix_u * x.qte)



 	test = Vente.objects.filter(date_vente__range=(start_date, end_date)).values('produit').annotate(dcount=Count('produit'))

 	args = {
 		'nb_achat':nb_achat.count(),
 		# 'montant_de_achat':montant_de_achat,
 		'nb_vente':nb_vente.count(),
 		'montant_de_vente':montant_de_vente,
 		'test':test,
 	}
 	return render(request , template_name , args)
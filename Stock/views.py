from django.contrib 				import messages
from django.shortcuts import render ,redirect , get_object_or_404
from .forms import *
from .models import Produit ,Achat , Vente
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


# Create your views here.

@login_required(login_url='/admin/login/')
def list_produit(request):
	template_name = 'list_produit.html'
	produits = Produit.objects.all()
	paginator = Paginator(produits, 1) # Show 25 contacts per page.

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	args = {
		'page_obj': produits,
		}
	return render(request, template_name, args)



@login_required(login_url='/admin/login/')
def produit(request):
	template_name = 'produit.html'
	form = ProduitForm()
	if request.method == "POST":
		try:
			form = ProduitForm(request.POST , request.FILES or None)
			if form.is_valid():
				form.save()
				messages.success(request , 'Produit Ajoute avec succe')
				return redirect('list_produit')
		except Exception as e:
			messages.error(request , f'Produit n\'a pas été ajoute {e}')
			return redirect('list_produit')

	args = {
		'form':form,
	}

	return render(request , template_name , args)


@login_required(login_url='/admin/login/')
def modifier_produit(request , pk):
	template_name = 'produit.html'
	produit =get_object_or_404(Produit , pk=pk)
	print(produit)
	form = ProduitForm(instance = produit)
	if request.method == "POST":
		try:
			form = ProduitForm(request.POST , request.FILES or None ,instance = produit)
			if form.is_valid():
				form.save()
				messages.success(request , 'Produit modifier avec succe')
				return redirect('list_produit')
		except Exception as e:
			messages.error(request , 'Produit n\'a pas été modifer')
			return redirect('list_produit')

	args = {
		'form':form,
	}

	return render(request , template_name , args)




@login_required(login_url='/admin/login/')
def achat(request):
	template_name = 'achat.html'
	form = AchatForm()
	if request.method == "POST":
		try:
			form = AchatForm(request.POST , request.FILES or None)
			if form.is_valid():
				form.save(commit=False)
				produit_qte = form.cleaned_data['produit']
				print(type(produit_qte))
				produit_qte.qte_stocke = produit_qte.qte_stocke + form.cleaned_data['qte']
				produit_qte.save()
				form.save()
				messages.success(request , 'achat Ajoute avec succe')
				return redirect('list_achat')
		except Exception as e:
			messages.error(request , f'achat n\'a pas été ajoute {e}')
			return redirect('list_entree')

	args = {
		'form':form,
	}

	return render(request , template_name , args)

@login_required(login_url='/admin/login/')
def entree(request):
	template_name = 'entree.html'
	form = EntreeForm()
	if request.method == "POST":
		try:
			form = EntreeForm(request.POST , request.FILES or None)
			if form.is_valid():
				form.save()
				
				messages.success(request , 'entree Ajoute avec succe')
				return redirect('list_vente')
		except Exception as e:
			messages.error(request , f'entree n\'a pas été ajoute {e}')
			return redirect('list_vente')

	args = {
		'form':form,
	}

	return render(request , template_name , args)

@login_required(login_url='/admin/login/')
def list_achat(request):
	template_name = 'list_achat.html'
	entrees = Achat.objects.filter(fraisdivers = None  )
	# paginator = Paginator(entrees, 1) # Show 25 contacts per page.

	# page_number = request.GET.get('page')
	# page_obj = paginator.get_page(page_number)
	args = {
		'page_obj': entrees,
		}
	return render(request, template_name, args)


@login_required(login_url='/admin/login/')
def vente(request):
	template_name = 'vente.html'
	form = VenteForm()
	if request.method == "POST":
		try:
			form = VenteForm(request.POST , request.FILES or None)
			if form.is_valid():
				form.save(commit=False)
				produit  = form.cleaned_data['produit']
				qte  = form.cleaned_data['qte']
				if qte > produit.qte_stocke :
					messages.error(request , 'stock insufisant!!')
				elif  qte < 1 :
					messages.error(request , 'Verifier votre quantite!')
				else:
					produit.qte_stocke = produit.qte_stocke  - qte
					produit.save()
					form.save()
					messages.success(request , 'vente Ajoute avec succe')
					return redirect('list_vente')

		except Exception as e:
			messages.error(request , f'vente n\'a pas été ajoute {e}')
			return redirect('list_vente')

	args = {
		'form':form,
	}

	return render(request , template_name , args)

@login_required(login_url='/admin/login/')
def list_vente(request):
	template_name = 'list_vente.html'
	ventes = Vente.objects.filter(fraisdivers = None  )
	paginator = Paginator(ventes, 1) # Show 25 contacts per page.

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	args = {
		'page_obj': ventes,
		}
	return render(request, template_name, args)


@login_required(login_url='/admin/login/')
def sortie(request):
	template_name = 'sortie.html'
	form = SortieForm()
	if request.method == "POST":
		try:
			form = SortieForm(request.POST , request.FILES or None)
			if form.is_valid():
				form.save()
				
				messages.success(request , 'sortie Ajoute avec succe')
				return redirect('list_vente')
		except Exception as e:
			messages.error(request , f'sortie n\'a pas été ajoute {e}')
			return redirect('list_vente')

	args = {
		'form':form,
	}

	return render(request , template_name , args)



def entree_sortie(request):
	template_name ='entree_sortie.html'
	achats = Achat.objects.exclude(fraisdivers = None  )
	ventes = Vente.objects.exclude(fraisdivers = None  )
	args = {
		'ventes': ventes,
		'achats': achats,
		}
	return render(request, template_name, args)

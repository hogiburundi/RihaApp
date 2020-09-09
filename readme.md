1) le nom de l'application doit
	- ne pas contenir d'espacement
	- ne pas être ajouter manuellement dans settings.py

2) le fichier ```__init__.py``` doit comptenir une ligne:

```python
APP_NAME = "Nom de l'Application" #exemple: Identité Complète
```

2) le fichier urls
	- doit ne pas être référencé manuellement dans urls principal
	- doit contenir un chemin "" avec l'attribut name = nom de l'application
	- les attributs name des autres applications remarquables doivent être précédés
	du nom de application suivi d'un underscore (ex: idcompete_form)
	
	les applications remarquables sont:
		- user_form (formulaire de creation d'un document)
		- user_list (page listants les documents commandés coté user)
		- secr_list (page listants les documents commandés coté admin)
		- secr_edit (page pour preview contenant valider, rejeter, imprimer...)
		- payment_form (page containant les formulaires de payment)

3) le model doit contenir les models Document et PriceHistory.

4) le model ```Document``` doit contenir les champs:

```python
rejection_msg = models.TextField(null=True, blank=True)
secretary_validated = models.BooleanField(default=False)
ready = models.BooleanField(default=False)
```

elle doit aussi avoir les methodes simple suivantes

```python
def requirements():
	return ["cahier de menage",...]

def price():
	return PriceHistory.object.filter(zone=self.zone).last().total() # +
	# PriceHistory.object.filter(commune=self.commune).last().total() ...

def onlyPaid(): # /!\ sans self
	return Document.objects.filter(zone_payment__isnull=False, secretary_validated__isnull=True)
	# tout les filter necessaire en fait pas seulement zone
	# si il y a pas de payments requises : return Document.objects.all()
def paymentPercent(self):
	return 100 if self.zone_payment else 0

def validationPercent(self):
	progression = 0
	progression += 70 if self.secretary_validated != None else 0
	progression += 30 if self.ready else 0
	return progression
```

4) le model price history doit comptenir une methode
```python
def total(self):
	return self.zone_price # + self.commune_price ...
```
plusieres champs peuvent faire partie de l'application comme ```date, zone, zone_price, commune, commune_price...```

5) le fichier ```forms.py``` doit contenir une formulaire ```ValidationForm``` variant selon le requis pouvant être cause de rejection et ainsi il faudra revoir par consequent la readaptations de ```SecretaryListView``` et ```SecretaryView``` et les templates y relatifs
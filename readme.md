1) le nom de l'application doit
	- ne pas contenir d'espacement
	- ne pas être ajouter manuellement dans settings.py

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

3) le model doit contenir les champs:
	```
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)
	```
	
	elle doit aussi avoir une methode simple suivante
```
	def requirements():
		return ["cahier de menage",...]
```


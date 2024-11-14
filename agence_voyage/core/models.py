from django.db import models
from django.conf import settings

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pays = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    etoiles = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=3)
    
    def __str__(self):
        return self.name

class OffreVoyage(models.Model):
    TYPE_CHOICES = [
        ('sejour', 'Séjour'),
    ]
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    destination_pays = models.CharField(max_length=100, blank=True)
    destination_ville = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    # Infos détaillées
    etablissement = models.CharField(max_length=100, blank=True)
    nb_etoiles = models.PositiveSmallIntegerField(default=2)
    note = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    commentaires = models.TextField(blank=True)
    # Prix
    number_of_people = models.IntegerField(null=True, blank=True) 
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    min_price_w_flight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    include_flight = models.BooleanField(default=False)
    # Images & coordonnées
    main_image = models.ImageField(upload_to='offres_voyages/', null=True, blank=True)
    liste_images = models.JSONField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
      
    # Détails supplémentaires
    durees_disponibles = models.JSONField(null=True, blank=True)    
    presentation = models.TextField(blank=True) 
    details_offre = models.TextField(blank=True)
    equipement_chambre = models.TextField(blank=True)
    equipement_hotel = models.TextField(blank=True)
    informations_complementaires = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titre} - {self.destination_ville}, {self.destination_pays}"
    def __str__(self):
        return self.title
    
class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    offre = models.ForeignKey(OffreVoyage, on_delete=models.CASCADE, related_name="reservations")
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, verbose_name="En attente de confirmation")
        
    def __str__(self):
        return f"Réservation de {self.user} pour {self.offre}"
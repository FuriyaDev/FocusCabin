from django.db import models
from bases.model import BaseModel

# class for cabines
class CabineClass(BaseModel):
    cabine_class = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cabine_class

    class Meta:
        verbose_name = 'Cabine Class'
        verbose_name_plural = 'Cabine Classes'
        db_table = 'cabine_classes'

# CABINE MODEL
class Cabine(BaseModel):
    number = models.IntegerField()
    description = models.CharField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.PositiveIntegerField()
    cabine_class = models.ForeignKey(CabineClass, on_delete=models.CASCADE)    
    
    class Meta:
        verbose_name = 'Cabine'
        verbose_name_plural = 'Cabines'
        db_table = 'cabines'

    def __str__(self):
        return self.number

# Photos of cabines
class CabineMedia(BaseModel):
    cabine = models.ManyToManyField(Cabine, related_name='media')
    media = models.FileField(upload_to='cabine_media/')

    class Meta:
        verbose_name = 'Cabine Media'
        verbose_name_plural = 'Cabine Media'
        db_table = 'cabine_media'

# stuff like pillow, blank and playstation. offering for charge
class CabineAmenity(BaseModel):
    cabine = models.ForeignKey(Cabine, on_delete=models.CASCADE, related_name='amenities')
    amenity = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.FileField(upload_to='cabine_amenities/')
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Cabine Amenity'
        verbose_name_plural = 'Cabine Amenities'
        db_table = 'cabine_amenities'

class CabineBooking(BaseModel):
    cabine = models.ForeignKey(Cabine, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cabine_bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cabine Booking'
        verbose_name_plural = 'Cabine Bookings'
        db_table = 'cabine_bookings'

    def __str__(self):
        return f"Booking {self.id} for Cabine {self.cabine.number} by {self.user.username}"
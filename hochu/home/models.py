from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class frm1(models.Model):
    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2, 'Не менее двух букв')]
    )
    number = models.CharField(
        max_length=18,
        validators=[
            MinLengthValidator(10, 'Не менее десяти цифр'), 
            MaxLengthValidator(18, 'Не более десяти цифр'),
            ]
    )
    sent = models.BooleanField(default=False)
    
    def __str__(self):
      return(self.title)
    
    
class frm2(models.Model): 
    number = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(10, 'Не менее десяти цифр')]
    )
    sent = models.BooleanField(default=False)
    width = models.IntegerField()
    length = models.IntegerField()
    
    VID_NAVESA_CHOISES = [
      ('Поликарбонат', 'Поликарбонат'),
      ('Металлопрофиль','Металлопрофиль'),
      ('Монолит','Монолит'),
      ('Мягкая кровля','Мягкая кровля'),
      ('Дерево','Дерево'),
      ('Профильная труба','Профильная труба'),
      ('Металлочерепица','Металлочерепица'),
      ('Ковка','Ковка'), 
    ]
    tip = models.CharField(
        max_length=40,
        choices=VID_NAVESA_CHOISES,
        default='POLI',
    )
    
    def __str__(self):
      return(self.title)
  
  
class newfrm(models.Model): 
    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2, 'Не менее двух букв')]
    )
    number = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(10, 'Не менее десяти цифр')]
    )
    sent = models.BooleanField(default=False)
    width = models.CharField(
        max_length=20
    )
    length = models.CharField(
        max_length=20
    )
    
    VID_NAVESA_CHOISES = [
      ('POLI', 'Поликарбонат'),
      ('METAL','Металлопрофиль'),
      ('MONO','Монолит'),
      ('SOFT','Мягкая кровля'),
      ('DEREVO','Дерево'),
      ('PROFIL','Профильная труба'),
      ('METCHER','Металлочерепица'),
      ('KOVK','Ковка'), 
    ]
    tip = models.CharField(
        max_length=40,
        choices=VID_NAVESA_CHOISES,
        default='POLI',
    )
    
    def __str__(self):
      return(self.title)


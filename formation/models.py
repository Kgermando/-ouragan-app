from django.db import models

# Create your models here.


class Formation(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=800)

    def __str__(self):
        return self.title


class Art_Culture(models.Model):
    title_art = models.CharField(max_length=150)
    contenu_art = models.TextField(max_length=500)
    last_accessed = models.DateTimeField()

    def __str__(self):
        return self.title_art


class Office(models.Model):
    titre_office = models.CharField(max_length=150)
    contenu_office = models.TextField(max_length=500)
    last_accessed = models.DateTimeField()

    def __str__(self):
        return self.titre_office


class Infographie(models.Model):
    title_info = models.CharField(max_length=150)
    contenu_info = models.TextField(max_length=500)
    last_accessed = models.DateTimeField()

    def __str__(self):
        return self.title_info


class English(models.Model):
    title_english = models.CharField(max_length=150)
    contenu_english = models.TextField(max_length=500)
    last_accessed = models.DateTimeField()

    def __str__(self):
        return self.title_english


class Programmation(models.Model):
    title_Programmation = models.CharField(max_length=150)
    contenu_Programmation = models.TextField(max_length=500)
    last_accessed = models.DateTimeField()

    def __str__(self):
        return self.title_Programmation


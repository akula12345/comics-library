from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Genre(models.Model):
    """
    Model representing a comic genre.
    """
    name = models.CharField(max_length=200, help_text="Enter a a comic genre.")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Comic(models.Model):
    """
    Model representing a comic.
    """
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the comic", null=True, blank=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this comic")
    year = models.DateField()

    COMPLETION_STATUS = (
    	('p', 'Published'),
    	('c', 'Complete')
    )

    status = models.CharField(max_length=1, choices=COMPLETION_STATUS, blank=True, default='c', help_text='Change the completion status of the comic.')


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular comic instance.
        """
        return reverse('comic-detail', args=[str(self.id)])


    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'


class Publisher(models.Model):
    """
    Model representing an publisher.
    """
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """
        Returns the url to access a particular publisher instance.
        """
        return reverse('publisher-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name





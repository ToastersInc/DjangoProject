from django.db import models

# Create your models here.
# a model is a class that represents a table in your database. each attribute of the class will be a column in the table.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio_images/")
    date_completed = models.DateField()

    def __str__(self):
        return self.title

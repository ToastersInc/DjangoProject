from django.db import models

# Create your models here.
# a model is a class that represents a table in your database. each attribute of the class will be a column in the table.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_completed = models.DateField()

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return f"Image for {self.project.title}"

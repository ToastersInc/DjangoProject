from django.contrib import admin

from .models import Project, ProjectImage

# Register your models here.
# add mutliple images on the project page
class ProjectImageInLine(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInLine]

admin.site.register(Project, ProjectAdmin)

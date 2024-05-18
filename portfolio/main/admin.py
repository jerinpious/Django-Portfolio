from django.contrib import admin
from .models import Tag,Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model= ProjectImage
    extra=1

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "link"
    ) # when wec are viewing the list of all the projects it is gonna show us in that list the title and the link for that project
    inlines = [ProjectImageInline]
    search_fields = ("title", "description") # this is specifying how we will be able to search for the project, so based on the title or the description
    list_filter = ("tags",) # so that we can filter them based on tags

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields =("name",)

admin.site.register(Tag,TagAdmin) # register the customization to the model
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
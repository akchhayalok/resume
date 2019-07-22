from django.contrib import admin
from .models import Blog
from django.db import models

class BlogAdmin(admin.ModelAdmin):
	"""docstring for BlogAdmin"""

fieldset = [("Name", {"fields": ["name"]}),
		("Email", {"fields":["email"]})	

	]


# Register your models here.
admin.site.register(Blog,BlogAdmin)

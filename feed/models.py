from django.db import models

# Create your models here.

class CategoriesMaster(models.Model):
	category = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'categories_master'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category
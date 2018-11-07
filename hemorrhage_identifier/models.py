from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator

# Create your models here.

class Hemorrhage(models.Model):
	ct_scan_image = models.FileField(null=True, help_text="upload jpg, jpeg, png files only", validators=[FileExtensionValidator(['jpg','png','jpeg'])])
	output = models.IntegerField(default=0)
	is_output_correct = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('')

	def __str__(self):
		return str(self.output)
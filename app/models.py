from django.db import models

# Create your models here.
class Contacts(models.Model):
    CLASS_CHOICES = [
        ('8th','8th'),
        ('9th','9th'),
        ('10th','10th'),
        ('11th','11th'),
        ('12th','12th'),
    ]    

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    student_class = models.CharField(
        max_length=10,
        choices=CLASS_CHOICES
    )

    subject = models.CharField(max_length=100)
    message = models.TextField()

    image = models.ImageField(
        upload_to='user/',
        blank=True,
        null=True
    )

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
from django.db import models

class Application(models.Model):
    CATEGORY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    STATUS_CHOICES = [
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
    ]
    
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    optional_courses = models.JSONField()  # Stores selected optional courses
    preferred_time = models.CharField(max_length=50, blank=True, null=True)
    motivation = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="applications/profile_pics/", blank=True, null=True)
    certificates = models.FileField(upload_to="applications/certificates/", blank=True, null=True)
    date_applied = models.DateTimeField(auto_now_add=True)
   
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.full_name

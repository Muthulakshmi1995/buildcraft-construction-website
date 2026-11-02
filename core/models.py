from django.db import models
from django.utils.text import slugify

class SiteSetting(models.Model):
    company_name = models.CharField(max_length=120, default="BuildCraft")
    tagline = models.CharField(max_length=220, default="Building dreams. Creating legacies.")
    phone = models.CharField(max_length=40, default="+91 98765 43210")
    email = models.EmailField(default="hello@buildcraft.example")
    address = models.CharField(max_length=250, default="Trivandrum, Kerala, India")
    about_text = models.TextField(blank=True, default="We create thoughtful spaces with quality craftsmanship.")
    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"
    def __str__(self): return self.company_name

class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=40, default="🏗️")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    def __str__(self): return self.title
    class Meta: ordering = ["order", "title"]

class Project(models.Model):
    title = models.CharField(max_length=160)
    category = models.CharField(max_length=100, default="Residential")
    location = models.CharField(max_length=160)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    image_url = models.URLField(blank=True)
    completion_year = models.PositiveIntegerField(default=2026)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
    class Meta: ordering = ["-created_at"]

class Property(models.Model):
    PROPERTY_TYPES = [("Villa","Villa"),("House","House"),("Apartment","Apartment"),("Commercial","Commercial")]
    STATUS = [("Sale","For Sale"),("Rent","For Rent")]
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, blank=True)
    property_type = models.CharField(max_length=30, choices=PROPERTY_TYPES, default="House")
    status = models.CharField(max_length=20, choices=STATUS, default="Sale")
    location = models.CharField(max_length=180)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    bedrooms = models.PositiveSmallIntegerField(default=3)
    bathrooms = models.PositiveSmallIntegerField(default=2)
    area_sqft = models.PositiveIntegerField(default=1500)
    description = models.TextField()
    image = models.ImageField(upload_to="properties/", blank=True, null=True)
    image_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title)[:45]
        super().save(*args, **kwargs)
    def __str__(self): return self.title
    class Meta: ordering = ["-featured", "-created_at"]

class Testimonial(models.Model):
    customer_name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.customer_name

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    subject = models.CharField(max_length=160, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} - {self.subject}"

class QuoteRequest(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    project_type = models.CharField(max_length=100)
    location = models.CharField(max_length=180, blank=True)
    budget = models.CharField(max_length=100, blank=True)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} - {self.project_type}"

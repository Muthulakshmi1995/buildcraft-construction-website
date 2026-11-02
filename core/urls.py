from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("projects/", views.projects, name="projects"),
    path("properties/", views.properties, name="properties"),
    path("properties/<slug:slug>/", views.property_detail, name="property_detail"),
    path("gallery/", views.gallery, name="gallery"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("contact/", views.contact, name="contact"),
    path("get-a-quote/", views.quote, name="quote"),
    path("chatbot/", views.chatbot, name="chatbot"),
]

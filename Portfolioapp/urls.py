from django.urls import path
from . import views
from .views import create_contact_api, list_contacts_api

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('api/contact/', create_contact_api, name='create-contact-api'),
    path('api/contacts/', list_contacts_api, name='list-contacts-api'),
    
]
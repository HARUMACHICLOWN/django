
from django.contrib import admin
from django.urls import path
from Samir import views

urlpatterns = [
    path('info', views.info, kwargs={"name": "Насибулин Самир Дамирович",
                                  "age":16,
                                  "interests":"программирование"}),
    path('about', views.about, kwargs={"city": "Kizner",
                                       "marks": "ударник",
                                       "learning": "нравится"}),
    path('contact', views.contact, kwargs={"github": "https://github.com/HARUMACHICLOWN",
                                           "telegram": "https://t.me/AsgerClown",
                                           "phone": "+79508363506"})
]

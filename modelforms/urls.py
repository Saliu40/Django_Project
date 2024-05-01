from django.urls import path
from . import views

urlpatterns = [
    path('enrol/', views.enrol, name='enrol'),  # This line maps the view function 'enrol' to the URL '/enrol/'
    # other URL patterns if any
]

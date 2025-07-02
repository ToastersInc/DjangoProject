from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact_view, name="contact"),
    path("contact/thank-you", views.thank_you_view, name="thank_you"),
    path("portfolio/", views.portfolio_view, name="portfolio"),
    path("portfolio/<int:pk>/", views.project_detail_view, name="project_detail"),
    path("services/", views.services_view, name="services"),
]

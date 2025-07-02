from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from .models import Project

# Create your views here.


def home(request):
    featured_projects = Project.objects.all().order_by("-date_completed")[:3]

    context = {"featured_projects": featured_projects}

    return render(request, "website/index.html", context)


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        phone = request.POST.get("phone")

        subject = f"New Inquiry from {name} via Earth in Finish Website"

        message_body = f"""
        You have received a new message from your website contact form.

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        send_mail(
            subject,
            message_body,
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )

        print(f"New Contact Form Submission")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        return redirect("thank_you")

    return render(request, "website/contact.html")


def thank_you_view(request):
    return render(request, "website/thank_you.html")


def portfolio_view(request):
    projects = Project.objects.all().order_by("-date_completed")

    context = {"projects": projects}

    return render(request, "website/portfolio.html", context)


def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)

    context = {"project": project}

    return render(request, "website/project_detail.html", context)


def services_view(request):
    return render(request, "website/services.html")

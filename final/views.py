from django.shortcuts import render, redirect
from app.models import Contacts
from django.core.mail import send_mail
from django.conf import settings
import threading

# ---------------- Background email functions ----------------
def send_student_email(name, email, student_class, subject):
    send_mail(
        subject="Thank you for contacting Bright Coaching",
        message=f"""
Hello {name},

Thank you for contacting Bright Coaching Classes.

We have received your inquiry.
Class: {student_class}
Subject: {subject}

Our team will contact you shortly.

Regards,
Bright Coaching Classes
""",
        from_email=settings.DEFAULT_FORM_EMAIL,
        recipient_list=[email],
        fail_silently=True,
    )

def send_admin_email(name, email, phone, student_class, subject, message):
    send_mail(
        subject="New Coaching Inquiry Received",
        message=f"""
New Inquiry Details:
Name: {name}
Email: {email}
Phone: {phone}
Class: {student_class}
Subject: {subject}
Message: {message}
""",
        from_email=settings.DEFAULT_FORM_EMAIL,
        recipient_list=['khannoushad2004@gmail.com'],  # ✅ Replace with your email
        fail_silently=True,
    )

# ---------------- Contact view ----------------
def contact(request):
    if request.method == "POST":
        # ---------------- Data fetch ----------------
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        student_class = request.POST.get('student_class')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        image = request.FILES.get('image')

        # ---------------- Simple validation ----------------
        if not (name and email and phone and student_class and subject and message):
            return render(request, "contact.html", {"error": "All fields are required."})

        # ---------------- Save to database ----------------
        Contacts.objects.create(
            name=name,
            email=email,
            phone=phone,
            student_class=student_class,
            subject=subject,
            message=message,
            image=image
        )

        # ---------------- Send emails in background ----------------
        threading.Thread(target=send_student_email, args=(name,email,student_class,subject)).start()
        threading.Thread(target=send_admin_email, args=(name,email,phone,student_class,subject,message)).start()

        # ---------------- Redirect fast ----------------
        return redirect('thankyou')

    return render(request, "contact.html")


# ---------------- Other views ----------------
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def service(request):
    return render(request, "service.html")

def thankyou(request):
    return render(request, "thankyou.html")

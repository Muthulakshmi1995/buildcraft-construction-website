import json
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.decorators.http import require_POST
from .models import Service, Project, Property, Testimonial
from .forms import ContactForm, QuoteForm

def home(request):
    return render(request, "core/home.html", {
        "services": Service.objects.filter(is_active=True)[:4],
        "projects": Project.objects.filter(featured=True)[:6],
        "testimonials": Testimonial.objects.filter(is_active=True)[:3],
    })

def about(request): return render(request, "core/about.html")
def services(request): return render(request, "core/services.html", {"services": Service.objects.filter(is_active=True)})
def projects(request):
    category = request.GET.get("category", "")
    qs = Project.objects.all()
    if category:
        qs = qs.filter(category=category)
    categories = Project.objects.order_by("category").values_list("category", flat=True).distinct()
    return render(request, "core/projects.html", {"projects": qs, "categories": categories, "selected_category": category})
def properties(request): return redirect("home")
def property_detail(request, slug): return redirect("home")
def gallery(request): return redirect("projects")
def testimonials(request): return redirect("home")
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(); messages.success(request, "Thank you! Your message has been sent."); return redirect("contact")
    return render(request, "core/contact.html", {"form": form})
def quote(request):
    form = QuoteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(); messages.success(request, "Your quotation request has been submitted."); return redirect("quote")
    return render(request, "core/quote.html", {"form": form})

@require_POST
def chatbot(request):
    """Rule-based BuildCraft assistant. Works without an OpenAI API key."""
    try:
        payload = json.loads(request.body.decode("utf-8"))
        question = payload.get("message", "").strip()[:1000]
    except Exception:
        return JsonResponse({"reply": "Please type your question and try again."}, status=400)
    if not question:
        return JsonResponse({"reply": "Please type a question."}, status=400)

    q = question.lower()
    if any(x in q for x in ["hi", "hello", "hey", "good morning", "good evening"]):
        answer = ("Welcome to BuildCraft. I can assist with our construction services, "
                  "project information and quotation enquiries. What would you like to know?")
    elif any(x in q for x in ["service", "what do you do", "provide", "construction type"]):
        answer = ("BuildCraft supports residential construction, commercial construction, "
                  "renovation and remodelling, architectural planning, interior works, and "
                  "building maintenance. Please visit the Services page to review each service, "
                  "or use Get a Quote to discuss the requirements for your project.")
    elif any(x in q for x in ["quote", "quotation", "estimate", "price", "cost", "budget", "rate"]):
        answer = ("We would be pleased to prepare a project-specific estimate. The cost depends "
                  "on the site location, built-up area, design, materials, specifications and "
                  "project timeline. Please submit the Get a Quote form with your name, contact "
                  "details and a short description of the work. Our team can then review your enquiry.")
    elif any(x in q for x in ["project", "portfolio", "completed work", "previous work", "work sample"]):
        answer = ("You can explore selected residential and commercial construction work on our "
                  "Projects page. Each project highlights a different approach to planning, "
                  "design and construction. For information about a specific project, please "
                  "send us an enquiry through the Contact page.")
    elif any(x in q for x in ["contact", "phone", "email", "address", "location", "reach"]):
        answer = ("Thank you for your interest in BuildCraft. Please visit the Contact page and "
                  "submit the enquiry form. You can also use the Get a Quote form if you would "
                  "like to discuss a new construction or renovation project.")
    elif any(x in q for x in ["time", "duration", "how long", "days", "months"]):
        answer = ("The project duration depends on the building size, design approvals, site "
                  "conditions, material selection and scope of work. Share your project details "
                  "through Get a Quote so the team can review a suitable timeline.")
    elif any(x in q for x in ["material", "cement", "steel", "quality"]):
        answer = ("Material selection is based on the project design, technical requirements "
                  "and the client's preferences. Please include your material or quality "
                  "requirements in the Get a Quote form so they can be discussed during planning.")
    else:
        answer = ("Thank you for contacting BuildCraft. I can help with three areas: our "
                  "construction services, our project portfolio, and quotation enquiries. "
                  "Please choose one of the options above or describe your construction "
                  "requirement. For other enquiries, our Contact page is the best place to start.")
    return JsonResponse({"reply": answer})

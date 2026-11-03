
import json
from google import genai
from openai import OpenAI
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
    try:
        payload = json.loads(request.body.decode("utf-8"))
        question = payload.get("message", "").strip()[:1000]

        if not question:
            return JsonResponse(
                {"reply": "Please type your question."},
                status=400
            )

        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question,
            config={
                "system_instruction": (
                    "You are BuildBot, the friendly AI assistant for "
                    "BuildCraft Construction Website. Answer naturally "
                    "and helpfully. You can answer general questions and "
                    "construction-related questions. For BuildCraft-specific "
                    "prices, contact details or project facts that are not "
                    "provided, do not invent information. Guide users to "
                    "the Contact or Get a Quote page. Keep answers simple "
                    "and clear."
                )
            }
        )

        answer = response.text
        return JsonResponse({"reply": answer})

    except Exception as error:
        import traceback
        traceback.print_exc()
        return JsonResponse({
            "reply": str(error)
        }, status=500)
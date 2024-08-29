import asyncio
import datetime

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import StudentForm


@require_http_methods(["GET", "POST"])
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new student record to the database
            return redirect(
                reverse("success")
            )  # Redirect to the success page using URL name
    else:
        form = StudentForm()

    return render(request, "create_student.html", {"form": form})


def success(request):
    return render(request, "success.html")


def my_html_view(request):
    html = "<html><body><h1>Hey, it's David</h1><p>Wait for 10 seconds...</p></body></html>"
    return HttpResponse(html)


async def my_async_view(request):

    await asyncio.sleep(10)
    return JsonResponse({"message": "Hello, async world!"})


def custom_404_view(request, exception):
    return HttpResponseNotFound("<h1>This Page not found</h1>")

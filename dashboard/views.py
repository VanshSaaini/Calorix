from django.shortcuts import render
import json 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from home.models import UserStats
from django.utils.timezone import now
from datetime import timedelta
from django.db.models.functions import TruncDay, TruncMonth, TruncYear
from django.db.models import Avg


@login_required
def chart_data(request):
    qs = UserStats.objects.filter(user=request.user)

    start = request.GET.get("start")
    end = request.GET.get("end")

    if start and end:
        qs = qs.filter(date__date__range=[start, end])

    qs = qs.order_by("date")

    labels = [d.date.strftime("%d %b") for d in qs]

    return JsonResponse({
        "labels": labels,
        "weight": [d.weight for d in qs],
        "bmi": [d.bmi for d in qs],
        "bmr": [d.bmr for d in qs],
        "calories": [d.bmr for d in qs],
    })

@login_required
def update_stats(request):
    if request.method == "POST":
        data = json.loads(request.body)

        weight = float(data.get("weight"))
        height = float(data.get("height_cm"))

        height_m = height / 100
        bmi = weight / (height_m ** 2)
        bmr = (10 * weight) + (6.25 * height) - (5 * 20) + 5

        UserStats.objects.create(
            user=request.user,
            weight=weight,
            height_cm=height,
            bmi=round(bmi, 2),
            bmr=round(bmr, 2)
        )

        return JsonResponse({"status": "success"})


# ✅ DASHBOARD VIEW
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
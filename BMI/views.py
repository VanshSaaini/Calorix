from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import UserStats


def calculate_bmi(weight, weight_unit, height_cm):
    """Return rounded BMI value."""
    weight    = float(weight)
    height_cm = float(height_cm)

    # Convert lbs → kg
    if weight_unit == "lbs":
        weight *= 0.453592

    height_m = height_cm / 100
    bmi      = weight / (height_m ** 2)
    return round(bmi, 1)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def bmi_advice(category):
    advice = {
        "Underweight": (
            "You are below the healthy weight range. Focus on nutrient-dense foods "
            "and consult a healthcare professional."
        ),
        "Normal": (
            "You are within a healthy BMI range. Keep up a balanced diet and regular exercise."
        ),
        "Overweight": (
            "You are slightly above the healthy range. A modest calorie deficit and "
            "increased activity can help."
        ),
        "Obese": (
            "Your BMI indicates obesity. Please consult a doctor or registered dietitian "
            "for a personalised plan."
        ),
    }
    return advice.get(category, "")


@login_required
def bmi(request):
    context = {}

    if request.method == "POST":
        weight      = request.POST.get('weight', '')
        weight_unit = request.POST.get('weight_unit', 'kg')
        height_cm   = request.POST.get('height_cm', '')
        height_ft   = request.POST.get('height_ft', '')
        height_in   = request.POST.get('height_in', '')
        height_unit = request.POST.get('height_unit', 'cm')

        # Convert ft/in → cm
        if height_unit == 'in':
            try:
                ft   = float(height_ft or 0)
                inch = float(height_in or 0)
                height_cm = (ft * 12 + inch) * 2.54
            except (TypeError, ValueError):
                height_cm = None

        # Validate
        try:
            weight    = float(weight)
            height_cm = float(height_cm)
        except (TypeError, ValueError):
            messages.error(request, "Invalid input — please enter valid numbers.")
            return redirect('BMI')

        if weight <= 0 or height_cm <= 0:
            messages.error(request, "Weight and height must be positive values.")
            return redirect('BMI')

        bmi_value = calculate_bmi(weight, weight_unit, height_cm)
        category  = bmi_category(bmi_value)

        # Optionally save to UserStats
        UserStats.objects.filter(user=request.user).create(
              user=request.user,
              weight=weight,
              weight_unit=weight_unit,
              height_cm=height_cm,
              bmi=bmi_value
        )

        context = {
            'bmi':      bmi_value,
            'category': category,
            'advice':   bmi_advice(category),
            'form_data': {
                'weight':      weight,
                'weight_unit': weight_unit,
                'height_cm':   height_cm,
                'height_unit': height_unit,
            }
        }

    return render(request, 'bmi.html', context)
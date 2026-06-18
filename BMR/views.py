from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import UserStats
from django.contrib import messages


# 🔹 Activity multipliers
ACTIVITY_MULTIPLIERS = {
    1.2:   1.2,
    1.375: 1.375,
    1.55:  1.55,
    1.725: 1.725,
    1.9:   1.9,
}


# 🔹 BMR + TDEE Calculation
def calculate_bmr(gender, weight, height_cm, age, activity_multiplier, weight_unit):
    weight = float(weight)
    height_cm = float(height_cm)
    age = int(age)

    # Convert lbs → kg
    if weight_unit == "lbs":
        weight *= 0.45359237

    if gender.lower() == "male":
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

    tdee = bmr * activity_multiplier
    return bmr, tdee


# 🔹 Advice
def bmr_advice(bmr):
    if bmr < 1200:
        return "Your BMR is very low. Focus on improving nutrition and strength training."
    elif bmr < 1600:
        return "Your BMR is below average. Maintain a balanced diet and regular activity."
    elif bmr < 2000:
        return "Your BMR is in a healthy range. Keep up your current lifestyle."
    elif bmr < 2500:
        return "Your BMR is good. Ensure proper calorie intake and stay active."
    else:
        return "Your BMR is high — likely due to high muscle mass or intense activity."


# 🔥 MAIN VIEW
@login_required
def bmr(request):
    context = {}

    if request.method == "POST":
        try:
            gender = request.POST.get('gender', 'male')
            age = int(request.POST.get('age'))
            weight = float(request.POST.get('weight'))
            weight_unit = request.POST.get('weight_unit', 'kg')
            activity = float(request.POST.get('activity'))
            height_unit = request.POST.get('height_unit', 'cm')

            height_cm = request.POST.get('height_cm')
            height_ft = request.POST.get('height_ft', '')
            height_in = request.POST.get('height_in', '')

            # 🔹 Convert height if needed
            if height_unit == 'in':
                ft = float(height_ft or 0)
                inch = float(height_in or 0)
                height_cm = (ft * 12 + inch) * 2.54

            height_cm = float(height_cm)

            # 🔹 Validation
            if age < 10 or age > 100:
                messages.error(request, "Age must be between 10 and 100.")
                return redirect('BMR')

            if weight <= 0 or height_cm <= 0:
                messages.error(request, "Weight and height must be positive.")
                return redirect('BMR')

            # 🔥 STEP 1: CALCULATE FIRST
            bmr_value, tdee_value = calculate_bmr(
                gender, weight, height_cm, age, activity, weight_unit
            )

            # 🔥 STEP 2: SAVE TO DB (IMPORTANT → CREATE, NOT UPDATE)
            stats = UserStats.objects.create(
                user=request.user,
                gender=gender,
                age=age,
                weight=weight,
                weight_unit=weight_unit,
                height_cm=height_cm,
                activity=str(activity),
                bmr=round(bmr_value, 2),
            )

            # 🔥 STEP 3: SEND TO TEMPLATE
            context = {
                'BMR': round(bmr_value, 2),
                'TDEE': round(tdee_value, 2),
                'TDEE_minus': round(tdee_value - 500, 2),
                'TDEE_plus': round(tdee_value + 300, 2),
                'advice': bmr_advice(bmr_value),
                'user_stats': stats,
                'form_data': {
                    'gender': gender,
                    'age': age,
                    'weight': weight,
                    'weight_unit': weight_unit,
                    'height_cm': height_cm,
                    'height_unit': height_unit,
                    'activity': str(activity),
                }
            }

        except Exception as e:
            messages.error(request, "Invalid input. Please enter correct values.")
            return redirect('BMR')

    return render(request, 'bmr.html', context)
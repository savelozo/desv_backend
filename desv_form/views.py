from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EvaluateForm
import json

@csrf_exempt
def submit_data_view(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode) 

        # Crea una instancia del modelo EvaluateForm y guarda los datos
        evaluate_form = EvaluateForm(
            name=body_data.get('firstName', ''),
            last_name=body_data.get('lastName', ''),
            email=body_data.get('email', ''),
            date_of_birth=body_data.get('birthdate', ''),
            nationality=body_data.get('nationality', ''),
            address=body_data.get('address', ''),
            education_level=body_data.get('educationLevel', ''),
            employment_status=body_data.get('employmentStatus', ''),
            industry_type=body_data.get('industry', ''),
            #monthly_income=body_data.get('incomeLevel', '')
        )

        # Guarda la instancia del modelo en la base de datos
        evaluate_form.save()

        # Devuelve una respuesta exitosa
        return JsonResponse({'message': 'Datos guardados con éxito'}, status=200)

    # Maneja otros métodos HTTP si es necesario
    return JsonResponse({'message': 'Método no permitido'}, status=405)


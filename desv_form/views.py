from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def submit_data(request):
    print("Request: {}".format(request.method))
    if request.method == 'POST':
        data = json.loads(request.body)
        # Aquí puedes procesar los datos y guardarlos en la base de datos
        # por ejemplo: nombre = data['firstName'], apellido = data['lastName'], etc.
        # Realiza las operaciones necesarias y devuelve una respuesta
        response_data = {'message': 'Datos recibidos con éxito'}
        return JsonResponse(response_data)


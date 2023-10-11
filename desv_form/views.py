from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def submit_data_view(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)    
        # Obtén los datos del formulario
        # Procesa y almacena los datos según tus necesidades
        # ...

        # Devuelve una respuesta al cliente
        response_data = {'message': 'Datos recibidos exitosamente'}
        return JsonResponse(response_data)

    # Maneja otros métodos HTTP si es necesario
    return JsonResponse({'message': 'Método no permitido'}, status=405)


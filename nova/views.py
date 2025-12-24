from django.http import JsonResponse
from .models import NovaBlock

def blocks_api(request, pk):
    blocks = NovaBlock.objects.filter(page_id=pk).values()
    return JsonResponse(list(blocks), safe=False)


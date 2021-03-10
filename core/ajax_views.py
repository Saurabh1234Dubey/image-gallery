from django.http import JsonResponse
from .models import Media
from .utils import GetDict

def GetImage(request):
    data = request.POST.getlist('cat[]')
    if data:
        data_list = [int(i) for i in data] 
        filter_image = Media.objects.filter(category__id__in=data_list)
    else:
        filter_image = Media.objects.all().order_by('-created_at')
    data = GetDict(filter_image)
    
    return JsonResponse(data, safe=False)
from django.http import JsonResponse
from .models import Media
from .utils import GetDict

def GetImage(request):
    data = request.POST.getlist('cat[]')
    print(data)
    data_list = [int(i) for i in data] 
    filter_image = Media.objects.filter(category__id__in=data_list)
    data = GetDict(filter_image)
    
    return JsonResponse(data, safe=False)
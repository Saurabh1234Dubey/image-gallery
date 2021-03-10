from django.shortcuts import render, redirect
from .models import Media, Category
from django.views import View
from .utils import GetContext
# Create your views here.

def Index(request):
    '''
    To view all image
    '''
    media = Media.objects.all().order_by('-created_at')
    context = GetContext()
    context.update({'media':media, 'page':"home"})
    return render(request,'image-gellery.html.j2',context)

class ImageUploadView(View):
    '''
    To uplaod image
    '''
    def get(self, request):
        context = GetContext()
        return render(request,'upload-image.html.j2', context)

    def post(self, request):
        data = request.POST
        files = request.FILES
        data = {
            'title':data.get('title'),
            'category_id':data.get('category'),
            'image':files.get('image')
        }
        Media.objects.create(**data)
        return redirect('index')

class AddCategoryView(View):
    '''
    To add category
    '''
    def get(self, request):
        context = GetContext()
        return render(request,'add-category.html.j2', context)

    def post(self, request):
        data = request.POST
        Category.objects.create(name=data.get('name'))
        return redirect('image_upload')



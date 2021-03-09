from .models import Category

def GetContext():
    '''
    Get context for tamplate
    '''
    context = {
        'category':Category.objects.all() # need category on almost every page
    }
    return context

def GetDict(queryset):
    """
    return queryset dict
    """
    data = []
    if queryset:
        for q in queryset:
            x = dict()
            x['id'] = q.id
            x['title'] = q.title
            x['image'] = str(q.image.url) if q.image else None
            x['category'] = q.category.name
            data.append(x)
    return data
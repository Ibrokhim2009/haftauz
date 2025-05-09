from app1.models import Category,New

def main(request):
    categories = Category.objects.filter(is_menu=True)
    svejiy = New.objects.all().order_by('-id')[:8]
    return {
        'categories':categories,
        'svejiy': svejiy
    }
    
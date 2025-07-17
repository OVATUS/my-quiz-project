from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def home(request):
   return render(request,'p.html')

def question(request):
    n1 = request.GET['name11']
    n2 = request.GET['name22']
    n3 = request.GET['name33']
    return JsonResponse({'id': n1, 'text': n2, 'choices': n3})
    
        #"id" :1 ,
        #"text": "ประเทศมีกี่จังหวัด" ,
        #"choices" :[50 , 68 ,72, 77]

    


def create_question(request):
   if request.method == 'POST':
    n1 = request.POST['name1']
    n2 = request.POST['name2']
    n3 = request.POST['name3']
    return JsonResponse({'id': n1, 'text': n2, 'choices': n3})
   else:
    return HttpResponse('sssss')



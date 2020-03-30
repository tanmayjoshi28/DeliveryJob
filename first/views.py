from .models import Areawise, Person
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import Operator_required, Manager_required

@login_required
@Manager_required
def Display_detail(request, area_id):
    p_detail = Person.objects.filter(areawise=area_id)
    n_area = get_object_or_404(Areawise, pk=area_id)
    context = {
        'objects_list': p_detail,
        'Area': n_area
    }
    return render(request, 'first/p_detail.html', context)

@login_required
@Operator_required
def inputperson(request, area_id):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('vno') and request.POST.get('phno'):
            area = get_object_or_404(Areawise, pk=area_id)
            p = Person()
            p.areawise = area
            p.p_name = request.POST.get('name')
            p.vehicle = request.POST.get('vno')
            p.phone_no = request.POST.get('phno')
            p.save()
            all_areawise = Areawise.objects.all()
            return render(request, 'first/template.html', {'all_areawise': all_areawise})
        else:
            raise Http404("FIELD INCOMPLETE")

@login_required
@Operator_required
def detail(request, area_id):
    area = get_object_or_404(Areawise, pk=area_id)
    return render(request, 'first/detail.html', {'area': area})

@login_required
@Operator_required
def index(request):
    all_areawise = Areawise.objects.all()
    return render(request, 'first/template.html', {'all_areawise': all_areawise})


@login_required
@Manager_required
def personindex(request):
    all_areawise = Areawise.objects.all()
    return render(request, 'first/AreadetailforP.html', {'all_areawise': all_areawise})


def home_view(request):
    return render(request, 'first/homepage.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ContactForm, StrokeForm
from .ml_model import logic_layer
from django.contrib import messages
# from django.template.loader import get_template
# from xhtml2pdf import pisa

from django.core.files.storage import FileSystemStorage

# Create your views here.
res = None

def index(request):
    return render(request=request, 
                  template_name='main/index1.html')

def predict(request):
    return render(request=request, 
                  template_name='main/predict.html', context={"stroke": res})


def index2(request):
    if request.method == 'POST':
        form = StrokeForm(request.POST)
        
        if form.is_valid():

            age = form.cleaned_data['age'] * 365
            gender =  int(form.cleaned_data['gender'])
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            ap_hi = form.cleaned_data['ap_hi']
            ap_lo = form.cleaned_data['ap_lo']            
            cholesterol =  int(form.cleaned_data['cholesterol'])
            gluc =  int(form.cleaned_data['gluc'])
            smoke =  int(form.cleaned_data['smoke'])
            alco =  int(form.cleaned_data['alco'])
            active =  int(form.cleaned_data['active'])
            
            x = [age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]
            global res
            res = logic_layer(x)
            return redirect("/predict")
        else:
            problem = form.errors.as_data()
            # This section is used to handle invalid data 
            messages.error(request, list(list(problem.values())[0][0])[0])
            form = StrokeForm()
    form = StrokeForm()
    return render(request=request, template_name='main/index2.html', context={"form": form})


def about(request):
    return render(request=request, 
            template_name="main/about.html")


def under_construction(request):
    messages.info(request, "This page coming soon..")
    return render(request=request, 
            template_name="main/under_construction.html")

def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'mypdf.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' #user will be prompted with the browser’s open/save file
            response['Content-Disposition'] = 'filename="mypdf.pdf"' #user will be prompted display the PDF in the browser
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
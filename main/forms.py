from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
# from django.forms import extras

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

GENDER_CHOICES =[
    ('0', 'select gender'),
    ('1', 'female'),
    ('2', 'male')
]

CHOLESTEROL_CHOICES =[
    ('0', 'What is your Cholesterol level ?'),
    ('1', 'Normal'),
    ('2', 'Above Normal'),
    ('3', 'Well Above Normal')
]

GLUC_CHOICES =[
    ('0', 'What is your Glucose level ?'),
    ('1', 'Normal'),
    ('2', 'Above Normal'),
    ('3', 'Well Above Normal')
]

SMOKE_CHOICES = [
    ('3', 'Do you Smoke ?'),
    ('0', 'yes'),
    ('1', 'no')
]

ALCO_CHOICES = [
    ('3', 'Do you consume Alcohol ?'),
    ('0', 'yes'),
    ('1', 'no')
]

ACTIVE_CHOICES = [
    ('3', 'Are you physically active ?'),
    ('0', 'yes'),
    ('1', 'no')
]

class StrokeForm(forms.Form):
    age = forms.IntegerField(label="Age", 
                              validators=[MinValueValidator(1, message="Year is invalid!"), 
                              MaxValueValidator(100, message="Please Check Age")])

    height = forms.IntegerField(label="Height", 
                                validators=[MinValueValidator(90, message="Are sure about your height in cm ? "), 
                              MaxValueValidator(225, message="Are sure you are that high ?")])

    weight = forms.IntegerField(label="Weight",
                                validators=[MinValueValidator(25, message="Are you that light ? "), 
                              MaxValueValidator(200, message="Are you that heavy ? ")])

    ap_hi = forms.IntegerField(label="Systolic Blood Pressure",
                                validators=[MinValueValidator(0, message="Enter valid value"), 
                              MaxValueValidator(500, message="Please call Ambulance right NOW")])

    ap_lo = forms.IntegerField(label="Diastolic Blood Pressure",
                                validators=[MinValueValidator(0, message="Enter valid value"), 
                              MaxValueValidator(500, message="Please call Ambulance right NOW")])   
    gender = forms.CharField(label="Gender", widget=forms.Select(choices=GENDER_CHOICES))
    cholesterol = forms.CharField(label="cholesterol", widget=forms.Select(choices=CHOLESTEROL_CHOICES))
    gluc = forms.CharField(label="gluc", widget=forms.Select(choices=GLUC_CHOICES))
    smoke = forms.CharField(label="smoke", widget=forms.Select(choices=SMOKE_CHOICES))
    alco = forms.CharField(label="alco", widget=forms.Select(choices=ALCO_CHOICES))
    active = forms.CharField(label="active", widget=forms.Select(choices=ACTIVE_CHOICES))
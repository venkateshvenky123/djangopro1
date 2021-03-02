from django import forms
from .models import productdata
class Insertingdata(forms.Form):
    product_id=forms.IntegerField(
        label="enter your product_id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your id'
            }
        )
    )
    product_name = forms.CharField(
        label="enter your product_name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your  product name'
            }
        )
    )
    product_class = forms.CharField(
        label="enter your product_class",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product class'
            }
        )
    )
    product_color = forms.CharField(
        label="enter your product_color",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product color'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="enter your product_cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your cost'
            }
        )
    )
class updatingdata(forms.Form):
    product_id = forms.IntegerField(
        label="enter your product_id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your id'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="enter your product_cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product cost'
            }
        )
    )
class deletingdata(forms.Form):
    product_id = forms.IntegerField(
        label="enter your product_id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product id'
            }
        )
    )


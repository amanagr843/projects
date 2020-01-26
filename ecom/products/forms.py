from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta():
        model = Products
        fields = [
            'name',
            'description',
            'price'
        ]
class Product_raw(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs={"placeholder" : "Product Name"}))
    description = forms.CharField(
                        required = False,
                        widget  = forms.Textarea(
                                        attrs = {
                                        "placeholder" : "Product description",
                                        "class" : "new-class",
                                        "rows" : 15,
                                        "cols" : 150
                                        }
                        )
    )
    price = forms.CharField()

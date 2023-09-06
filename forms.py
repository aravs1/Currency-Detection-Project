from django import forms


class ImageForm(forms.Form):
    # file = forms.ImageField(label='Image')
    file = forms.FileField(label='',
       widget=forms.FileInput(attrs={'accept': 'image/*', 'capture':'camera', 'style':'width:970px; height:550px;font-size:20px;'})
    )

    #background-color:black;
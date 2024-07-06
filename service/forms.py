from django import forms

class MultiplePhotoForm(forms.Form):
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'custom-file-input'}),
        label="Выбрать изображения",
        required=False,
        label_suffix=''
    )

    def __init__(self, *args, **kwargs):
        super(MultiplePhotoForm, self).__init__(*args, **kwargs)
        self.fields['images'].label_class = "custom-label-class"
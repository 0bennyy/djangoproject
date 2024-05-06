from django.forms.formsets.BaseFormSet import forms


class Meta:
    class ModelName(models.Model):
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model =
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
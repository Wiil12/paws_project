from django import forms
 
class AddPetForm(forms.Form):
    petName = forms.CharField(label='Pet Name', max_length=255, required=True)
    petAge = forms.IntegerField(label='Pet Age', required=True)
    petBreed = forms.CharField(label='Pet Breed', max_length=255, required=True)
    petImage = forms.CharField(label='Pet Image URL', max_length=500, required=False)
 
 
 
class BlogForm(forms.Form):
     title = forms.CharField(label='Title', max_length=(255), required=True)
     content = forms.CharField(label='Content',widget=forms.Textarea, required=True)
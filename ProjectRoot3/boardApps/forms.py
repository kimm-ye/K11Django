from django import forms

class WriteForm(forms.Form):
    
    my_name = forms.CharField(label='작성자',  widget=forms.TextInput(attrs={'class': 'form-control w100'}))
    my_pw = forms.CharField(label='패스워드', widget=forms.TextInput(attrs={'class': 'form-control w200'}))
    my_titles = forms.CharField(label='제목', widget=forms.TextInput(attrs={'class': 'form-control'}))
    my_contents = forms.CharField(label='내용', widget=forms.Textarea(attrs={'class': 'form-control'}))
    my_file = forms.FileField(label='첨부파일',  widget=forms.FileInput(attrs={'class':'form-control'}), required=False)



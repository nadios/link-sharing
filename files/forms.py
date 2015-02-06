from django import forms

""" Simple user form for file upload"""


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Select a file'
    )
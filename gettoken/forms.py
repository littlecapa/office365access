from django import forms

#
# https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
#

class OauthForm(forms.Form):
    client_id = forms.CharField(help_text="Enter Client ID", required = True, label = "Client-ID", max_length=128)
    secret = forms.CharField(help_text="Enter Secret", required = True, label = "Secret")

class AccessForm(forms.Form):
    access_token = forms.CharField(required = True, label = "Access Token")
    refresh_token = forms.CharField(required = True, label = "Refresh Token")
    json = forms.CharField(required = True, label = "Json Str")

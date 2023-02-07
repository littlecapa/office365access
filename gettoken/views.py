from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.http.response import JsonResponse, HttpResponse

from .onedrive_lib import onedriveAccess

myOnedrive = onedriveAccess()

from .forms import OauthForm, AccessForm

# Create your views here.

def ssoCallback(request):
    if request.method == 'GET':
        myOnedrive.setTokenFromRequest(request)
        response = redirect('/gettoken/result/')
        return response
    return HttpResponse(request)

def inputOauth(request):
    if request.method == 'POST':
        form = OauthForm(request.POST)
        if form.is_valid():
            client_id = form.cleaned_data['client_id']
            secret = form.cleaned_data['secret']
            myOnedrive.setIds(clientId = client_id, secret = secret)
            print(myOnedrive.getAuthUrl())
            return HttpResponseRedirect(myOnedrive.getAuthUrl())
    form = OauthForm(initial={'secret': '<secret>', 'client_id': '<client_id>'})
    return render(request, 'oauth.html', {'form': form})   

def result(request):
    access_token, refresh_token = myOnedrive.getToken()
    json_str = "{'access_token: '" + access_token + "', refresh_token: '" + refresh_token + "',}'"
    print(json_str)
    form = AccessForm(initial={'access_token': access_token, 
                                'refresh_token': refresh_token,
                                'json': json_str})
    return render(request, 'token.html', {'form': form}) 

@api_view(['GET'])
def health(request):
    return JsonResponse({'Health': 'Service is healthy'})

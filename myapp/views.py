from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
import requests
from django.conf import settings  # Import Django settings
from .models import SalesforceToken

def login_with_salesforce(request):
    # Construct the OAuth URL
    oauth_url = f'{settings.SALESFORCE_AUTH_URL}?client_id={settings.SALESFORCE_CLIENT_ID}&' \
                f'response_type=code&redirect_uri={settings.SALESFORCE_REDIRECT_URI}'

    return redirect(oauth_url)

def oauth_callback(request):
    # Get the authorization code from the query parameters
    code = request.GET.get('code')

    # Prepare data for token exchange
    data = {
        'grant_type': 'authorization_code',
        'client_id': settings.SALESFORCE_CLIENT_ID,
        'client_secret': settings.SALESFORCE_CLIENT_SECRET,
        'code': code,
        'redirect_uri': settings.SALESFORCE_REDIRECT_URI,
    }

    # Request the access token from Salesforce
    response = requests.post(settings.SALESFORCE_TOKEN_URL, data=data)

    if response.status_code == 200:
        # Successful authentication, parse the JSON response
        auth_data = response.json()
        access_token = auth_data['access_token']
        instance_url = auth_data['instance_url']
        refresh_token = auth_data['refresh_token']

        # Store access_token and instance_url in your app's database if needed
        salesforce_token = SalesforceToken(
            access_token=access_token,
            instance_url=instance_url
        )
        salesforce_token.save()
        return render(request, 'welcome_to_mavlon.html')
    else:
        # Handle authentication error
        return redirect('login_with_salesforce')
    
from django.contrib.auth.decorators import login_required

# @login_required
def welcome(request):
    return render(request, 'login_with_salesforce.html')
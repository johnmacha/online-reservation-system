from django.http import HttpResponse
import requests
# from .forms5 import MpesaForm
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth
from .models import MpesaPay
import json
from datetime import datetime
from .credentials import MpesaAccessToken, LipanaMpesaPpassword, MpesaC2bCredential
import base64
#from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword


def getAccessToken():
    consumer_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
    consumer_secret = '2nHEyWSD4VjpNh2g'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return (validated_mpesa_access_token)


def lipa_na_mpesa_online(request,amount, phone):
    current_time = datetime.now()
    access_token = getAccessToken()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token, "Content-Type": "application/json"}
    request = {
        "BusinessShortCode": 174379,
        "Password":LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": phone,  # replace with your phone number to get stk push
        "PartyB": 174379,
        "PhoneNumber": phone,  # replace with your phone number to get stk push
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "SPORTSVIEW",
        "TransactionDesc": "Testing hotel payment"
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)
    return HttpResponse("Success")

def lipa(request):
 print(request.POST)
 if request.method == 'POST':
    first_name = request.POST.get("first_name")
    second_name = request.POST.get("second_number")
    #date_of_payment = request.POST.get("date_of_payment")
    amount= request.POST.get("amount")
    phone_number = request.POST.get('phone_number')

    lipa_na_mpesa_online(request, amount,phone_number)
    mpesa_pay = MpesaPay(first_name=first_name, second_name=second_name,
    amount=int(amount)) #, date_of_payment=date_of_payment
    mpesa_pay.save()
        
    # try:
    #
    # except:
    #     print("Transaction failed")

 return render(request,'mpesa.html')
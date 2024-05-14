from django.shortcuts import render
import requests
from .models import ExchangeRates
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


# EXR_API_KEY = 'ju30rWSTYJlFvOI87uL68kfv8BMN9f5V'
EXR_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXR_API_KEY}&data=AP01'

@api_view(['GET'])
def get_exchange_rates(request):
  response = requests.get(EXR_API_URL).json()
  
  print(response)
  return Response(response)
from django.shortcuts import render
import requests
from .models import ExchangeRates
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
from .serializers import ExchangeRatesSerializer
from rest_framework import status


@api_view(['GET'])
def get_exchange_rates(request):
  SEARCH_DATE = datetime.date.today()
  EXR_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXR_API_KEY}&searchdate={SEARCH_DATE}&data=AP01'
  response = requests.get(EXR_API_URL).json()
  
  if not response:
    while not response:
      SEARCH_DATE -= datetime.timedelta(days=1)
      EXR_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXR_API_KEY}&searchdate={SEARCH_DATE}&data=AP01'
      response = requests.get(EXR_API_URL).json()
  
  for rate in response:
      # 쉼표 제거 후 float 변환
      rate['deal_bas_r'] = float(rate['deal_bas_r'].replace(',', ''))
      rate['ttb'] = float(rate['ttb'].replace(',', ''))
      rate['tts'] = float(rate['tts'].replace(',', ''))

  context = {
    'exchange_rates': response,
    'search_date' : SEARCH_DATE.strftime('%Y-%m-%d')
  }
  serializer = ExchangeRatesSerializer(data=context['exchange_rates'], many=True)
  if serializer.is_valid():
    # Delete existing data
    ExchangeRates.objects.all().delete()
    # Save new data
    serializer.save()

    return Response({'exchange_rates':serializer.data,
                     'search_date':context['search_date']}, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
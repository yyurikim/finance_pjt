from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from .serializers import DepositSerializers, DepositOptionsSerializers, SavingSerializers, SavingOptionsSerializers, UserDepositSerializers, UserSavingsSerializers
from .models import Deposit, Deposit_options, Saving, Saving_option, UserDeposit, UserSavings
from django.db.models import Max
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
def index(request) :
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    return JsonResponse(response)

def indexx(request) :
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    return JsonResponse(response)

def save_deposit_products(request) :
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # 확인
    for item in response['result']['baseList']:
        fin_prdt_cd = item['fin_prdt_cd']
        kor_co_nm = item['kor_co_nm']
        fin_prdt_nm = item['fin_prdt_nm']
        spcl_cnd = item['spcl_cnd']
        join_deny = item['join_deny']
        join_way = item['join_way']
        etc_note = item['etc_note']

        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'spcl_cnd' : spcl_cnd,
            'join_deny' : join_deny,
            'join_way' : join_way,
            'etc_note' : etc_note,
        }

        serializer = DepositSerializers(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True) :
            # 유효하다면 저장
            serializer.save()

    for item in response['result']['optionList']:
        fin_prdt_cd = item['fin_prdt_cd']
        intr_rate_type_nm = item['intr_rate_type_nm']
        save_trm = item['save_trm']
        intr_rate = item.get('intr_rate', -1)
        intr_rate2 = item.get('intr_rate2', -1)

        product = get_object_or_404(Deposit, fin_prdt_cd=fin_prdt_cd)

        save_data = {
            'deposit_product_id': product.pk,  # 외래 키 필드에는 객체를 직접 할당
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'save_trm': save_trm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
        }

        serializer = DepositOptionsSerializers(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면 저장
            serializer.save()

    return JsonResponse({"message": "save_okay!"})



def save_saving_products(request) :
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # 확인
    for item in response['result']['baseList']:
        fin_prdt_cd = item['fin_prdt_cd']
        kor_co_nm = item['kor_co_nm']
        fin_prdt_nm = item['fin_prdt_nm']
        mtrt_int = item['mtrt_int']
        spcl_cnd = item['spcl_cnd']
        join_deny = item['join_deny']
        etc_note = item['etc_note']

        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'spcl_cnd' : spcl_cnd,
            'join_deny' : join_deny,
            'mtrt_int' : mtrt_int,
            'etc_note' : etc_note,
        }
        
        serializer = SavingSerializers(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True) :
            # 유효하다면 저장
            serializer.save()
        

    for item in response['result']['optionList']:
        fin_prdt_cd = item['fin_prdt_cd']
        intr_rate_type_nm = item['intr_rate_type_nm']
        save_trm = item['save_trm']
        intr_rate_type_nm = item['intr_rate_type_nm']
        rsrv_type_nm = item['rsrv_type_nm']
        intr_rate = item.get('intr_rate', -1)
        intr_rate2 = item.get('intr_rate2', -1)

        product = get_object_or_404(Saving, fin_prdt_cd=fin_prdt_cd)

        save_data = {
            'saving_product_id': product.pk,  # 외래 키 필드에는 객체를 직접 할당
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'save_trm': save_trm,
            'rsrv_type_nm': rsrv_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
        }

        serializer = SavingOptionsSerializers(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면 저장
            serializer.save()

    return JsonResponse({"message": "save_okay!"})




@api_view(['GET', 'POST'])
def deposit_products(request) :
    if request.method == 'GET' :
        products = Deposit.objects.all()
        serializers = DepositSerializers(products, many=True)
        return Response(serializers.data)
    elif request.method == 'POST' :
        serializers = DepositSerializers(data = request.data)
        if serializers.is_valid() :
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response({'message':'이미 있는 데이터이거나, 데이터가 잘못 입력됐습니다.'})
    

@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd) :
    product = Deposit_options.objects.filter(fin_prdt_cd = fin_prdt_cd)
    serializers = DepositOptionsSerializers(product, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def top_rate(request) :
    top_rate = Deposit_options.objects.aggregate(max_intr_rate2=Max('intr_rate2'))
    max_intr_rate2 = top_rate['max_intr_rate2']

    top_option = Deposit_options.objects.filter(intr_rate2=max_intr_rate2).first()
    product_serializer = DepositSerializers(top_option.product)
    option_serializer  = DepositOptionsSerializers(top_option)
    
    response_data = {
        'deposit_product': product_serializer.data,
        'options': option_serializer.data,
    }

    return Response(response_data)
    

class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializers

class DepositOptionsViewSet(viewsets.ModelViewSet):
    queryset = Deposit_options.objects.all()
    serializer_class = DepositOptionsSerializers

class SavingViewSet(viewsets.ModelViewSet):
    queryset = Saving.objects.all()
    serializer_class = SavingSerializers

class SavingOptionsViewSet(viewsets.ModelViewSet):
    queryset = Saving_option.objects.all()
    serializer_class = SavingOptionsSerializers


@api_view(['GET', 'POST', 'DELETE'])
def user_deposit(request):
    user = request.user
    user_deposits = UserDeposit.objects.filter(user=user)
    serializer = UserDepositSerializers(user_deposits, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'DELETE'])
def user_savings(request):
    user = request.user
    user_savings = UserSavings.objects.filter(user=user)
    serializer = UserSavingsSerializers(user_savings, many=True)
    return Response(serializer.data)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
from django.contrib.auth import get_user_model
from django.conf import settings
from .serializers import *
from django.db.models import Max
from .models import Deposit, Deposit_options, Saving, Saving_option
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_deposit(request, deposit_id):
    deposit = get_object_or_404(Deposit, pk=deposit_id)
    user = request.user
    print(request)
    if user.is_authenticated:
        if user in deposit.liked_user.all():
            deposit.liked_user.remove(user)
            liked = False
        else:
            deposit.liked_user.add(user)
            liked = True
        deposit.save()
        return JsonResponse({'liked': liked})
    return JsonResponse({'error': 'User not authenticated'}, status=403)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_saving(request, saving_id):
    saving = get_object_or_404(Saving, pk=saving_id)
    user = request.user
    if user.is_authenticated:
        if user in saving.liked_user.all():
            saving.liked_user.remove(user)
            liked = False
        else:
            saving.liked_user.add(user)
            liked = True
        saving.save()
        return JsonResponse({'liked': liked})
    return JsonResponse({'error': 'User not authenticated'}, status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_deposit(request, deposit_id):
    deposit = get_object_or_404(Deposit, pk=deposit_id)
    user = request.user
    print(request)
    if user.is_authenticated:
        if user in deposit.user_deposit.all():
            deposit.user_deposit.remove(user)
            joined = False
        else:
            deposit.user_deposit.add(user)
            joined = True
        deposit.save()
        return JsonResponse({'joined': joined})
    return JsonResponse({'error': 'User not authenticated'}, status=403)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_saving(request, saving_id):
    saving = get_object_or_404(Saving, pk=saving_id)
    user = request.user
    if user.is_authenticated:
        if user in saving.user_saving.all():
            saving.user_saving.remove(user)
            joined = False
        else:
            saving.user_saving.add(user)
            joined = True
        saving.save()
        return JsonResponse({'joined': joined})
    return JsonResponse({'error': 'User not authenticated'}, status=403)

def check_meaningout(request):
    keywords = ['Green', '그린세이브', '탄소', 'ESG', '펫', '해양플라스틱', '맑은하늘']
    for keyword in keywords:
        deposits_fin_prdt_nm = Deposit.objects.filter(fin_prdt_nm__contains=keyword)
        deposits_fin_prdt_nm.update(is_meaningout=True)
        deposits_spcl_cnd = Deposit.objects.filter(spcl_cnd__contains=keyword)
        deposits_spcl_cnd.update(is_meaningout=True)
        savings_fin_prdt_nm = Saving.objects.filter(fin_prdt_nm__contains=keyword)
        savings_fin_prdt_nm.update(is_meaningout=True)
        savings_spcl_cnd = Saving.objects.filter(spcl_cnd__contains=keyword)
        savings_spcl_cnd.update(is_meaningout=True)
        
    return JsonResponse({"message": "check_okay!"})

'''
1. POST로 요청을 보낸다
 => data를 통해서 변수를 보낼수있음(GET으로 보내도 상관X -> API 요청 보낼 때 주소 건들여야함)
2. 변수는 username 아니면 pk값을 보낸다
3. 로그인 여부는
@permission_classes([IsAuthenticated]) 이걸로 확인 아니면 프론트에서 beforeenter 가드 이용해서 profile 자체 접근 막기

4. object.get.get_or_404(pk=pk) 이용해서 해당 유저의 정보를 가져온다
 '''

@api_view(['GET', 'POST'])
def recommendation_by_survey(request):
    user = request.user
    terms = ['6', '12', '24', '36']
    response_data={'user_type': user.user_type}
    if user.user_type == 'ERV' or user.user_type == 'FRV':
        rsrv_type='정액적립식'
        for term in terms:
            saving_options1 = Saving_option.objects.filter(
                rsrv_type_nm=rsrv_type,
                save_trm=term,
                saving_product_id__is_meaningout=True
            ).order_by('-intr_rate')

            savings1 = [option.saving_product_id for option in saving_options1]
            savings1 = list(set(savings1))

            saving_options2 = Saving_option.objects.filter(
                rsrv_type_nm=rsrv_type,
                save_trm=term,
                saving_product_id__is_meaningout=False
            ).order_by('-intr_rate')

            savings2 = [option.saving_product_id for option in saving_options2]
            savings2 = list(set(savings2))

            savings = savings1[:2] + savings2[:3]

            deposit_options1 = Deposit_options.objects.filter(
                save_trm=term,
                deposit_product_id__is_meaningout=True
            ).order_by('-intr_rate')

            deposits1 = [option.deposit_product_id for option in deposit_options1]
            deposits1 = list(set(deposits1))

            deposit_options2 = Deposit_options.objects.filter(
                save_trm=term,
                deposit_product_id__is_meaningout=False
            ).order_by('-intr_rate')

            deposits2 = [option.deposit_product_id for option in deposit_options2]
            deposits2 = list(set(deposits2))

            deposits = deposits1[:2] + deposits2[:3]

            context = {'term': term}
            serializer = RecSavingSerializer(savings, many=True, context=context)
            serializer2 = RecDepositSerializer(deposits, many=True,  context=context)

            response_data[f'{term}개월'] = {
                'savings': serializer.data,
                'deposits': serializer2.data,
                }

    elif user.user_type == 'ERG' or user.user_type == 'FRG':
        rsrv_type='정액적립식'
        for term in terms:
            saving_options = Saving_option.objects.filter(
                rsrv_type_nm=rsrv_type,
                save_trm=term,
                saving_product_id__is_meaningout=False
            ).order_by('-intr_rate')

            savings = [option.saving_product_id for option in saving_options]
            savings = list(set(savings))[:5]

            deposit_options = Deposit_options.objects.filter(
                save_trm=term,
                deposit_product_id__is_meaningout=False
            ).order_by('-intr_rate')

            deposits = [option.deposit_product_id for option in deposit_options]
            deposits = list(set(deposits))[:5]

            context = {'term': term}
            serializer = RecSavingSerializer(savings, many=True, context=context)
            serializer2 = RecDepositSerializer(deposits, many=True, context=context)

            response_data[f'{term}개월'] = {
                'savings': serializer.data,
                'deposits': serializer2.data,
                }


    elif user.user_type == 'EIV' or user.user_type == 'FIV':
        rsrv_type='자유적립식'
        for term in terms:
            saving_options1 = Saving_option.objects.filter(
                rsrv_type_nm=rsrv_type,
                save_trm=term,
                saving_product_id__is_meaningout=True
            ).order_by('-intr_rate')

            savings1 = [option.saving_product_id for option in saving_options1]
            savings1 = list(set(savings1))


            saving_options2 = Saving_option.objects.filter(
                rsrv_type_nm=rsrv_type,
                save_trm=term,
                saving_product_id__is_meaningout=False
            ).order_by('-intr_rate')

            savings2 = [option.saving_product_id for option in saving_options2]
            savings2 = list(set(savings2))

            savings = savings1[:2] + savings2[:3]

            deposit_options1 = Deposit_options.objects.filter(
                save_trm=term,
                deposit_product_id__is_meaningout=True
            ).order_by('-intr_rate')

            deposits1 = [option.deposit_product_id for option in deposit_options1]
            deposits1 = list(set(deposits1))

            deposit_options2 = Deposit_options.objects.filter(
                save_trm=term,
                deposit_product_id__is_meaningout=False
            ).order_by('-intr_rate')

            deposits2 = [option.deposit_product_id for option in deposit_options2]
            deposits2 = list(set(deposits2))

            deposits = deposits1[:2] + deposits2[:3]

            context = {'term': term}

            serializer = RecSavingSerializer(savings, many=True, context=context)
            serializer2 = RecDepositSerializer(deposits, many=True, context=context)

            response_data[f'{term}개월'] = {
                'savings': serializer.data,
                'deposits': serializer2.data,
                }

    elif user.user_type == 'EIG' or user.user_type == 'FIG':
        rsrv_type='자유적립식'
        for term in terms:
            saving_options = Saving_option.objects.filter(
            rsrv_type_nm='자유적립식',
            save_trm=term,
            saving_product_id__is_meaningout=False
            ).order_by('-intr_rate')

            savings = [option.saving_product_id for option in saving_options]
            savings = list(set(savings))[:5]

            deposit_options = Deposit_options.objects.filter(
                save_trm=term,
                deposit_product_id__is_meaningout=False
            ).order_by('-intr_rate')

            deposits = [option.deposit_product_id for option in deposit_options]
            deposits = list(set(deposits))[:5]

            context = {'term': term}

            serializer = RecSavingSerializer(savings, many=True, context=context)
            serializer2 = RecDepositSerializer(deposits, many=True, context=context)

            response_data[f'{term}개월'] = {
                'savings': serializer.data,
                'deposits': serializer2.data,
                }

    return Response(response_data)

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DepositViewSet, DepositOptionsViewSet, SavingViewSet, SavingOptionsViewSet

router = DefaultRouter()
router.register(r'deposits', DepositViewSet)
router.register(r'deposit-options', DepositOptionsViewSet)
router.register(r'savings', SavingViewSet)
router.register(r'saving-options', SavingOptionsViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('saving/', views.indexx, name="indexx"),
    path('save-deposit-products/', views.save_deposit_products),
    path('save-saving-products/', views.save_saving_products),
    path('check_meaningout/', views.check_meaningout),
    path('deposit-products/', views.deposit_products),
    path('deposit-product-options/<str:fin_prdt_cd>', views.deposit_products_options),
    path('deposit-products/top_rate/', views.top_rate),
    path('recommendation_by_survey/', views.recommendation_by_survey, name='recommendation_by_survey'),
    path('api/', include(router.urls)),
]

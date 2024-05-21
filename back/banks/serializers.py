from rest_framework import serializers
from .models import Deposit, Deposit_options, Saving, Saving_option, UserDeposit, UserSavings

# serializers.ModelSerializer
# - 모델 필드에 정의된 데이터만 변환

# serializers.Serializer
#  - 모델 필드에 없어도 추가로 변환

class DepositSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Deposit
        fields = '__all__'

class DepositOptionsSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Deposit_options
        fields = '__all__'

class SavingSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Saving
        fields = '__all__'

class SavingOptionsSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Saving_option
        fields = '__all__'


class UserDepositSerializers(serializers.ModelSerializer) :
    class Meta :
        model = UserDeposit
        fields = '__all__'


class UserSavingsSerializers(serializers.ModelSerializer) :
    class Meta :
        model = UserSavings
        fields = '__all__'

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'



class RecSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'

class RecSavingOptionSerializer(serializers.ModelSerializer):
    saving_product = RecSavingSerializer()

    class Meta:
        model = Saving_option
        fields = '__all__'

class RecDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class RecDepositOptionSerializer(serializers.ModelSerializer):
    deposit_product = RecDepositSerializer()

    class Meta:
        model = Deposit_options
        fields = '__all__'
from rest_framework import serializers
from .models import Deposit, Deposit_options, Saving, Saving_option
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


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'


class RecSavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving_option
        fields = '__all__'

    def to_representation(self, instance):
        # Filter options by term provided in context
        if 'term' in self.context and str(instance.save_trm) == self.context['term']:
            return super().to_representation(instance)
        return None

class RecSavingSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField() 

    class Meta:
        model = Saving
        fields = '__all__'

    def get_options(self, obj):
        term = self.context['term']
        options = obj.saving_option_set.all()
        filtered_options = [
            RecSavingOptionSerializer(option, context=self.context).data
            for option in options if str(option.save_trm) == term
        ]
        return [option for option in filtered_options if option is not None]

class RecDepositOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit_options
        fields = '__all__'

    def to_representation(self, instance):
        if 'term' in self.context and str(instance.save_trm) == self.context['term']:
            return super().to_representation(instance)
        return None

class RecDepositSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Deposit
        fields = '__all__'
    
    def get_options(self, obj):
        options = obj.deposit_options_set.all()
        filtered_options = [
            RecDepositOptionSerializer(option, context=self.context).data
            for option in options if str(option.save_trm) == self.context['term']
        ]

        return [option for option in filtered_options if option is not None]
        fields = '__all__'

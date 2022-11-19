from rest_framework import serializers
from stocks_api import models

class TransactionDataSerializer(serializers.ModelSerializer):
    """Model Serialzer for the Transaction Table Model"""
    class Meta:
        model = models.TransactionModel
        fields = '__all__'
        read_only_fields = ('amount', 'cummulative_allocation', 'bal_quantity', 'avg_purchase_price')


from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from stocks_api.models import TransactionModel
from .serializers import TransactionDataSerializer


class ListTransactionData(ModelViewSet):
    """ModelViewset for the Transactional Table"""

    queryset = TransactionModel.objects.all()
    serializer_class = TransactionDataSerializer

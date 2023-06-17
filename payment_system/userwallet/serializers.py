from rest_framework import serializers
from . models import Users,Transaction

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Users
        fields=('__all__')
class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Transaction
        fields=('__all__')
        
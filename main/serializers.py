from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields=['id','email', 'username','password','is_active','is_superuser','last_login','joined_date']

        extra_kwargs ={
            'password' : {'write_only': True}
        }

    def validate_password(self,value):
        if len(value)<4:
            raise serializers.ValidationError("Password must be minimum 4 characters")
        else:
            return value

    def save(self):
        reg = Account(
            email=self.validated_data['email'],
            username = self.validated_data['username']
        )           
        password = self.validated_data['password']
        reg.set_password(password)
        reg.save()
        return reg

# class UrlSerializer(serializers.ModelSerializer):
#      class Meta:
#         model =UrlModel
#         fields='__all__'



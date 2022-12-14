from datetime import date
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import ResetCode
from roles.administrator.serializers import RoleSerializer
from blocks.administrator.serializers import BlockSerializer
from roles.models import Role

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    username_field = get_user_model().USERNAME_FIELD

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [ 'email', 'password' ]

class ProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    block_permissions = BlockSerializer(many=True, read_only=True, source="user_blocks")
    class Meta:
        model = get_user_model()
        fields = [ 'id','email', 'first_name', 'last_name', 'dob', 'phone_no','role','profile_code','creater','block_permissions']
        read_only_fields = [ 'id', 'email', 'first_name', 'last_name', 'dob', 'phone_no','role','profile_code','creater']

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    password = serializers.CharField(
        required = True, 
        write_only = True
    )
    dob = serializers.DateField(input_formats=['%d-%m-%Y',])
    phone_no = serializers.CharField(max_length = 10)

    def validate(self, data):
        if data["dob"] >= date.today():
            raise serializers.ValidationError("The day of birth must be set before nowadays! Please check them again.")
        if str(data["phone_no"]).isdigit() == False:
            raise serializers.ValidationError("This phone number should be numbers!")
        return data

    class Meta:
        model = get_user_model()
        fields = [ "email", "password", "dob", "phone_no", "first_name", "last_name", "role"]

class UserRoleSerializer(serializers.ModelSerializer):

    role_id = serializers.PrimaryKeyRelatedField(
        queryset = Role.objects.all(),
        write_only = True,
        source = "role"
    )
    class Meta:
        model = get_user_model()
        fields = ["role","role_id"]
        read_only_fields = ["role"]

class ForgotPasswordSerializer(serializers.ModelSerializer):
    code = serializers.StringRelatedField()
    
    class Meta:
        model = get_user_model()
        fields = [ "code" ]
    
class ResetCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResetCode
        fields = ["code"]
        write_only_fields = ["code"]

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [ "id","email","first_name","last_name","role","creater" ]
        read_only_fields = [ "id","email","first_name","last_name","role","creater" ]
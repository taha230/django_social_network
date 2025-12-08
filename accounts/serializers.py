from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from termcolor import colored

# read from settings.AUTH_USER_MODEL to sync model user
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )



    password_1 = serializers.CharField(required=True ,write_only=True) # just appear in input with write_only = True  ( do not appear in output)
    password_2 = serializers.CharField(required=True ,write_only=True) # just appear in input with write_only = True  ( do not appear in output)

    class Meta:
        model = User
        fields = ('email','username', 'password_1', 'password_2', 'first_name', 'last_name') # used for returned fields
        extra_kwargs = {'first_name' : {'required' : False}, 'last_name' : {'required' : False}}


    def validate(self, attrs):
        # print(colored(attrs, 'blue'))
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError(
                {'password' : 'password did not match'}
            )
        return super(RegisterSerializer, self).validate(attrs) # to ensure the super class validator(users)

    def create(self, validated_data):
        # user= User.objects.create(
        #     username=validated_data['username'],
        #     email=validated_data['email'],
        #     first_name=validated_data.get('first_name', ''), # because the first_name {'required' : False} in extra_kwargs
        #     last_name=validated_data.get('last_name', ''), # because the last_name {'required' : False} in extra_kwargs
        # )
        # user.set_password(validated_data['password_1']) # to save the password in hashed
        # user.save()

        # print(colored(validated_data, 'yellow'))
        # use create_user in UserManager of AbstractUser instead of save
        user= User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''), # because the first_name {'required' : False} in extra_kwargs
            last_name=validated_data.get('last_name', ''), # because the last_name {'required' : False} in extra_kwargs
            password=validated_data['password_1'] # password is hashed with make_password module in create_user in UserManager
        )
        return user
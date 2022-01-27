from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import *
from django.contrib.auth.models import Group
from backend.config import verification_code_length


User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'nickname', 'password', 'avatar', 'email', 'age']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        request = self.context['request']

        user = User(
            nickname=validated_data['nickname'],
            email=validated_data['email'],
            age=validated_data['age'],
            is_active=False,
        )

        if request.session['django_timezone'] != 'unknown':
            user.country = request.session['countryCode']
            user.region = request.session['regionCode']
            user.city = request.session['city']

        if 'avatar' in validated_data:
            user.avatar = validated_data['avatar']

        user.set_password(validated_data['password'])
        user.save()
        user.groups.add(Group.objects.get(name='Regular'))

        return user


class VerifyUserSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False)
    code = serializers.CharField(max_length=verification_code_length, allow_null=False)

    def save(self):
        email = self.validated_data['email']
        code = self.validated_data['code']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return {'result': False, 'user': 'User is not exist.'}
        if VerificationCode.verify_code(user=user, code=code):
            user.is_active = True
            user.save()
            return {'result': True, 'token': user.get_token_string()}
        else:
            return {'result': False, 'code': 'Code is invalid or expired.'}


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False)

    def save(self, **kwargs):
        try:
            user = User.objects.get(email=self.validated_data['email'])
        except User.DoesNotExist:
            return {'result': False, 'user': 'User is not exist.'}
        user.send_reset_password_email()
        return {'result': True}


class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False)
    old_pass = serializers.CharField(max_length=100, allow_null=False)
    new_pass = serializers.CharField(max_length=100, allow_null=False)

    def save(self, **kwargs):
        email = self.validated_data['email']
        old_pass = self.validated_data['old_pass']
        new_pass = self.validated_data['new_pass']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return {'result': False, 'user': 'User is not exist.'}

        if user.check_password(old_pass):
            user.set_password(new_pass)
            user.save()
            return {'result': True}
        else:
            return {'result': False, 'password': 'Incorrect old password.'}


class ResetPasswordSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=verification_code_length, allow_null=False)
    email = serializers.EmailField(allow_null=False)
    password = serializers.CharField(max_length=300, allow_null=False, write_only=True)

    def save(self, **kwargs):
        code = self.validated_data['code']
        email = self.validated_data['email']
        password = self.validated_data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return {'result': False, 'error': 'User not exist.'}

        if not VerificationCode.verify_code(user=user, code=code):
            return {'result': False, 'error': 'Verification code invalid.'}

        user.set_password(password)
        user.is_active = True
        user.save()
        return {'result': True}













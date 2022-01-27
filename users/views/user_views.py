from logs.models import UserLog
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, authentication
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, parser_classes, permission_classes
from users.serializers import *
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterUser(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUser(APIView):
    parser_classes = (JSONParser, )

    def post(self, request, *args, **kwargs):
        serializer = VerifyUserSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            result = serializer.save()

            if result['result']:
                return Response(result, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(result, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([authentication.BasicAuthentication])
def login_view(request):
    user = User.objects.get(email=request.user.email)
    user_token = user.get_token_string()
    UserLog.write_log(request=request, content="Login")
    return Response(
        {"token": user_token},
        status=status.HTTP_202_ACCEPTED
    )


@api_view(['GET', 'POST'])
def logout_view(request):
    try:
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)
    except (AttributeError, ObjectDoesNotExist):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['GET', 'POST'])
@authentication_classes([authentication.TokenAuthentication])
def forget_password(request):
    serializer = ForgetPasswordSerializer(data=request.data)
    if serializer.is_valid():
        result = serializer.save()
        if result['result']:
            return Response(result, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(result, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@parser_classes([JSONParser])
def change_password(request):
    if request.user.email != request.data['email']:
        return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        result = serializer.save()
        if result['result']:
            return Response(result, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(result, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(APIView):
    parser_classes = (JSONParser, )
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            result = serializer.save()

            if result['result']:
                return Response(result, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(result, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











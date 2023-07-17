from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AlienUser, WhiteUser


# Create your views here.
class UserAccessView(APIView):
    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request, *args, **kwargs):
        if self.get_client_ip(request) == request.data["ipaddress"]:
            WhiteUser.objects.create(
                username=request.data["username"],
                type_of_log=request.data["type"],
                userdomain=request.data["userdomain"],
                hostname=request.data["hostname"],
                ipaddress=request.data["ipaddress"],
                type_of_service=request.data["logontype"],
            )
            return Response("Insert done")
        AlienUser.objects.create(
            username=request.data["username"],
            type_of_log=request.data["type"],
            userdomain=request.data["userdomain"],
            hostname=request.data["hostname"],
            ipaddress=request.data["ipaddress"],
            type_of_service=request.data["logontype"],
        )
        return Response("Insert_done")

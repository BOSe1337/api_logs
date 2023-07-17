from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


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
            User.objects.create_user(
                username=request.data["username"],
                type_of_log=request.data["type"],
                userdomain=request.data["userdomain"],
                hostname=request.data["hostname"],
                ipaddress=request.data["ipaddress"],
                type_of_service=request.data["logontype"],
            )
            return Response("Insert done")
        # return Response(request.META["REMOTE_ADDR"])
        return Response(self.get_client_ip(request))

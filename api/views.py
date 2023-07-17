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
        if self.get_client_ip(request) == request.POST["ipaddress"]:
            User.objects.create_user(
                username=request.POST["username"],
                type_of_log=request.POST["type"],
                userdomain=request.POST["userdomain"],
                hostname=request.POST["hostname"],
                ipaddress=request.POST["ipaddress"],
                type_of_service=request.POST["logontype"],
            )
            return Response("Insert done")
        # return Response(request.META["REMOTE_ADDR"])
        return Response(self.get_client_ip(request))

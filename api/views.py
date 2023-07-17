from rest_framework.response import Response
from rest_framework.views import APIView


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
        # return Response(request.META["REMOTE_ADDR"])
        return Response(self.get_client_ip(request))

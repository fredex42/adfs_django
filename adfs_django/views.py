from django.views.generic import TemplateView, View
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .jwt_auth_backend import JwtAuthMixin, JwtRestAuth
from django.http.response import HttpResponse
import json
import logging

logger = logging.getLogger(__name__)

class IndexPageView(JwtAuthMixin, TemplateView):
    template_name = "index.jinja2"


class LogoutView(TemplateView):
    template_name = "logged_out.jinja2"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request,*args,**kwargs)


class PointlessView(TemplateView):
    template_name = "nologin.jinja2"


class SetLoginCookie(JwtAuthMixin, View):
    """
    call this endpoint with a bearer token and it'll set a cookie that is picked up for regular views access.
    TODO: implement max_age from the JWT data
    """

    def get(self, request):
        if "adfstest-auth" in request.COOKIES:
            logger.info("called SetLoginCookie but cookie already set")
            return HttpResponse(json.dumps({"status":"ok","detail":"cookie set"}), status=200)
        else:
            logger.info("setting session cookie for login")
            resp = HttpResponse(json.dumps({"status":"ok","detail":"cookie set"}), status=200)
            #we already know that HTTP_AUTHORIZATION must be set, because if it was not then we would have been
            #blocked from getting here by JwtAuthMixin
            resp.set_cookie("adfstest-auth", request.META["HTTP_AUTHORIZATION"][7:])
            return resp


class RestView(APIView):
    renderer_classes = (JSONRenderer, )
    authentication_classes = (JwtRestAuth, )
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return Response({"status":"ok", "message":"Hello world!"}, status=200)

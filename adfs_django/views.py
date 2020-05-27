from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, PermissionDenied
from .jwt_auth_backend import JwtAuthMixin, JwtRestAuth


class IndexPageView(JwtAuthMixin, TemplateView):
    template_name = "index.jinja2"


class LogoutView(TemplateView):
    template_name = "logged_out.jinja2"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request,*args,**kwargs)


class PointlessView(TemplateView):
    template_name = "nologin.jinja2"


class RestView(APIView):
    renderer_classes = (JSONRenderer, )
    authentication_classes = (JwtRestAuth, )
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return Response({"status":"ok", "message":"Hello world!"}, status=200)

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = "index.jinja2"


class LogoutView(TemplateView):
    template_name = "logged_out.jinja2"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request,*args,**kwargs)


class RestView(APIView):
    authentication_classes = (JSONWebTokenAuthentication, )
    renderer_classes = (JSONRenderer, )
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args,**kwargs):
        return Response({"status":"ok","message":"Hello world!"}, status=200)

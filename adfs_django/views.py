from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = "index.jinja2"


class LogoutView(TemplateView):
    template_name = "logged_out.jinja2"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request,*args,**kwargs)
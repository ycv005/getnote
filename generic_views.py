from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "base/home_page.html"
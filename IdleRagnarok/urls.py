"""IdleRagnarok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views import generic

from django.conf.urls import url, include
from rest_framework import routers
from IdleRagnarok import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'chars', views.CharsViewSet)
router.register(r'guilds', views.GuildsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-test/', generic.TemplateView.as_view(template_name='api_test.html')),
    url(r'^', generic.TemplateView.as_view(template_name='view.html')),

    # currently unused
    #
    # path('api/v1/', generic.TemplateView.as_view(template_name='api_test.html')),
    # path('api/v1/', views.UserViewSet),
]

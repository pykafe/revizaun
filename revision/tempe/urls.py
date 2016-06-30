from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'districts', views.DistrictViewSet)
router.register(r'subdistricts', views.SubDistrictViewSet)
router.register(r'sucos', views.SucoViewSet)

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^api/', include(router.urls)),
]

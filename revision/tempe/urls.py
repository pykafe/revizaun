from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'districts', views.DistrictViewSet)
router.register(r'subdistricts', views.SubdistrictViewSet)
router.register(r'sucos', views.SucoViewSet)
router.register(r'aldeias', views.AldeiaViewSet)
router.register(r'visitors', views.VisitorViewSet)


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

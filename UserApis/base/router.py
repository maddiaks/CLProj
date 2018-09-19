from rest_framework import routers
import UserApis.base.CLThreatsApp.views

rdr_router = routers.DefaultRouter()

rdr_router.register(r'urlinfo/1', UserApis.base.CLThreatsApp.views.ThreatView)
# rdr_router.register(r'urlinfo/1', SafeURLApi.base.SafeUrlApp.views.ListThreat.as_view)


api_urlpatterns = rdr_router.urls
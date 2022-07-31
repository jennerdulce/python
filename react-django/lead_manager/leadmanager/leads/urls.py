from rest_framework import routers
from .api import LeadViewSet

# This is where you create URLS for your website / apps
router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

# Just gives us URLS that are registered by the created endpoints
urlpatterns = router.urls
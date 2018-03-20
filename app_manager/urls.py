from smp_commons.routers import SmpRouter

from . import views


router = SmpRouter()
router.register('app', views.AppViewSet, base_name='app')

urlpatterns = router.urls

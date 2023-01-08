from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register("sessions", views.SessionViewSet, basename="sessions")

urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ForwardedMessageViewSet,
    MessageViewSet,
    ThreadMemberViewSet,
    MessageActionViewSet,
    ThreadViewSet,
    ThreadActionViewSet,
)

router = DefaultRouter()
router.register("forwardedmessage", ForwardedMessageViewSet)
router.register("message", MessageViewSet)
router.register("thread", ThreadViewSet)
router.register("threadaction", ThreadActionViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("threadmember", ThreadMemberViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

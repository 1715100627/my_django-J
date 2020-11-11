from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from debugtalks.models import Debugtalks
from interfaces.models import Interfaces
from debugtalks.serializer import DebugtalksModeSerializer
from rest_framework.decorators import action

from projects.utils import get_paginated_response


class DebugtalksViewSet(viewsets.ModelViewSet):
    queryset = Debugtalks.objects.filter(is_delete=False)
    serializer_class = DebugtalksModeSerializer
    # 指定过滤引擎
    # filter_fields = [DjangoFilterBackend]
    filter_fields = ['id', 'project_id']
    # 指定权限类
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data_dict = {
            'id': instance.id,
            'debugtalk': instance.debuglak
        }
        return Response(data_dict)

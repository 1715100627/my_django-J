from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from envs.models import Envs
from interfaces.models import Interfaces
from envs.serializer import EnvModeSerializer
from rest_framework.decorators import action

from projects.utils import get_paginated_response


class EnvsViewSet(viewsets.ModelViewSet):
    queryset = Envs.objects.filter(is_delete=False)
    serializer_class = EnvModeSerializer
    # 指定过滤引擎
    # filter_fields = [DjangoFilterBackend]
    filter_fields = ['id', 'name']
    # 指定权限类
    permission_classes = [permissions.IsAuthenticated]


    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  # 逻辑删除

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = serializer.data
            datas = get_paginated_response(datas)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def names(self,request, pk=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data)
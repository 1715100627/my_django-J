from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from envs.models import Envs
from debugtalks.models import Debugtalks
from interfaces.models import Interfaces


class EnvModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        # filter=('id','name','leader','tester')
        # filter = '__all__'
        exclude = ('update_time', 'is_delete')
        # read_only_fields = ('leader', 'tester')
        extra_kwarge = {
            'create_time': {
                "read_only": True
            },
        }
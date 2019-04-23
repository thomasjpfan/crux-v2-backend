from graphene import relay
from graphene_django.types import DjangoObjectType

from ..models import Analysis
from ..models import AnalysisTag
from ..models import Dataset
from ..models import DatasetTag
from ..models import Task
from crux.models import User


class AnalysisTagNode(DjangoObjectType):
    class Meta:
        model = AnalysisTag
        interfaces = (relay.Node, )


class AnalysisNode(DjangoObjectType):
    class Meta:
        model = Analysis
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'created_by': ['exact'],
            'created_by__username': ['exact'],
            'task__dataset': ['exact'],
            'tags__name': ['exact'],
            'created_on': ['gt', 'lt'],
        }
        interfaces = (relay.Node, )


class DatasetTagNode(DjangoObjectType):
    class Meta:
        model = DatasetTag
        interfaces = (relay.Node, )


class DatasetNode(DjangoObjectType):
    class Meta:
        model = Dataset
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'created_by': ['exact'],
            'created_by__username': ['exact'],
            'tags__name': ['exact'],
            'created_on': ['gt', 'lt']
        }
        interfaces = (relay.Node, )


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        only_fields = ('id', 'username')
        interfaces = (relay.Node, )


class TaskNode(DjangoObjectType):
    class Meta:
        model = Task
        interfaces = (relay.Node, )

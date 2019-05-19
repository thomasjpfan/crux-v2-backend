import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required
from graphql_relay import from_global_id

from .nodes import DatasetNode
from ..models import DatasetTag
from ..models import Dataset
from ..models import Task


class CreateDataset(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        tags = graphene.List(graphene.NonNull(graphene.String), required=True)
        tasks = graphene.List(graphene.NonNull(graphene.String), required=True)
        figshare_id = graphene.Int(required=True)

    dataset = graphene.Field(DatasetNode)

    @staticmethod
    @login_required
    def mutate_and_get_payload(self,
                               info,
                               name,
                               description,
                               tags,
                               tasks,
                               figshare_id,
                               client_mutation_id=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')

        ds_exists = Dataset.objects.filter(figshare_id=figshare_id).exists()
        if ds_exists:
            raise Exception(
                f'figshare document, {figshare_id} already in database')

        dataset = Dataset(name=name,
                          description=description,
                          created_by=user,
                          figshare_id=figshare_id)
        dataset.save()
        for tag_name in tags:
            tag, _ = DatasetTag.objects.get_or_create(name=tag_name)
            dataset.tags.add(tag)

        for task_name in tasks:
            Task.objects.get_or_create(name=task_name,
                                       dataset=dataset,
                                       created_by=user)

        return CreateDataset(dataset=dataset)


class EditDataset(relay.ClientIDMutation):
    class Input:
        description = graphene.String(required=True)
        dataset_id = relay.GlobalID(required=True)
        tasks = graphene.List(graphene.NonNull(graphene.String), required=True)

    dataset = graphene.Field(DatasetNode)

    @staticmethod
    @login_required
    def mutate_and_get_payload(self,
                               info,
                               description,
                               dataset_id,
                               tasks,
                               client_mutation_id=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')

        _type, _id = from_global_id(dataset_id)
        graphene_type = info.schema.get_type(_type).graphene_type
        dataset_obj = graphene_type.get_node(info, _id)

        if dataset_obj.created_by != user:
            raise Exception('User did not create dataset')

        dataset_obj.description = description

        if tasks is not None:
            for task_name in tasks:
                Task.objects.get_or_create(name=task_name,
                                           dataset=dataset_obj,
                                           created_by=user)
        dataset_obj.save()

        return EditDataset(dataset=dataset_obj)


class DatasetQuery:
    dataset = relay.Node.Field(DatasetNode)
    datasets = DjangoFilterConnectionField(DatasetNode)


class DatasetMutations:
    create_dataset = CreateDataset.Field()
    edit_dataset = EditDataset.Field()

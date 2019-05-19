import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required
from graphql_relay import from_global_id

from ..models import Dataset
from ..models import Task
from .nodes import AnalysisNode
from ..models import Analysis
from ..models import AnalysisTag


class CreateAnalysis(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        tags = graphene.List(graphene.NonNull(graphene.String), required=True)
        figshare_id = graphene.Int(required=True)
        dataset_id = relay.GlobalID(required=True)
        task_id = relay.GlobalID(required=False)

    analysis = graphene.Field(AnalysisNode)

    @staticmethod
    @login_required
    def mutate_and_get_payload(self,
                               info,
                               name,
                               description,
                               tags,
                               figshare_id,
                               dataset_id,
                               task_id,
                               client_mutation_id=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')

        anaylsis_exists = Analysis.objects.filter(
            figshare_id=figshare_id).exists()
        if anaylsis_exists:
            raise Exception(
                f'figshare document, {figshare_id} already in database')

        _type, _id = from_global_id(dataset_id)
        graphene_type = info.schema.get_type(_type).graphene_type
        dataset_obj = graphene_type.get_node(info, _id)

        if not isinstance(dataset_obj, Dataset):
            raise Exception("dataset_id does not reference a valid dataset")

        task_obj = None
        if task_id:
            _type, _id = from_global_id(task_id)
            graphene_type = info.schema.get_type(_type).graphene_type
            task_obj = graphene_type.get_node(info, _id)

            if not isinstance(task_obj, Task):
                raise Exception("task_id does not reference a valid task")

            if (task_obj.dataset != dataset_obj):
                raise Exception("Task is not assoicated with dataset")

        analysis = Analysis(name=name,
                            description=description,
                            created_by=user,
                            dataset=dataset_obj,
                            task=task_obj,
                            figshare_id=figshare_id)
        analysis.save()
        for tag_name in tags:
            tag, _ = AnalysisTag.objects.get_or_create(name=tag_name)
            analysis.tags.add(tag)

        return CreateAnalysis(analysis=analysis)


class EditAnalysis(relay.ClientIDMutation):
    class Input:
        description = graphene.String(required=True)
        analysis_id = relay.GlobalID(required=True)

    analysis = graphene.Field(AnalysisNode)

    @staticmethod
    @login_required
    def mutate_and_get_payload(self,
                               info,
                               description,
                               analysis_id,
                               client_mutation_id=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')

        _type, _id = from_global_id(analysis_id)
        graphene_type = info.schema.get_type(_type).graphene_type
        analysis_obj = graphene_type.get_node(info, _id)

        if analysis_obj.created_by != user:
            raise Exception('User did not create dataset')

        analysis_obj.description = description
        analysis_obj.save()

        return EditAnalysis(analysis=analysis_obj)


class AnalysisQuery:
    analysis = relay.Node.Field(AnalysisNode)
    analyses = DjangoFilterConnectionField(AnalysisNode)


class AnalysisMutations:
    create_analysis = CreateAnalysis.Field()
    edit_analysis = EditAnalysis.Field()

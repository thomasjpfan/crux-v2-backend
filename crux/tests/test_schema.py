from django.test import TestCase

from ..schema import schema
from ..models import User
from ..models import Dataset
from ..models import Tag


class SchemaModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('tom', 'tom@a.com', 'pw1')
        self.user2 = User.objects.create_user('jerry', 'j@b.com', 'pw2')

        datasets = [
            {
                'name': 'mnist',
                'description': 'cool',
                'created_by': self.user1
            },
            {
                'name': 'titanic',
                'description': 'very cool',
                'created_by': self.user2
            },
            {
                'name': 'paris',
                'description': 'wow',
                'created_by': self.user1
            },
            {
                'name': 'sf',
                'description': 'very interesting',
                'created_by': self.user2
            },
            {
                'name': 'nyc',
                'description': 'what is this',
                'created_by': self.user1
            },
        ]
        self.datasets = {}

        for ds_kwargs in datasets:
            ds = Dataset(**ds_kwargs)
            ds.save()
            self.datasets[ds_kwargs['name']] = ds

        # Add cool tag
        t = Tag(content_object=self.datasets['mnist'], name="cool")
        t.save()
        t = Tag(content_object=self.datasets['titanic'], name="cool")
        t.save()

    def execute_query(self, query):
        executed = schema.execute(query)
        self.assertIsNotNone(executed)
        self.assertIsNotNone(executed.data)
        return executed.data

    def test_query_all_datasets(self):
        query = '''
        {
        allDatasets {
            edges {
                node {
                    name
                    createdBy {
                        username
                    }
                }
            }
        }
        }
        '''
        data = self.execute_query(query)
        self.assertEqual(len(data['allDatasets']['edges']), len(self.datasets))

    def test_query_all_datasets_filter_exact(self):
        query = '''
        {
        allDatasets(name: "sf") {
            edges {
                node {
                    name
                    createdBy {
                        username
                    }
                }
            }
        }
        }
        '''
        data = self.execute_query(query)
        self.assertEqual(len(data['allDatasets']['edges']), 1)

    def test_query_all_datasets_filter_icontains(self):
        query = '''
        {
        allDatasets(name_Icontains: "n") {
            edges {
                node {
                    name
                }
            }
        }
        }
        '''
        data = self.execute_query(query)
        self.assertEqual(len(data['allDatasets']['edges']), 3)

    def test_query_all_datasets_filter_istartswith(self):
        query = '''
        {
        allDatasets(name_Istartswith: "m") {
            edges {
                node {
                    name
                }
            }
        }
        }
        '''
        data = self.execute_query(query)
        self.assertEqual(len(data['allDatasets']['edges']), 1)

    def test_query_dataset_with_tag(self):
        query = '''
        {
            allDatasets(tag: "cool") {
                edges {
                    node {
                        name
                    }
                }
            }
        }
        '''
        data = schema.execute(query)
        self.assertEqual(len(data['allDatasets']['edges']), 2)

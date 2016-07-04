import datetime
from haystack import indexes
from utils.models import School


class SchoolIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    address = indexes.DateTimeField(model_attr='address')

    def get_model(self):
        return School

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
		
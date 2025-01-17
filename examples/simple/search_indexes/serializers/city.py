from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from ..documents import CityDocument

__all__ = ('CityDocumentSerializer',)


class CityDocumentSerializer(DocumentSerializer):
    """Serializer for city document."""

    class Meta:
        """Meta options."""

        document = CityDocument
        fields = (
            'id',
            'name',
            'info',
            'country',
            'location',
            'capital',
            'boolean_list',
            'datetime_list',
            'float_list',
            'integer_list',
        )

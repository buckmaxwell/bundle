__author__ = 'Max Buck and Sam Buck'
__email__ = 'maxbuckdeveloper@gmail.com'
__reddit__ = '/r/egolocation'
__version__ = '1.0.0'

from neomodel import (StringProperty, AliasProperty, RelationshipTo, RelationshipFrom, OneOrMore, One)
from neoapi import SerializableStructuredNode, SerializableStructuredRel, DateTimeProperty
import user
import word


class Reflection(SerializableStructuredNode):
    """
    This is the Reflection Object
    """

    __type__ = 'reflections'  # => __type__ must be specified and the same as the default for type

    # INFO
    version = '1.0.0'  # => A version is not required but is a good idea

    # ATTRIBUTES -- NOTE: 'type' and 'id' are required for json api specification compliance
    type = StringProperty(default='reflections')  # => required, unique name for model
    id = StringProperty(unique_index=True, required=True)  # => required
    title = StringProperty(required=True)
    text_blob = StringProperty(required=True)

    # RELATIONSHIPS
    words = RelationshipTo('word.Word', 'HAS_WORD', cardinality=OneOrMore, model=SerializableStructuredRel)
    user = RelationshipFrom('user.User', 'CREATED', cardinality=One, model=SerializableStructuredRel)

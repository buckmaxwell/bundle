__author__ = 'Max Buck and Sam Buck'
__email__ = 'maxbuckdeveloper@gmail.com'
__reddit__ = '/r/egolocation'
__version__ = '1.0.0'

from neomodel import (StringProperty, AliasProperty, RelationshipTo, RelationshipFrom, ZeroOrMore)
from neoapi import SerializableStructuredNode, SerializableStructuredRel, DateTimeProperty
import reflection


class Word(SerializableStructuredNode):
    """
    This is the Word Object
    """

    __type__ = 'words'  # => __type__ must be specified and the same as the default for type

    # INFO
    version = '1.0.0'  # => A version is not required but is a good idea

    # ATTRIBUTES -- NOTE: 'type' and 'id' are required for json api specification compliance
    type = StringProperty(default='words')  # => required, unique name for model
    id = StringProperty(unique_index=True, required=True)  # => required
    word = AliasProperty(to=id)

    # RELATIONSHIPS
    reflections = RelationshipFrom('reflection.Reflection', 'HAS_WORD', cardinality=ZeroOrMore, model=SerializableStructuredRel)

"""Transport registry."""
from ..utils.imports import FactoryMapping

__all__ = ['by_name', 'by_url']

TRANSPORTS = FactoryMapping(
    aiokafka='faust.transport.aiokafka:Transport',
    kafka='faust.transport.aiokafka:Transport',
    confluent='faust.transport.confluent:Transport',
)
TRANSPORTS.include_setuptools_namespace('faust.transports')
by_name = TRANSPORTS.by_name
by_url = TRANSPORTS.by_url

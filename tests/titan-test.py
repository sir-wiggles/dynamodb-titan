# This is a python 3.4 test script using bulbsflow to connect to titan
#
# First install bulbsflow:
# - pip install bulbs
#
# TEST Commands:
# - http://bulbflow.com/quickstart/#create-the-graph-object

from bulbs.titan import Graph, Config
from bulbs.config import DEBUG, ERROR
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime
import os

from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.table import Table

host = os.getenv('TITAN_ON_DDB_PORT_8182_TCP_ADDR')
port = os.getenv('TITAN_ON_DDB_PORT_8182_TCP_PORT')

config = Config(
    "http://%s:%s/graphs/yay_graph/" % (
        os.getenv('TITAN_ON_DDB_PORT_8182_TCP_ADDR'),
        os.getenv('TITAN_ON_DDB_PORT_8182_TCP_PORT'),
    )
)
g = Graph(config)

g.config.set_logger(DEBUG)
# g.config.set_logger(ERROR)

# james = g.vertices.create(name="James")
# julie = g.vertices.create(name="Julie")
# g.edges.create(james, "knows", julie)

host = os.getenv('DDB_LOCAL_PORT_8000_TCP_ADDR')
port = os.getenv('DDB_LOCAL_PORT_8000_TCP_PORT')

conn = DynamoDBConnection(
    host=host,
    port=port,
    aws_access_key_id='foo',
    aws_secret_access_key='bar',
    is_secure=False,
)

'''
{u'TableNames': [u'yay_graph_edgestore',
  u'yay_graph_graphindex',
  u'yay_graph_system_properties',
  u'yay_graph_systemlog',
  u'yay_graph_titan_ids',
  u'yay_graph_txlog']}
'''

tables = conn.list_tables()

table_objects = {}
for k in tables['TableNames']:
    t = Table(k, connection=conn)
    table_objects[k] = t


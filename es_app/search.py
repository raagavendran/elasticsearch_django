from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date

connections.create_connection()

class BlogPostIndex(DocType):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()
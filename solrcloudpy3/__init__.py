from solrcloudpy3.connection import SolrConnection
from solrcloudpy3.collection import SolrCollection
from solrcloudpy3.parameters import SearchOptions
import logging
logging.basicConfig()

__version__ = "0.1a"
__all__ = ['SolrCollection', 'SolrConnection', 'SearchOptions']

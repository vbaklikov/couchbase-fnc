'''
Created on Apr 2, 2014

@author: klyk
'''
from twisted.internet import reactor

from couchbase import experimental
experimental.enable()

from txcouchbase.connection import Connection

def on_view_rows(res):
    for row in res:
        print "Got row", row.key

cb = Connection(bucket='beer-sample', password='beer')
d = cb.queryAll("beer", "brewery_beers", limit=20)
d.addCallback(on_view_rows)
reactor.run()
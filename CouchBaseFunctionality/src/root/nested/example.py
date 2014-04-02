'''
Created on Apr 1, 2014

@author: klyk
'''
import pprint
from couchbase import Couchbase
from couchbase.exceptions import CouchbaseError

c = Couchbase.connect(bucket='beer-sample', host='localhost',password='beer')

try:
    beer = c.get("aass_brewery-juleol")

except CouchbaseError as e:
    print "Couldn't retrieve value for key", e
    # Rethrow the exception, making the application exit
    raise

doc = beer.value

# Because Python 2.x will complain if an ASCII format string is used
# with Unicode format values, we make the format string unicode as well.


#print unicode("{name}, ABV: {abv}").format(name=doc['name'], abv=doc['abv'])
pprint.pprint(doc)

doc['comment'] = "Random beer from Norway"

try:
    result = c.replace("aass_brewery-juleol", doc)
    print result

except CouchbaseError as e:
    print "Couldn't replace key"
    raise
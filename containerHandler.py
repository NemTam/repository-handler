from google.appengine.ext import ndb
import pickle


# Google AppEngine DataBase model class
class RepoContainer(ndb.Model):
    name = ndb.StringProperty()
    repo_list_db = ndb.BlobProperty()
    id_list_db = ndb.BlobProperty()


# Initialization of the container which stores the repositories
def container_init():
    container = RepoContainer.query(RepoContainer.name == 'myContainer').get()
    if container is None:
        container = RepoContainer(name='myContainer')
        # Object serialization (AppEngine Datastore can only hold predefined data objects)
        container.repo_list_db = pickle.dumps([])
        container.id_list_db = pickle.dumps([])
    return container.put()



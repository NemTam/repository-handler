import repoHandlerFunctions
import ast
from containerHandler import container_init
import pickle

REQUEST_TYPE = "requestType"
PRINT_ALL = "print_all"
NEW_REPO = "new_repo"
DELETE_REPO = "delete_repo"
ACCESS_REPO = "get_singe_repo"
GET_MULTIPLE_ACCESSED_REPOS = "get_multiple_accessed_repos"


def request_parser(request, repo_container, id_container):
    request_type = request.get(REQUEST_TYPE)
    if request_type == PRINT_ALL:
        return repoHandlerFunctions.print_repos(repo_container)

    elif request_type == NEW_REPO:
        # Parsing unicode parameter list
        params = ast.literal_eval(request.get("params"))
        id = params[0]
        owner = params[1]
        return repoHandlerFunctions.new_repo(repo_container, id_container, id, owner)

    elif request_type == ACCESS_REPO:
        repo_id = request.get("params")
        return repoHandlerFunctions.access_repo(repo_container, repo_id)

    elif request_type == DELETE_REPO:
        repo_id = request.get("params")
        return repoHandlerFunctions.delete_repo(repo_container, repo_id)

    elif request_type == GET_MULTIPLE_ACCESSED_REPOS:
        value = int(request.get("params"))
        return repoHandlerFunctions.get_repos_access_count(repo_container, value)


def request_controller(request):
    container_key = container_init()
    # loading the repository container
    container = container_key.get()

    # object deserialization
    repo_container = pickle.loads(container.repo_list_db)
    id_container = pickle.loads(container.id_list_db)

    response = request_parser(request, repo_container, id_container)

    # container serialization
    container.repo_list_db = pickle.dumps(repo_container)
    container.id_list_db = pickle.dumps(id_container)

    # storing the data container
    container.put()
    return response

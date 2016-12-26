import repoContainer
import ast

REQUEST_TYPE = "requestType"
PRINT_ALL = "print_all"
NEW_REPO = "new_repo"
DELETE_REPO = "delete_repo"
GET_SINGLE_REPO = "get_singe_repo"
GET_MULTIPLE_ACCESSED_REPOS = "get_multiple_accessed_repos"


def request_controller(request):
    request_type = request.get(REQUEST_TYPE)

    if request_type == PRINT_ALL:
        return repoContainer.print_repos()

    if request_type == NEW_REPO:
        # Parsing unicode parameter list
        params = ast.literal_eval(request.get("params"))
        id = params[0]
        owner = params[1]
        return repoContainer.new_repo(id, owner)

    if request_type == DELETE_REPO:
        repo_id = request.get("params")
        return repoContainer.delete_repo(repo_id)

    if request_type == GET_SINGLE_REPO:
        repo_id = request.get("params")
        return repoContainer.get_single_repo(repo_id)

    if request_type == GET_MULTIPLE_ACCESSED_REPOS:
        value = int(request.get("params"))
        return repoContainer.get_repos_access_count(value)

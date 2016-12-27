# repository-handler
This is a repository handler service, a Google AppEngine application.
You are able to use it with a REST client.

Request parameters:
'requestType': 'print_all'  - Fetches all repositories
'requestType': 'new_repo', 'params' : [<id>,<owner>] - Creates new repository
'requestType': 'delete_repo', 'params' : <id> - Deletes a repository
'requestType': 'get_single_repo', 'params' : <id> - Access a repository
'requestType': 'get_multiple_accessed_repos', 'params': <value> - Fetches all the repositories which have been accessed <value> times.
# repository-handler
This is a repository handler service, a Google AppEngine application. <br>
You are able to use it with a REST client. <br>

Request parameters: <br>
'requestType': 'print_all'  - Fetches all repositories <br>
'requestType': 'new_repo', 'params' : '[\<id>, \<owner>] - Creates new repository <br>
'requestType': 'delete_repo', 'params' : \<id> - Deletes a repository <br>
'requestType': 'get_single_repo', 'params' : \<id> - Access a repository <br>
'requestType': 'get_multiple_accessed_repos', 'params': \<value> - Fetches all the repositories which have been accessed \<value> times. <br>

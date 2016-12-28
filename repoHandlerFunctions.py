from myRepo import Repo

REPO_FOUND = "\nRepository accessed, details: \n"
LIST_ALL_REPOS = "<id>  <owner>  <date>\n"
LIST_ONE_REPO = "\n<id>  <owner>  <date>  <access counter>\n"
NEW_REPO_DONE = "\nNew repo created, details: \n"
NEW_REPO_FAIL = "\nThis is not a valid id, please try again.\n"
REPO_NOT_FOUND = "\nThere is no repository with this id, please try again.\n"
REPOS_NOT_FOUND = "\nThere are no repositories with this criteria, please try again.\n"


def print_repos(repo_container):
    response = ""
    for repo in repo_container:
        response += repo.id + ' ' + repo.owner + ' ' + repo.date + '\n'
    return LIST_ALL_REPOS + response


def new_repo(repo_container, id_list, repo_id, owner):
    if repo_id not in id_list:
        repo = Repo(repo_id, owner)
        repo_container.append(repo)
        id_list.append(repo_id)
        return NEW_REPO_DONE + repo.id + ' ' + repo.owner + ' ' + repo.date
    else:
        return NEW_REPO_FAIL


def access_repo(repo_container, repo_id):
    response = ""
    for repo in repo_container:
        if repo.id == repo_id:
            repo.increment_access_count()
            response += repo.id + ' ' + repo.owner + ' ' + repo.date + ' ' + str(repo.access_count) + '\n'
            return REPO_FOUND + LIST_ONE_REPO + response
    return REPO_NOT_FOUND


def delete_repo(repo_container, repo_id):
    for repo in repo_container:
        if repo.id == repo_id:
            repo_container.remove(repo)
            return "Repository <" + repo.id + "> deleted"
    else:
        return REPO_NOT_FOUND


def get_repos_access_count(repo_container, value):
    response = ""
    for repo in repo_container:
        if repo.access_count >= value:
            response += repo.id + ' ' + repo.owner + ' ' + repo.date + ' ' + str(repo.access_count) + '\n'
    if response:
        return LIST_ONE_REPO + response
    else:
        return REPOS_NOT_FOUND

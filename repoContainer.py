from myRepo import Repo

repoContainer = []
idList = []

LIST_ALL_REPOS = "<id>  <owner>  <date>\n"
LIST_ONE_REPO = "\n<id>  <owner>  <date>  <access counter>\n"
NEW_REPO_DONE = "\nNew repo created, details: \n"
NEW_REPO_FAIL = "\nThis is not a valid id, please try again.\n"
REPO_NOT_FOUND = "\nThere is no repository with this id, please try again.\n"
REPOS_NOT_FOUND = "\nThere are no repositories with this criteria, please try again.\n"
REPO_FOUND = "\nRepository found, details: \n"


def new_repo(repo_id, owner):
    if repo_id not in idList:
        repo = Repo(repo_id, owner)
        repoContainer.append(repo)
        idList.append(repo_id)
        return NEW_REPO_DONE + repo.id + ' ' + repo.owner + ' ' + repo.date
    else:
        return NEW_REPO_FAIL


def print_repos():
    response = ""
    for repo in repoContainer:
        response += repo.id + ' ' + repo.owner + ' ' + repo.date + '\n'
    return LIST_ALL_REPOS + response


def get_single_repo(repo_id):
    response = ""
    for repo in repoContainer:
        if repo.id == repo_id:
            repo.increment_access_count()
            response += repo.id + ' ' + repo.owner + ' ' + repo.date + ' ' + str(repo.access_count) + '\n'
            return REPO_FOUND + LIST_ONE_REPO + response
    return REPO_NOT_FOUND


def delete_repo(repo_id):
    for repo in repoContainer:
        if repo.id == repo_id:
            repoContainer.remove(repo)
            return "Repository <" + repo.id + "> deleted"
    else:
        return REPO_NOT_FOUND


def get_repos_access_count(value):
    response = ""
    for repo in repoContainer:
        if repo.access_count >= value:
            response += repo.id + ' ' + repo.owner + ' ' + repo.date + ' ' + str(repo.access_count) + '\n'
    if response:
        return LIST_ONE_REPO + response
    else:
        return REPOS_NOT_FOUND


# Todelete
new_repo("12345", "Tamas")
new_repo("54321", "John")
new_repo("1234", "Nadal")
print print_repos()
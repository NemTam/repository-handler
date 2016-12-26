import urllib
import httplib2
import os

url = 'http://127.0.0.1:8080'
headers = {'Content-type': 'application/x-www-form-urlencoded'}


REQUEST_TYPE = "requestType"
PRINT_ALL = "print_all"
NEW_REPO = "new_repo"
DELETE_REPO = "delete_repo"
GET_SINGLE_REPO = "get_singe_repo"
GET_MULTIPLE_ACCESSED_REPOS = "get_multiple_accessed_repos"


def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('cls')

    print("\t************************************")
    print("\t***   REPO HANDLER REST CLIENT   ***")
    print("\t************************************")


def send_http_request(my_body):
    http = httplib2.Http()
    response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(my_body))
    return content


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def body_assembler(requestType, params=None):
    request_body = {'requestType': requestType, 'params': params}
    return request_body

display_title_bar()

### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
choice = ''
while choice != 'q':

    # Let users know what they can do.
    repo_help = "\n[1] List all of the repos\n[2] Add a new repository\n" \
                "[3] Access a repository\n[4] Delete repository\n" \
                "[5] List the repository if it was accessed more than X\n" \
                "[q] Quit.\n"
    print repo_help
    choice = raw_input("What would you like to do?\n")

    # Respond to the user's choice.
    if choice == '1':
        clear()
        body = body_assembler(PRINT_ALL)
        print send_http_request(body)

    elif choice == '2':
        clear()
        owner = raw_input("What is your name?\n")
        id = raw_input("Enter the id of the new repo:\n")
        body = body_assembler(NEW_REPO, [id, owner])
        print send_http_request(body)

    elif choice == '3':
        clear()
        body = body_assembler(PRINT_ALL)
        print send_http_request(body)
        repo_id = raw_input("\nEnter a Valid repository ID\n")
        body = body_assembler(GET_SINGLE_REPO, repo_id)
        print send_http_request(body)

    elif choice == '4':
        clear()
        body = body_assembler(PRINT_ALL)
        print send_http_request(body)
        repo_id = raw_input("\nEnter a Valid repository ID\n")
        body = body_assembler(DELETE_REPO, repo_id)
        print send_http_request(body)

    elif choice == '5':
        clear()
        value = raw_input("\nAdd a value:\n")
        body = body_assembler(GET_MULTIPLE_ACCESSED_REPOS, value)
        print send_http_request(body)

    elif choice == 'q':
        print("\nDisconnecting, bye")
    else:
        print("\nI don't understand.\n")



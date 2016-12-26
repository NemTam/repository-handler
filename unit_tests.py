import unittest
import repoContainer as testContainer

test_new_id = "1234ABC"
test_delete_id = "1234"
test_id1 = "1235"
test_id2 = "123"

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        testContainer.new_repo(test_delete_id, "Tamas")
        testContainer.new_repo(test_id1, "Peter")
        testContainer.new_repo(test_id2, "Zoltan")

        testContainer.access_repo(test_id1)
        testContainer.access_repo(test_id1)
        testContainer.access_repo(test_id2)

    @classmethod
    def tearDownClass(cls):
        del testContainer.repoContainer[:]

    def test_addRepo(self):
        testContainer.new_repo(test_new_id, "Tamas")
        add_success = False
        for repo in testContainer.repoContainer:
            if repo.id == test_new_id:
                add_success = True
        self.assertTrue(add_success)

    def test_addExistingRepo(self):
        result = testContainer.new_repo("123", "Zoltan")
        self.assertIn(result, testContainer.NEW_REPO_FAIL)

    def test_deleteRepo_success(self):
        testContainer.delete_repo(test_delete_id)
        for repo in testContainer.repoContainer:
            if repo.id == test_delete_id:
                self.fail("Repo is not deleted")

    def test_deleteRepo_fail(self):
        result = testContainer.delete_repo("notvalidid")
        self.assertIn(result, testContainer.REPO_NOT_FOUND)

    def test_accessRepo(self):
        testContainer.access_repo(test_id1)
        for repo in testContainer.repoContainer:
            if repo.id == test_id1:
                self.assertEqual(repo.access_count, 3)

    def test_getMultipleAccessedRepos(self):
        result = testContainer.get_repos_access_count(1)
        if test_id1 not in result or test_id2 not in result:
            self.fail("Repos are not correctly displayed")


if __name__ == '__main__':
    unittest.main()

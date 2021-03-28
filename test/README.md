# Executing Tests

```bash
# run all tests in the current directory
$ pytest .
$ nosetests .

# run all tests with full stdout (-s / --capture=no)
$ pytest -s
$ nosetests -s .

# run a test module
$ pytest -s test_user.py
$ nosetests -s test_user.py

# run a single test
$ pytest -s test_user.py::User::test_environment_queries
$ nosetests -s test_user.py:User.test_environment_queries

# run a set of tests (filtered by keywords)
$ pytest -s -k "User and test_extension_name"
```

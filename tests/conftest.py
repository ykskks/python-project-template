# ref: https://github.com/pytest-dev/pytest/issues/2393
# delete after adding tests
def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 5:
        session.exitstatus = 0

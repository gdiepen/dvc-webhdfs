import pytest
from dvc.testing.api_tests import (  # noqa, pylint: disable=unused-import
    TestAPI,
)
from dvc.testing.remote_tests import (  # noqa, pylint: disable=unused-import
    TestRemote,
)
from dvc.testing.workspace_tests import TestImport as _TestImport


@pytest.fixture
def remote(make_remote):
    yield make_remote(name="upstream", typ="webhdfs")


@pytest.fixture
def workspace(make_workspace):
    yield make_workspace(name="workspace", typ="webhdfs")


class TestImport(_TestImport):
    @pytest.fixture
    def stage_md5(self):
        return "3869631c193f0a3c206c6f04e84cb2b6"

    @pytest.fixture
    def is_object_storage(self):
        return False

    @pytest.fixture
    def dir_md5(self):
        return "32f6597da5c3c1dead9dc562faac09a2.dir"

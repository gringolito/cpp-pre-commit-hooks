# -*- coding: utf-8 -*-
import os
import unittest

from pre_commit_hooks.check_using_namespace_directive import main as hook


class TestUsingNamespaceHook(unittest.TestCase):
    """ Tests for Check `using namespace` directive hook """

    def setUp(self) -> None:
        resources_path = os.path.relpath(
            os.path.join(os.path.dirname(__file__), "resources", "using_namespace_directive")
        )
        ok_path = os.path.join(resources_path, "ok")
        nok_path = os.path.join(resources_path, "nok")
        self.ok_files = [os.path.join(ok_path, file) for file in os.listdir(ok_path)]
        self.nok_files = [os.path.join(nok_path, file) for file in os.listdir(nok_path)]

    def assertFail(self, value: int, file: str) -> None:  # pylint: disable=C0116
        self.assertEqual(value, 1, msg=f"\nFile:     {file}\nExpected: To be Non-Ok\nResult:   Ok")

    def assertOk(self, value: int, file: str) -> None:  # pylint: disable=C0116
        self.assertEqual(value, 0, msg=f"\nFile:     {file}\nExpected: To be Ok\nResult:   Non-Ok")

    @staticmethod
    def is_source_file(file: str) -> bool:  # pylint: disable=C0116
        return any(
            [
                file.endswith(".c"),
                file.endswith(".cc"),
                file.endswith(".cpp"),
                file.endswith(".cxx"),
            ]
        )

    def test_ok_files(self):
        """
        Test Ok files
        """
        for file in self.ok_files:
            ret = hook([file])
            self.assertOk(ret, file)

    def test_nok_files(self):
        """
        Test Non-Ok files
        """
        for file in self.nok_files:
            ret = hook([file])
            self.assertFail(ret, file)

    def test_ok_files_allow_in_source(self):
        """
        Test Ok files with --allow-in-source flag
        """
        for file in self.ok_files:
            ret = hook(["--allow-in-source", file])
            self.assertOk(ret, file)

    def test_nok_files_allow_in_source(self):
        """
        Test Non-Ok files with --allow-in-source flag
        """
        for file in self.nok_files:
            ret = hook(["--allow-in-source", file])
            if self.is_source_file(file):
                self.assertOk(ret, file)
            else:
                self.assertFail(ret, file)

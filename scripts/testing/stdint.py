"""
@file stdint.py
@brief Unit tests for cilibc standard integer types.

This module contains unit tests for verifying the correct behavior
of the cilibc standard integer types, including size and alignment checks.
"""
from subprocess import run, CompletedProcess
from typing import Any, List
import unittest
import os


class TestStdint(unittest.TestCase):
    """
    Unit tests for cilibc standard integer types.
    """

    def testInt8Min(self):
        """
        Test that INT8_MIN is -128.
        """
        result: CompletedProcess = run(
            ["__build/test/int8min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testInt8Max(self):
        """
        Test that INT8_MAX is 127.
        """
        result: CompletedProcess = run(
            ["__build/test/int8max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testInt16Min(self):
        """
        Test that INT16_MIN is -32768.
        """
        result: CompletedProcess = run(
            ["__build/test/int16min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testInt16Max(self):
        """
        Test that INT16_MAX is 32767.
        """
        result: CompletedProcess = run(
            ["__build/test/int16max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testInt32Min(self):
        """
        Test that INT32_MIN is -2147483648.
        """
        result: CompletedProcess = run(
            ["__build/test/int32min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testInt32Max(self):
        """
        Test that INT32_MAX is 2147483647.
        """
        result: CompletedProcess = run(
            ["__build/test/int32max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testInt64Min(self):
        """
        Test that INT64_MIN is -9223372036854775808.
        """
        result: CompletedProcess = run(
            ["__build/test/int64min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testInt64Max(self):
        """
        Test that INT64_MAX is 9223372036854775807.
        """
        result: CompletedProcess = run(
            ["__build/test/int64max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUInt8Max(self):
        """
        Test that UINT8_MAX is 255.
        """
        result: CompletedProcess = run(
            ["__build/test/uint8max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUInt16Max(self):
        """
        Test that UINT16_MAX is 65535.
        """
        result: CompletedProcess = run(
            ["__build/test/uint16max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUInt32Max(self):
        """
        Test that UINT32_MAX is 4294967295.
        """
        result: CompletedProcess = run(
            ["__build/test/uint32max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUInt64Max(self):
        """
        Test that UINT64_MAX is 18446744073709551615.
        """
        result: CompletedProcess = run(
            ["__build/test/uint64max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntLeast8Min(self):
        """
        Test that INT_LEAST8_MIN is -128.
        """
        result: CompletedProcess = run(
            ["__build/test/intleast8min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntLeast16Min(self):
        """
        Test that INT_LEAST16_MIN is -32768.
        """
        result: CompletedProcess = run(
            ["__build/test/intleast16min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntLeast32Min(self):
        """
        Test that INT_LEAST32_MIN is -2147483648.
        """
        result: CompletedProcess = run(
            ["__build/test/intleast32min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntLeast64Min(self):
        """
        Test that INT_LEAST64_MIN is -9223372036854775808.
        """
        result: CompletedProcess = run(
            ["__build/test/intleast64min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntLeast8Max(self):
        """
        Test that INT_LEAST8_MAX is 127.
        """
        result: CompletedProcess = run(
            ["__build/test/intleast8max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntLeast16Max(self):
        """
        Test that INT_LEAST16_MAX is 32767.
        """
        result: CompletedProcess = run(
            ["__build/test/intleast16max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntLeast32Max(self):
        """
        Test that INT_LEAST32_MAX is 2147483647.
        """
        result: CompletedProcess = run(
            ["__build/test/intleast32max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntLeast64Max(self):
        """
        Test that INT_LEAST64_MAX is 9223372036854775807.
        """
        result: CompletedProcess = run(
            ["__build/test/intleast64max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntLeast8Max(self):
        """
        Test that UINT_LEAST8_MAX is 255.
        """
        result: CompletedProcess = run(
            ["__build/test/uintleast8max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntLeast16Max(self):
        """
        Test that UINT_LEAST16_MAX is 65535.
        """
        result: CompletedProcess = run(
            ["__build/test/uintleast16max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntLeast32Max(self):
        """
        Test that UINT_LEAST32_MAX is 4294967295.
        """
        result: CompletedProcess = run(
            ["__build/test/uintleast32max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntLeast64Max(self):
        """
        Test that UINT_LEAST64_MAX is 18446744073709551615.
        """
        result: CompletedProcess = run(
            ["__build/test/uintleast64max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntFast8Min(self):
        """
        Test that INT_FAST8_MIN is -128.
        """
        result: CompletedProcess = run(
            ["__build/test/intfast8min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntFast16Min(self):
        """
        Test that INT_FAST16_MIN is -32768.
        """
        result: CompletedProcess = run(
            ["__build/test/intfast16min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntFast32Min(self):
        """
        Test that INT_FAST32_MIN is -2147483648.
        """
        result: CompletedProcess = run(
            ["__build/test/intfast32min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntFast64Min(self):
        """
        Test that INT_FAST64_MIN is -9223372036854775808.
        """
        result: CompletedProcess = run(
            ["__build/test/intfast64min"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntFast8Max(self):
        """
        Test that INT_FAST8_MAX is 127.
        """
        result: CompletedProcess = run(
            ["__build/test/intfast8max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntFast16Max(self):
        """
        Test that INT_FAST16_MAX is 32767.
        """
        result: CompletedProcess = run(
            ["__build/test/intfast16max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntFast32Max(self):
        """
        Test that INT_FAST32_MAX is 2147483647.
        """
        result: CompletedProcess = run(
            ["__build/test/intfast32max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntFast64Max(self):
        """
        Test that INT_FAST64_MAX is 9223372036854775807.
        """
        result: CompletedProcess = run(
            ["__build/test/intfast64max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntFast8Max(self):
        """
        Test that UINT_FAST8_MAX is 255.
        """
        result: CompletedProcess = run(
            ["__build/test/uintfast8max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntFast16Max(self):
        """
        Test that UINT_FAST16_MAX is 65535.
        """
        result: CompletedProcess = run(
            ["__build/test/uintfast16max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntFast32Max(self):
        """
        Test that UINT_FAST32_MAX is 4294967295.
        """
        result: CompletedProcess = run(
            ["__build/test/uintfast32max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntFast64Max(self):
        """
        Test that UINT_FAST64_MAX is 18446744073709551615.
        """
        result: CompletedProcess = run(
            ["__build/test/uintfast64max"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntMaxMin(self):
        """
        Test that INTMAX_MIN is -9223372036854775808.
        """
        result: CompletedProcess = run(
            ["__build/test/intmaxmin"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntMaxMax(self):
        """
        Test that INTMAX_MAX is 9223372036854775807.
        """
        result: CompletedProcess = run(
            ["__build/test/intmaxmax"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntMaxMax(self):
        """
        Test that UINTMAX_MAX is 18446744073709551615.
        """
        result: CompletedProcess = run(
            ["__build/test/uintmaxmax"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntPtrMin(self):
        """
        Test that INTPTR_MIN is -9223372036854775808.
        """
        result: CompletedProcess = run(
            ["__build/test/intptrmin"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testIntPtrMax(self):
        """
        Test that INTPTR_MAX is 9223372036854775807.
        """
        result: CompletedProcess = run(
            ["__build/test/intptrmax"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testUIntPtrMax(self):
        """
        Test that UINTPTR_MAX is 18446744073709551615.
        """
        result: CompletedProcess = run(
            ["__build/test/uintptrmax"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testPtrDiffMin(self):
        """
        Test that PTRDIFF_MIN is -9223372036854775808.
        """
        result: CompletedProcess = run(
            ["__build/test/ptrdiffmin"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")

    def testPtrDiffMax(self):
        """
        Test that PTRDIFF_MAX is 9223372036854775807.
        """
        result: CompletedProcess = run(
            ["__build/test/ptrdiffmax"], capture_output=True, text=True
        )

        stdout: Any = result.stdout
        stderr: Any = result.stderr
        exitCode: int = result.returncode

        self.assertEqual(exitCode, 0)
        self.assertEqual(stdout.strip(), "")
        self.assertEqual(stderr, "")


if __name__ == "__main__":
    unittest.main()

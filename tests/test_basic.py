"""Test di base per Lezione1.

Author: Gianni Corona
"""

import unittest

from lezione1 import __author__, __version__


class ProjectMetadataTests(unittest.TestCase):
    """Verifica i metadati fondamentali del progetto."""

    def test_author(self) -> None:
        self.assertEqual(__author__, "Gianni Corona")

    def test_version(self) -> None:
        self.assertEqual(__version__, "0.3.0")


if __name__ == "__main__":
    unittest.main()

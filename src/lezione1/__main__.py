"""Entry point principale del progetto Lezione1.

Author: Gianni Corona
"""

from . import __author__, __version__


def main() -> None:
    """Esegue il comportamento principale dell'applicazione."""
    print("Ciao Gianni")
    print("Ciao Corona")
    print(f"{__author__} - Agosto 2026 - {__version__}")


if __name__ == "__main__":
    main()

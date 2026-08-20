# Corso Python

**Autore:** Gianni Corona

Progetto didattico Python strutturato con layout `src/` e versionamento SemVer.

## Struttura

```text
Lezione1/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── src/
│   └── lezione1/
│       ├── __init__.py
│       ├── __main__.py
│       └── version.py
└── tests/
    └── test_basic.py
```

La versione del progetto ha una sola fonte di verita in `src/lezione1/version.py`.

## Esecuzione

Dalla root del repository:

```bash
PYTHONPATH=src python -m lezione1
```

Dopo l'installazione del progetto e disponibile anche il comando:

```bash
lezione1
```

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

## Avvio rapido

Windows:

```bat
run-windows.bat
```

Linux:

```bash
./run-linux.sh
```

# AGENTS.md

## Scopo

Questo file definisce le regole operative per gli agenti AI che lavorano su questo repository.
Le istruzioni valgono per l'intero progetto, salvo la presenza di un `AGENTS.md` piu specifico in una sottodirectory.

## Principi di lavoro

- Leggere sempre il contesto esistente prima di modificare file.
- Preferire modifiche piccole, mirate e facilmente verificabili.
- Non cambiare codice o configurazioni non pertinenti alla richiesta.
- Non eliminare o sovrascrivere modifiche dell'utente senza una richiesta esplicita.
- Mantenere compatibilita con il comportamento esistente, salvo diversa indicazione.
- Evitare dipendenze aggiuntive quando la stessa soluzione puo essere realizzata in modo semplice con la libreria standard o con dipendenze gia presenti.
- Non inserire segreti, password, token, chiavi API o credenziali nel repository.

## Struttura e convenzioni del codice

- Usare nomi chiari e descrittivi per file, funzioni, variabili e classi.
- Per Python seguire PEP 8, salvo convenzioni locali piu specifiche.
- Preferire codice semplice e leggibile rispetto a soluzioni eccessivamente astratte.
- Aggiungere commenti solo quando spiegano il perche di una scelta non ovvia.
- Evitare commenti che ripetono semplicemente cio che il codice gia esprime.
- Conservare il formato, lo stile e le convenzioni gia adottate nei file esistenti.

## Modifiche ai file

Prima di modificare un file:

1. Leggere il file interessato e gli eventuali file correlati.
2. Verificare se esistono test o documentazione che descrivono il comportamento atteso.
3. Effettuare la modifica minima necessaria.
4. Verificare il risultato e controllare il diff prima di considerare concluso il lavoro.

## Test e validazione

- Eseguire i test esistenti quando disponibili.
- Per modifiche Python, eseguire almeno un controllo sintattico sui file toccati quando non esiste una suite di test.
- Non dichiarare un test come superato se non e stato realmente eseguito.
- Se un test non puo essere eseguito nell'ambiente disponibile, indicarlo chiaramente.
- Correggere gli errori introdotti dalla modifica prima di procedere al commit.

## Documentazione

- Aggiornare `README.md` o altra documentazione quando una modifica cambia installazione, utilizzo, configurazione o comportamento visibile.
- Mantenere esempi e comandi coerenti con lo stato corrente del progetto.
- Documentare nuove opzioni, parametri o dipendenze rilevanti.

## Git e commit

- Controllare sempre lo stato del repository e il diff prima di creare un commit.
- Ogni commit dovrebbe rappresentare una modifica logica e coerente.
- Usare messaggi di commit brevi ma descrittivi, preferibilmente in forma imperativa.
- Non fare force push, reset distruttivi o riscritture della cronologia senza autorizzazione esplicita.
- Non includere nel commit file temporanei, cache, credenziali o artefatti locali non necessari.
- Quando possibile, mantenere separati cambiamenti funzionali, refactoring e aggiornamenti puramente documentali.

## Versionamento SemVer

Il progetto usa **Semantic Versioning (SemVer)** nel formato:

`MAJOR.MINOR.PATCH`

Esempio: `1.4.2`.

Regole:

- Incrementare `MAJOR` quando vengono introdotte modifiche incompatibili con le versioni precedenti.
- Incrementare `MINOR` quando vengono aggiunte funzionalita compatibili con le versioni precedenti.
- Incrementare `PATCH` quando vengono introdotte correzioni compatibili con le versioni precedenti.
- Le versioni pre-release possono usare suffissi come `-alpha.1`, `-beta.1` o `-rc.1`.
- I tag Git delle release dovrebbero usare il prefisso `v`, ad esempio `v1.2.0`.
- Una nuova release deve avere una versione SemVer coerente con l'impatto delle modifiche introdotte.
- Non modificare retroattivamente il contenuto di una versione gia pubblicata; creare invece una nuova versione.

## Changelog e release

Quando il progetto iniziera a produrre release formali:

- Mantenere un `CHANGELOG.md` con le modifiche rilevanti per ogni versione.
- Raggruppare le modifiche, quando utile, in categorie come Added, Changed, Fixed, Deprecated, Removed e Security.
- Prima di una release verificare test, documentazione, numero di versione e contenuto del changelog.
- Creare il tag Git solo dopo che il commit della release e stato verificato.

## Dipendenze e sicurezza

- Aggiungere dipendenze solo quando realmente necessarie.
- Preferire versioni mantenute e compatibili con il progetto.
- Evitare codice che disabilita controlli di sicurezza o validazioni senza una motivazione esplicita.
- Non stampare nei log informazioni sensibili.

## Comportamento dell'agente

- Se la richiesta e ambigua e la scelta puo cambiare significativamente il risultato, chiedere chiarimenti.
- Per decisioni locali, reversibili e a basso rischio, scegliere una soluzione ragionevole e documentare eventuali assunzioni.
- Segnalare esplicitamente eventuali problemi rilevati che non vengono corretti perche fuori dallo scope della richiesta.
- Al termine del lavoro fornire un riepilogo sintetico delle modifiche e dei test eseguiti.

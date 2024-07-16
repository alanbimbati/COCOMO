# Stima dei costi con il metodo COCOMO

### COCOMO (Constructive Cost Model)

COCOMO, acronimo di Constructive Cost Model, è un modello utilizzato per stimare i costi di sviluppo del software. È stato sviluppato da Barry Boehm nel 1981 presso il TRW Defense Systems Group ed è stato uno dei primi modelli di stima del software ampiamente utilizzati nell'industria.

#### Principi Chiave di COCOMO:

1. **Tipi di Progetto**:
   - **Organico**: Progetti di piccole e medie dimensioni sviluppati da team esperti in un ambiente familiare.
   - **Semi-Distaccato**: Progetti di dimensioni medio-grandi con requisiti parzialmente nuovi e/o team misti di esperienza.
   - **Embedded**: Progetti grandi e complessi spesso sviluppati su contratto per clienti esterni con requisiti significativamente nuovi.

2. **Parametri di Stimatazione**:
   - **KLOC** (Migliaia di Linee di Codice): La dimensione del software stimata in migliaia di linee di codice.
   - **Sforzo**: La quantità di sforzo umano necessaria per sviluppare il software, misurata in mesi-persona.

3. **Costanti COCOMO**:
   - Ogni tipo di progetto (organico, semi-distaccato, embedded) ha costanti associate (a, b) che determinano la relazione tra KLOC e sforzo di sviluppo.

4. **Calcolo dello Sforzo**:
   - Lo sforzo di sviluppo è calcolato utilizzando l'equazione:
     ```
     Sforzo = a * (KLOC)^b
     ```
     dove \( a \) e \( b \) sono costanti specifiche del tipo di progetto.


#### Utilizzo del Codice Python:

Il codice Python fornito implementa una classe `COCOMOCalculator` che fornisce metodi per contare le linee di codice, stimare lo sforzo di sviluppo utilizzando COCOMO e analizzare i progetti in una directory specificata. Ecco una descrizione dei principali metodi:

- `count_lines_and_calculate_cost`: Conta le linee di codice nei file specificati e ne calcola il totale.
- `cocomo`: Metodo statico che calcola lo sforzo di sviluppo utilizzando COCOMO.
- `count_projects`: Conta il numero totale di progetti (cartelle) nella directory principale.
- `count_lines_of_code`: Conta le linee di codice per ogni progetto (cartella) nella directory.
- `analyze_projects`: Analizza i progetti nella directory e restituisce un DataFrame di Pandas con i nomi dei progetti e le linee di codice.

Questo modello consente una stima ragionevole degli sforzi di sviluppo basata sulla dimensione e complessità del codice presente nei progetti. Utilizzare COCOMO può aiutare nella pianificazione più accurata delle risorse umane e temporali necessarie per completare i progetti software.

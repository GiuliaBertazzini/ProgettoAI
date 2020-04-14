# Classificazione di documenti testuali
Lo scopo del progetto è di utilizzare implementazioni di Perceptron per classificare documenti testuali.

# Dataset
I datasets utilizzati possono essere scaricati dai seguenti link:
- 20 newsgroups: http://qwone.com/~jason/20Newsgroups/
- Reuters-21578: http://www.daviddlewis.com/resources/testcollections/reuters21578/

# Requisiti
- scikit-learn
- matplotlib

# Uso del codice
- Eseguire il run sul file preprocessing.py, il quale creerà la cartella data-set in cui sono contenute le 10 categorie più frequenti del dataset reuters-21578, divise in training-set e test-set. 
- Nel file reuters.py modificare il conteiner_path all'interno della funzione load_files(), specificando dove si trova la cartella "data-set" creata precedentemente.
- Eseguire il file main.py, che consente di visualizzare l'accuratezza ottenuta con dei parametri di default (che è possibile eventualmente modificare nei file newsgroups.py e reuters.py). 
-Per visualizzare graficamente i risultati è necessario eseguire il run sui file GraficoEsempi.py e GraficoVocabularySize.py.

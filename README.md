# generateGraph.py

## Description
**generateGraph.py** is a Python script that generates a graph of the French departments according to the results of the presidential elections in a chosen year. The graph represents each department with the order of the candidates according to the votes obtained.

## Requirements
Make sure you have the following items installed on your system :

- Python 3.x

## Installation
Clone this repository or download the source files.
```sh
git clone https://github.com/votre-utilisateur/generateGraph.git
```

## Usage
The **generateGraph.py** script takes as input the year of the presidential elections and generates a graph of the French departments with the order of the candidates according to the votes obtained.

## Syntaxe
```sh
python generateGraph.py <année>
```

For example, to generate the graph for the 2022 presidential elections :
```sh
python generateGraph.py 2022
```

## Structure du projet

│FrenchElectionGraph  
      ├── DataResults  
            ├── extractRankings.py  
            ├── pres1848comm.csv  
            ├── pres1965comm.csv  
            ├── pres1969comm.csv  
            ├── pres1974comm.csv  
            ├── pres1981comm.csv  
            ├── pres1988comm.csv  
            ├── pres1995comm.csv  
            ├── pres2002comm.csv  
            ├── pres2007comm.csv  
            ├── pres2012comm.csv  
            ├── pres2017comm.csv  
            ├── pres2022comm.csv  
            └── resultRankings2022.txt  
      ├── README.md   
      ├── departements-limitrophes-france.txt  
      ├── generateGraph.py  
      └── votePres2022.json

## Authors
Maurand Julia - maurand14000@gmail.com

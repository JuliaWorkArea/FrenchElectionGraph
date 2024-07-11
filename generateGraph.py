import json
import sys
import os

## Demande de la date des présidentielles

## Lancement du calcul des valeurs si non existant pour la date

## Mettre des commentaires et traduire en anglais !!
def createOrder():
    # Check for an argument
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        fileName = 'DataResults/pres'+first_arg+'comm.csv'
        if not os.path.exists(fileName):
            print("The date indicated does not exist in the DataResults folder.")
            exit(2)
        resultsName = 'DataResults/resultRankings'+first_arg+'.txt'
        if not os.path.exists(resultsName):
            os.system('cd DataResults/; python3 extractRankings.py '+first_arg)
    else:
        print("The date of the presidential elections is missing from the argument.")
        exit(1)
    return first_arg

def readFiles(date):
    file1 = open('DataResults/resultRankings'+date+'.txt','r')
    results = file1.readlines()
    file1.close()
    file2 = open('departements-limitrophes-france.txt','r')
    edges = file2.readlines()
    file2.close()
    return (results,edges)

def generateData(resultsData,edgeData):
    ListOfVertices = []
    ListOfEdges = []

    attributsLabel = resultsData[0].split(";")[1::]
    attributsLabel[len(attributsLabel)-1] = attributsLabel[len(attributsLabel)-1].replace("\n","")

    for node in range(0,len(resultsData[1::])):
        NodeLabel = resultsData[node+1].split(",")[0]
        descriptorValues = resultsData[node+1].split(",")[1::]
        descriptorValues[len(descriptorValues)-1] = descriptorValues[len(descriptorValues)-1].replace("\n","")
        descriptorValues = [int(value) for value in descriptorValues]
        ListOfVertices.append({"vertexId":NodeLabel, "descriptorsValues":descriptorValues})

    for edge in edgeData:
        edgeLine = edge.replace("\n","").replace(")","").replace("(","").split(",")
        ListOfEdges.append({"vertexId":edgeLine[0],"connected_vertices":edgeLine[1::]})
    
    return (attributsLabel,ListOfEdges,ListOfVertices)

def writeResults(date,names,edges,vertices):
    ##Integration de la date dans les noms de description et de fichier
    data_set = {"descriptorName": "Department graph with descriptions", "attributesName": names, "vertices": vertices, "edges":edges}
    json_dump = json.dumps(data_set,sort_keys=False, indent='\t', separators=(',', ': '), ensure_ascii=False)
    f = open("votePres"+date+".json", "w")
    f.write(json_dump)

def main():
    date = createOrder()
    results, edges = readFiles(date)
    names,edges,vertices = generateData(results,edges)
    writeResults(date,names,edges,vertices)

main()

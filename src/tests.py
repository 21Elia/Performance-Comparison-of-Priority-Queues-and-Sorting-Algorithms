from heap_priority_queue import MaxHeap
from unsorted_list_priority_queue import UnsortedLinkedListPQ
from sorted_list_priority_queue import SortedLinkedListPQ
import time
import random
import matplotlib.pyplot as plt
import pickle
import pandas as pd

def runTests(sizes, reps, results, structure, structureName):
    values = [random.randint(0, 9999) for _ in range(max(sizes))]
    structure.clear()   
    prevSize = 0
    for size in sizes:
        for value in values[prevSize : size]: # insert subsequent elements from values[prevSize] to values[size]
            structure.insert(value)
        prevSize = size

        insertTimes = []
        peekMaxTimes = []
        extractMaxTimes = []

        for _ in range(reps):
            # peek max
            start = time.perf_counter()
            var = structure.peekMax()
            end = time.perf_counter()
            peekMaxTimes.append(end - start)
            
            # insert
            newValue = random.randint(0, 9999)
            start = time.perf_counter()
            structure.insert(newValue)
            end = time.perf_counter()
            insertTimes.append(end - start)

            # extract max
            start = time.perf_counter()
            structure.extractMax()
            end = time.perf_counter()
            extractMaxTimes.append(end - start)

        averageInsertTime = sum(insertTimes) / len(insertTimes)
        averagePeekMaxTime = sum(peekMaxTimes) / len(peekMaxTimes)
        averageExtractMaxTime = sum(extractMaxTimes) / len(extractMaxTimes)
        results[structureName]["Insert"].append(averageInsertTime * 1000) # in ms
        results[structureName]["Peek Max"].append(averagePeekMaxTime * 1000) # in ms
        results[structureName]["Extract Max"].append(averageExtractMaxTime * 1000) # in ms

def plotComparison(results, sizes, opName):

    plt.figure()
    plt.title(f"{opName} Comparison: Heap, Unsorted List, Sorted List over size n")

    plt.plot(sizes, results["Heap"][opName], label="Heap")
    plt.plot(sizes, results["Unsorted Linked List"][opName], label="Unsorted Linked List")
    plt.plot(sizes, results["Sorted Linked List"][opName], label="Sorted Linked List")

    plt.xlabel("Input size (n)")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.savefig(f"graphs/{opName}-comparison.png")
    plt.show()

def plotStructureGraphs(results, sizes, structureName):
    plt.figure()
    plt.title("Insert in " + structureName)
    plt.plot(sizes, results[structureName]["Insert"], label = structureName)
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (ms)")
    if structureName == "Unsorted Linked List":
        plt.ylim(0, 0.0003)
    plt.legend()
    plt.savefig("graphs/" + structureName + "-" + "insert")

    plt.figure()
    plt.title("Peek Max in " + structureName)
    plt.plot(sizes, results[structureName]["Peek Max"], label = structureName)
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (ms)")
    if structureName == "Heap" or structureName == "Sorted Linked List":
        plt.ylim(0, 0.0003)
    plt.legend()
    plt.savefig("graphs/" + structureName + "-" + "peek-max")

    plt.figure()
    plt.title("Extract Max in " + structureName)
    plt.plot(sizes, results[structureName]["Extract Max"], label = structureName)
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (ms)")
    if structureName == "Sorted Linked List":
        plt.ylim(0, 0.0003)
    plt.legend()
    plt.savefig("graphs/" + structureName + "-" + "extract-max")

    plt.show()

def printTable(results, tableSizes = [101, 1001, 5001, 10001, 20001]):
    data = []
    sizeToIndex = {n: i for i, n in enumerate(sizes)}

    for size in tableSizes:
        if size not in sizeToIndex:
            continue
        index = sizeToIndex[size]
        for structure in results:
            for operation in results[structure]:
                if len(results[structure][operation]) > index:
                    timeMilliseconds= results[structure][operation][index]
                    data.append({
                        "Size": size,
                        "Data Structure": structure,
                        "Operation": operation,
                        "Average Time (ms)": round(timeMilliseconds, 6) 
                    })
    
    df = pd.DataFrame(data)
    print(df.to_string(index = False))



if __name__ == "__main__":
    sizes = []
    for i in range(1, 20002, 20):
        sizes.append(i)

    print(str(sizes))
    reps = 100
    heap = MaxHeap()
    unsortedLinkedList = UnsortedLinkedListPQ()
    sortedLinkedList = SortedLinkedListPQ()
    results = {
        "Heap": {
            "Insert": [],
            "Peek Max": [],
            "Extract Max": []
        },
        "Unsorted Linked List": {
            "Insert": [],
            "Peek Max": [],
            "Extract Max": []
        },
        "Sorted Linked List": {
            "Insert": [],
            "Peek Max": [],
            "Extract Max": []
        }
    }
    

    
    save: bool = False
    if save:
        runTests(sizes, reps, results, heap, "Heap")
        runTests(sizes, reps, results, unsortedLinkedList, "Unsorted Linked List")
        runTests(sizes, reps, results, sortedLinkedList, "Sorted Linked List")
        # SAVE DATA
        with open("results.pkl", "wb") as f:
            pickle.dump((sizes, results), f)


    if not save:
        # LOAD DATA
        with open("results.pkl", "rb") as f:
            sizes, results = pickle.load(f)
        
    printTable(results)

    plotStructureGraphs(results, sizes, "Heap")
    plotStructureGraphs(results, sizes, "Unsorted Linked List")
    plotStructureGraphs(results, sizes, "Sorted Linked List")


    plotComparison(results, sizes, "Insert")
    plotComparison(results, sizes, "Peek Max")
    plotComparison(results, sizes, "Extract Max")
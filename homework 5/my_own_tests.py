import csv
import os
import time

def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output

def row_to_edge(row):
    
	return float(row["Dem"]) - float(row["Rep"])  

def state_edges(election_result_rows):
    """
    Given a list of election result rows, returns state edges.
    The input list does has no duplicate states;
    that is, each state is represented at most once in the input list.
    """
    output = {}
    for i in range(len(election_result_rows)):
        state = election_result_rows[i]['State']
        edge = row_to_edge(election_result_rows[i])
        output.update({state:edge})

    return output

#edges_2008 = state_edges(read_csv("data/2008-results.csv"))

res = read_csv("data/2008-results.csv")

print state_edges(read_csv("data/2008-results.csv"))
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

#res = read_csv("data/2008-results.csv")

#print state_edges(read_csv("data/2008-results.csv"))

poll_rows1 = [{"ID":1, "State":"WA", "Pollster":"A", "Date":"Jan 07 2010"},
              {"ID":2, "State":"WA", "Pollster":"B", "Date":"Mar 21 2010"},
              {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"},
              {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"},
              {"ID":5, "State":"WA", "Pollster":"B", "Date":"Feb 10 2010"},
              {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}]

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if 
    date1 is after date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
	#for index in range(len(poll_rows)):
		# print index, poll_rows1[index]['Date']
		#if earlier_date(poll_rows[index]['Date'], poll_rows[index]['Date']):
		#	print poll_rows[index]['Date']
		#else:
		#	print 'No'
	recentdate = None
	datelist = []
	for index in range(len(poll_rows)):
		if poll_rows[index]['State'] == state and poll_rows[index]['Pollster'] == pollster:
			datelist.append(poll_rows[index]['Date'])
	print datelist
	while len(datelist) > 1:
		if not earlier_date(datelist[0], datelist[1]):
			datelist.remove(datelist[0])
		else:
			print 'Boo'

def test_most_recent_poll_row():
    assert most_recent_poll_row(poll_rows1, "A", "OR") == {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"}
    assert most_recent_poll_row(poll_rows1, "A", "WA") == {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"}
    assert most_recent_poll_row(poll_rows1, "B", "WA") == {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}
    assert most_recent_poll_row(poll_rows1, "B", "OR") == None
    assert most_recent_poll_row(poll_rows1, "DoesNotExist", "DoesNotExist") == None

#print poll_rows1[0]['Date']

#for i in int(poll_rows1['ID']):
#	print poll_rows1[i]['Date']
#test_most_recent_poll_row()

#print earlier_date(poll_rows1)

#for index in range(len(poll_rows1)):
	# print index, poll_rows1[index]['Date']
	#if earlier_date(poll_rows1[index]['Date'], poll_rows1[index]['Date']):
	#	print poll_rows1[index]['Date']

most_recent_poll_row(poll_rows1, 'B', 'WA')

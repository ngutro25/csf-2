from election import *

rows1 = [{'State': 'WA', 
                'Dem': '1.0', 
                'Rep': '0.1', 
                'Date': 'Nov 04 2008', 
                'Pollster': 'PPP'}]

rows3 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
      {'State': 'WA', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'},
      {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'IPSOS'}]

rows4 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'WA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]


poop = unique_column_values(rows3, "Pollster")
states = unique_column_values(rows3, "State")

dd = []
for i in poop:
    for p in states:
        dd.append(most_recent_poll_row(rows3, i, p))

print dd

for i in poop:
    s = {i:dd}
    print s
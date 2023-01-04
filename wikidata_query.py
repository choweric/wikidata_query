# -*- coding: utf-8 -*-
"""
Python script for finding the Wikidata links for a list of words, and output to a CSV file for easy checking
"""

import json
import requests


# Read text files (list of words to search in Wikidata)
f = open('words.txt', encoding = "utf-8")
lines = f.readlines()
f.close()


# Put all words into a list
wordlist = []
for l in lines:
    wordlist.append(l)
    


# Go through each word and query Wikidata through API
output_tofile = ""    

for w in wordlist:
    
    w = w.strip()   #remove any empty character or line breaks
    
    num_result_found = 0    
    out_list = [w]      #out_list represents a row in the output CSV
               
    req = requests.get('https://www.wikidata.org/w/api.php?action=wbsearchentities&language=en&format=json&search=' + w)
    j = json.loads(req.text)
    
    if j["search"]: #if Wikidata returns results         
        
        num_result_found = len(j["search"])        
        
        for s in j["search"]:            
            sid = s['id']            
            #out_list.append("https://www.wikidata.org/wiki/"+sid)
            out_list.append(sid)
       
    
    print("["+str(num_result_found) + " found]  " + ' | '.join(out_list))
    output_tofile = output_tofile + ';'.join(out_list) + '\n' #tab delimited words + url1 + url2 + url3...
    

f = open("output.csv", "w", encoding="utf-8")
f.write(output_tofile)
f.close()






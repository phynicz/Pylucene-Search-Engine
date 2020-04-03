#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"

import sys, os, lucene

from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from datetime import datetime

import mainwindow 

#import pdb; pdb.set_trace()
def run(searcher, analyzer):
    while True:
        print
        print ("Hit enter with no input to quit.")
        with open ('search.txt', 'r') as file:
            query = file.readlines()
            query1= ''.join(query)

        command = query1
        os.remove('search.txt')
        if command == '':
            return

        print
        start = datetime.now()
        print ("Searching for:", command)
        query = QueryParser("contents", analyzer).parse(command)
        scoreDocs = searcher.search(query, 50).scoreDocs
        print ("%s total matching documents." % len(scoreDocs))
        end = datetime.now()            
  

        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            print (doc.get("path"), 'name:', doc.get("name"))
        print('done...')
        print (end - start)     



if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    print ('lucene', lucene.VERSION)
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    directory = SimpleFSDirectory(Paths.get(os.path.join(base_dir, INDEX_DIR)))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer()
    run(searcher, analyzer)
    del searcher
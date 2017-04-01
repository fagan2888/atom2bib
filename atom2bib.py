# -*- coding: utf-8 -*-
"""
Created on Sat Apr 1 2017

@author: vilhuber
"""

# atom2bib.py
# python script to parse an Atom feed and spit out a bib
# no checking done
import feedparser
import re
import sys
import os.path

# test arguments
#print(sys.argv)
#print(len(sys.argv))
if ( len(sys.argv) != 3 ) :
    print("need two arguments")
    print(" - feed URL")
    print(" - output file (bib)")
    print("Good bye")
    exit
else :
    feedURL = sys.argv[1]
    bibFile = sys.argv[2]
    print(" Reading from ",feedURL)
    print(" Creating ",bibFile)
    bibData = open(bibFile, 'w')
    d = feedparser.parse(feedURL)
    #for i in d:
    #    print(i)
    # print(d.title)
    #print(d.entries[1])
    #for i in d.entries:
    #    for j in i:
    #        print(j)
    # loop over entries
    for post in d.entries:
#        print(post.id)
        paperid = post.id.split('/')[4]
        repoid = post.id.split('/')[3]
        bibData.write("@techreport{handle:" \
            + repoid + ":" + paperid + "," + "\n")
        bibData.write("  author={")
        #print(post.authors)
        if ( len(post.authors) == 1 ) :
            bibData.write(post.author + "},")
        else :
            #print(len(post.authors))
            a = post.authors
            #print(a)
            bibData.write(a[0]['name'])
            for i_author in range(1,len(post.authors)):
                bibData.write(" and " + post.authors[i_author]['name'])
            bibData.write("},"+ "\n")
        bibData.write("  title={" + post.title + "},"+ "\n")
        bibData.write("  url={" + post.id + "},"+ "\n")
        bibData.write("  type={Preprint},"+ "\n")
        bibData.write("  institution={" + d['feed']['title'] + "},"+ "\n")
        bibData.write("  number={" + repoid + ":" + paperid + "},"+ "\n")
        bibData.write("  abstract={" + post.summary.split('\n')[2] + "},"+ "\n")
        bibData.write("}" + "\n")

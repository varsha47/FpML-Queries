# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 18:22:27 2019

@author: Varsha Choudhary
title: "FpML queries"
date: "January 22, 2019"
output: csv file
"""


from lxml import etree
import pandas as pd

#importing xml file
path = 'C:/Users/Varsha/Desktop/JOB/project.xml'


#Function to remove the namespace from FpML file
def remove_namespaces_qname(doc, namespaces=None):

    for el in doc.getiterator():

        # clean tag
        q = etree.QName(el.tag)
        if q is not None:
            if namespaces is not None:
                if q.namespace in namespaces:
                    el.tag = q.localname
            else:
                el.tag = q.localname

            # clean attributes
            for a, v in el.items():
                q = etree.QName(a)
                if q is not None:
                    if namespaces is not None:
                        if q.namespace in namespaces:
                            del el.attrib[a]
                            el.attrib[q.localname] = v
                    else:
                        del el.attrib[a]
                        el.attrib[q.localname] = v
    return doc

tree = etree.parse(path)
tree = remove_namespaces_qname(tree)
#namespaces removed

'''
Create three lists to save the output from queries
L1 Question
L2 Query
L3 Output of Query
'''


L1 = []
L2 =[]
L3 =[]

#Getting the values of XPaths for business questions
test = tree.xpath('//party/partyId/text()')
L1.append('name of parties are')
L2.append('//party/partyId/text()')
L3.append(test)

#Getting all the parties involved
test = tree.xpath('*/partyId/text()')
L1.append('name of parties are')
L2.append('*/partyId/text()')
L3.append(test)

#Getting Name of "party 1" involved in transaction
test = tree.xpath('//party[@id="party1"]/partyId/text()')
L1.append('Name of Party 1')
L2.append('//party[@id="party1"]/partyId/text()')
L3.append(test)

"""
#OR
test = tree.xpath('//party/partyId/text()')
L1.append('Name of Party 1')
L2.append('//party/partyId/text()')
L3.append(test)
"""


#Getting the messgaeId attribute of trancation
test = tree.xpath('//messageId/@messageIdScheme')
L1.append('MessageId attribute is')
L2.append('//messageId/@messageIdScheme')
L3.append(test)

#Create a new dataframe and save lists as colums of dataframe df
df = pd.DataFrame({'Count':range(10)})
df['Query'] = pd.Series(L1, index = df.index[:len(L1)])
df['xpath'] = pd.Series(L2, index = df.index[:len(L2)]) 
df['Output'] = pd.Series(L3, index = df.index[:len(L3)]) 

#Print dataframe and export it to system as csv file
print (df)
export_csv = df.to_csv (r'C:\Users\Varsha\Desktop\JOB\FpML_dataframe.csv', index = None, header=True)
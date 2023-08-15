#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 15:18
# @Author  : hxinaa
# @Site    : 
# @File    : xin.py.py
# @Software: PyCharm
import pandas as pd
from py2neo import Graph
import pickle

def rdf():
    df = pd.read_csv('xin_Drugs.csv')
    print df['title']



def drugs_process():
    df = pd.read_csv('Drugs_table1.csv')
    # df = df.dropna(axis='columns', thresh=14000)
    print df.columns
    df = df.apply(lambda s: s.str.replace('"', ''))
    # df.apply(lambda s: s.str.replace("'", ''))
    df.columns = ['id', 'title', 'url', 'Interactions', 'SideEffects', 'Warnings', 'Overdose', 'DrugStatus',
                  'MedicalUse']
    print df.columns
    df.to_csv('xin_Drugs.csv', index=False)
    # df = df.drop(1,axis='columns')
    print df.info()


def health_procsee():
    df = pd.read_csv('Health_table1.csv')
    print df.info()
    df = df.dropna(axis='columns', thresh=1000)
    df = df.apply(lambda s: s.str.replace('"', ''))
    df.columns = [s.replace(' ', '') for s in df.columns]
    # df.apply(lambda s: s.str.replace("'", ''))
    # df.columns = ['id', 'title', 'url', 'Interactions', 'SideEffects', 'Warnings', 'Overdose', 'DrugStatus',
    #               'MedicalUse']
    print df.columns
    df.to_csv('xin_Health.csv', index=False)
    # df = df.drop(1,axis='columns')
    print df.info()


import os
import json


def wiki_process():
    path = '/data/kbc_data/Structured_Relation_And_Final_Triples/wikidata/'
    files = os.listdir(path)
    with open(path + 'xin_wiki.csv', 'w') as f:
        print >> f, 'id,title'
        for file in files:
            if file[0] == 'Q':
                with open(path + file) as data_file:
                    data = json.load(data_file)
                    if 'labels' in data:
                        if 'en' in data['labels']:
                            title = data['labels']['en']['value']

                    try:
                        print>> f, file.split('.')[0] + ',' + title
                    except:
                        print file.split('.')[0] + ',' + title


def wiki_p():
    d = {}
    file = '/data/kbc_data/Structured_Relation_And_Final_Triples/predicate_record.json'
    with open('/data/kbc_data/Structured_Relation_And_Final_Triples/xin_pname.csv', 'w') as f:
        # print >>f, "pid,titles"
        for line in open(file):
            pid = line.split(":")[0][2:-1]
            name = line.split(":")[1][2:-3].split(',')[0].replace('"', '')
            print pid, name
            # print>>f, pid+','+'"'+names.replace('"','').replace(', ',',')+'"'


def insert_db():
    graph = Graph("http://localhost:7474", username="neo4j", password="kbcdata")

def entity_namedict():
    ename_dict = {}
    for f in [open('/data/kbc_data/NER/semistructured/training_with_new_triple/EM_dic2.txt'),open('/data/kbc_data/NER/semistructured/EM_dic.txt')]:
        for line in f:
            data = line.split('\t')
            if len(data)>3:
                name1 = data[0].lower()
                name2 = data[1].lower()
                eid = data[2]
                if name1 not in ename_dict:
                    ename_dict[name1] = set([])
                if name2 not in ename_dict:
                    ename_dict[name2] = set([])
                ename_dict[name1].add(eid)
                ename_dict[name2].add(eid)
            else:
                print data
    # for i in ename_dict:
    #     if len(ename_dict[i])>1:
    #         print i,ename_dict[i]


    with open('/data/kbc_data/kbc/demoweb/ename.dict','wb') as f:
        pickle.dump(ename_dict,f)


def relation_dict():
    rname_dict = {}
    for line in open("/data/kbc_data/kbc/demoweb/toolkit/xin_wikip.csv"):
        if line.find(',"') > 0:
            pid = line.split(',"')[0]
            names = line.split(',"')[1][0:-2].split(',')
            # print pid,names
            for name in names:
                name = name.lower()
                if name not in rname_dict:
                    rname_dict[name] = set([])
                rname_dict[name].add(pid)
    for i in rname_dict:
        if len(rname_dict[i])>1:
            print i,rname_dict[i]
    with open('/data/kbc_data/kbc/demoweb/rname.dict','wb') as f:
        pickle.dump(rname_dict,f)

def rename_dict():
    relnamedict = {}
    for line in open("/data/kbc_data/kbc/demoweb/toolkit/xin_wikip.csv"):
        if line.find(',"') > 0:
            pid = line.split(',"')[0]
            names = line.split(',"')[1][0:-2].split(',')
            # print pid,names
            relnamedict[pid] = names
    # print relnamedict
    with open('/data/kbc_data/kbc/demoweb/rid.dict','wb') as f:
        pickle.dump(relnamedict,f)

if __name__ == '__main__':
    # rename_dict()
    ename = pickle.load(open('/data/kbc_data/kbc/demoweb/ename.dict'))
    rid_dict = pickle.load(open('/data/kbc_data/kbc/demoweb/rid.dict'))
    rname_dict = pickle.load(open('/data/kbc_data/kbc/demoweb/rname.dict'))
    rid = 'G0002'
    print rname_dict['inactive ingredient of']
    if rid in rid_dict:
        # for x in rid_dict[rid]:
        #     print x
        print rid_dict[rid]
    else:
        print "not find"

    print ename['vascular damage']
    #

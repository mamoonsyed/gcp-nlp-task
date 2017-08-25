# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 02:37:04 2017

@author: transmatter

this program takes text files for the standup report samples given by sir zia
and creates a CSV file, tokenizes the sentences from those individual reports 
and saves them to the CSV file.
"""

#from nltk.corpus import wordnet
#syns = wordnet.synsets('program')
#print syns[0].name()

#import nltk

import os.path
import logging
import csv
from nltk.tokenize import sent_tokenize

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


DATA_PATH = 'E:/code/zia-nlp-task/v1beta2/standup-reports/'
SAVE_PATH = 'E:/code/zia-nlp-task/v1beta2/standup-reports/sentences/'

def tokenize(current_text, user_id, report_part):
#     using NLTK to tokenize to extract sentences from text_files
#     'sent' in this program means sentence, and not sentiment
#     using extend instead of append solved the problem for me.
    sent_list=sent_tokenize(current_text)
    for index, item in enumerate(sent_list):
        save_file = SAVE_PATH+str(user_id)+'-'+str(report_part)+'-'+str(index)+'.txt'
        with open(save_file, 'wb') as f:
            f.write(item)
            f.close()

#   for line in sent_list:
#      print line
#   pprint.pprint(sents)
#   print sent_list

# def write_csv(sent_list):
#     sent_file = os.path.join(DATA_PATH, 'sentences.csv')
#     with open(sent_file, 'w') as f:
# #       writer = csv.writer(f, quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         writer = csv.writer(f)
#         for line in sent_list:
#             print line
#            # had to enclose line in [] because every letter was going into a separate column.
#             writer.writerow([line])

user_id = 0
while True:
    report_part = 0
    current_file = DATA_PATH+str(user_id)+'-'+str(report_part)+'.txt'
    file_exists = os.path.isfile(current_file)
    if file_exists:
        logging.debug('entered the first loop\n current filename='+current_file)
        while True:
            current_file = DATA_PATH+str(user_id)+'-'+str(report_part)+'.txt'
            if os.path.isfile(current_file):
                with open (current_file, 'r') as f:
                    current_text = f.read()
                    f.close()
                tokenize(current_text, user_id, report_part)
                report_part += 1
            else:
                break
        user_id += 1
    else:
        break
# write_csv(sent_list)
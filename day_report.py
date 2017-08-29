# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 02:37:04 2017

@author: transmatter

i will code in the ability to save day report for one day in this file.
following code has been copied from sentence.py, because that template suits
the use-case best.
"""

import os.path
import logging

SENT_PATH = 'E:/code/zia-nlp-task/v1beta2/standup-reports/sentences/'

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
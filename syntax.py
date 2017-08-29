# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 02:37:04 2017

@author: transmatter

this program takes sentences from the GCloud storage '/standup-reports/sentence'
folder and applies syntax analysis on it using GCP NLP API. after that we can 
use the dependency edge attribute and tense attribute to find out whether the
task that is being discussed in the sentence belongs in the 'todo' bucket or
'done' bucket.
"""

#from snippets import syntax_file
from snippets import syntax_text
from google.protobuf.json_format import MessageToDict
#from google.protobuf.json_format import MessageToJson

#tokens=syntax_file('gs://transmatter-bucket/standup-reports/sentences/0-0-0.txt')
text='I love shawarma'
tokens=syntax_text(text)

# we no longer need enums
#pos_enum = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
#                'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

for token in tokens:
    pos = token.part_of_speech
    token_dict = MessageToDict(token,
                               including_default_value_fields=True,
                               preserving_proto_field_name=True)

    # we can also convert the protocol buffer object to json using below lines
#    token_json = MessageToJson(token,
#                             including_default_value_fields=True,
#                             preserving_proto_field_name=True)
    print "------------"
    print token_dict
    
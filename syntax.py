#import json
from snippets import syntax_file

tokens=syntax_file('gs://transmatter-bucket/standup-reports/sentences/0-0-0.txt')
#pos_enum = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
#                'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
for token in tokens:
#    data=token.content
#    with open('data.json', 'w') as f:
#        json.dump(data, f)
#    print token
#    print token.text.content
#    print token.lemma
    pos = token.part_of_speech
#    pos_tag=token.part_of_speech.tag
    print "------------"
    print pos.tag
#    print token
#print tokens
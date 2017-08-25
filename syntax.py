import json
#import pprint
from snippets import syntax_file
from google.protobuf.json_format import MessageToDict, MessageToJson



tokens=syntax_file('gs://transmatter-bucket/standup-reports/sentences/0-0-0.txt')
#pos_enum = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
#                'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
for token in tokens:
    pos = token.part_of_speech
    token_dict = MessageToDict(token,
                             including_default_value_fields=True,
                             preserving_proto_field_name=True)
    token_json = MessageToJson(token,
                             including_default_value_fields=True,
                             preserving_proto_field_name=True)
#    data=token.content
#    with open('data.json', 'w') as f:
#        json.dump(data, f)
#    print token
#    print token.text.content
#    print token.lemma
#    pos_tag=token.part_of_speech.tag
    print "------------"
#    pprint.pprint(pos_json)
#    print token_json
#    print token.part_of_speech.tag
#    abc=json.dumps(token_json)/
#    print abc.part_of_speech.tag
    print token_dict['part_of_speech']['tag']
#    print token
#print tokens
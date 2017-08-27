from snippets import syntax_file
from google.protobuf.json_format import MessageToDict, MessageToJson



tokens=syntax_file('gs://transmatter-bucket/standup-reports/sentences/0-0-0.txt')

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

    print token_dict['part_of_speech']['tag']

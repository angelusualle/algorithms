def encode_xml(r):
    mapping = {'family': '1', 'person': '2', 'firstName': '3', 'lastName': '4', 'state': '5'}
    encoded_builder = mapping[r['tag']]
    if 'attributes' in r:
        for att in r['attributes']:
            encoded_builder = ' '.join([encoded_builder, mapping[att[0]], att[1]])
    encoded_builder = ' '.join([encoded_builder, '0'])
    if 'children' in r:
        for child in r['children']:
            encoded_builder = ' '.join([encoded_builder, encode_xml(child)])
    if 'value' in r:
        encoded_builder = ' '.join([encoded_builder, r['value']])
    encoded_builder = ' '.join([encoded_builder, '0'])
    return encoded_builder
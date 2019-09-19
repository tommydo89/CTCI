# Since XML is very verbose, you are given a way of encoding it where each tag gets
# mapped to a pre-defined integer value. The language/grammar is as follows: 
# Element --> Tag Attributes END Children END
# Attribute --> Tag Value
# END --> 0
# Tag --> some predefined mapping to int
# Value --> string value
# For example, the following XML might be converted into the compressed string below (assuming a
# mapping of family -> 1, person ->2, firstName -> 3, lastName -> 4, state
# -> 5).
# <family lastName="McDowell" state="CA">
# <person firstName="Gayle">Some Message</person>
# </family>
# Becomes:
# 1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0
# Write code to print the encoded version of an XML element (passed in Element and Attribute
# objects). 

# we assume this structure for an element:
	# {
	# 	tag: {
	# 		tag_name: ...
	# 		tag_number: ...
	# 	},
	# 	attributes: {
	# 		attribute1: {
	# 			tag_name: ...,
	# 			tag_number: ...,
	# 			value: ...
	# 		},
	# 		attribute2: {
	# 			tag_name: ...,
	# 			tag_number: ...,
	# 			value: ...
	# 		},
	# 		...
	# 	}
	# 	value: ...,
	# 	children: {
	# 		element1: ..., 
	# 		element2: ...,
	# 		...
	# 	}
	# }

def xmlEncoding(element):
	xml_array = []
	xml_array.append(str(element['tag']['tag_number']) + ' ')
	encodeAttributes(xml_array, element['attributes'])
	xml_array.append('0' + ' ')
	encodeValue(xml_array, element)
	if element['children'] != None:
		for child in element['children'].values():
			encodeChild(xml_array, child)
	xml_array.append('0 ')
	return ''.join(xml_array)


def encodeValue(xml_array, element):
	if element['value'] != None:
		xml_array.append(element['value'] + ' ')



def encodeAttributes(xml_array, attributes):
	for attribute in attributes.values():
		xml_array.append(str(attribute['tag_number']) + ' ' + attribute['value'] + ' ')

def encodeChild(xml_array, element):
	xml_array.append(xmlEncoding(element))

# Example

#	MAPPING:
#		family -> 1, person ->2, firstName -> 3, lastName -> 4, state -> 5

#	OBJECT:
# 		<family lastName="McDowell" state="CA">
#		<person firstName="Gayle">Some Message</person>
# 		</family>

#	ANSWER: 
#		1 4 McDowell SCA 0 2 3 Gayle 0 Some Message 0 0
	
xml_obj = {
	'tag': {
		'tag_name': 'family',
		'tag_number': 1
	},
	'attributes': {
		'attribute1': {
			'tag_name': 'lastName',
			'tag_number': 4,
			'value': 'McDowell'
		},
		'attribute2': {
			'tag_name': 'state',
			'tag_number': 5,
			'value': 'CA'
		}
	},
	'value': None,
	'children': {
		'element1': {
			'tag': {
				'tag_name': 'person',
				'tag_number': 2
			},
			'attributes': {
				'attribute1': {
					'tag_name': 'firstName',
					'tag_number': 3,
					'value': 'Gayle'
				}
			},
			'value': 'Some Message',
			'children': None
		}
	}
}
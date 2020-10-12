from encode_xml import encode_xml
import unittest

class Test_Case_Encode_Xml(unittest.TestCase):
    def test_encode_xml(self):
        xml = {
            'tag': 'family',
            'attributes': [('lastName', 'McDowell'), ('state', 'CA')],
            'children': [{
                'tag': 'person',
                'attributes': [('firstName', 'Gayle')],
                'value': 'Some message'
            }]
        }
        self.assertEqual('1 4 McDowell 5 CA 0 2 3 Gayle 0 Some message 0 0', encode_xml(xml))


if __name__ == '__main__':
    unittest.main()
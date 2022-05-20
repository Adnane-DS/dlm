# -*- coding: utf-8 -*-
import unittest
import dlm.models.deep_api as deep_api

class TestModelMethods(unittest.TestCase):
    
    def setUp(self):
        self.meta = deep_api.get_metadata()
        
    def test_model_metadata_type(self):
        """
        Test that get_metadata() returns dict
        """
        self.assertTrue(type(self.meta) is dict)
        
    def test_model_metadata_values(self):
        """
        Test that get_metadata() returns right values (subset)
        """
        self.assertEqual(self.meta['name'].lower().replace('-','_'),
                        'dlm'.lower().replace('-','_'))
        self.assertEqual(self.meta['author'].lower(),
                         'oussayer'.lower())
        self.assertEqual(self.meta['author-email'].lower(),
                         'adnane.oussayer@gmail.com'.lower())
        self.assertEqual(self.meta['license'].lower(), 
                         'MIT'.lower())


if __name__ == '__main__':
    unittest.main()

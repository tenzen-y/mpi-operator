# coding: utf-8

"""
    mpijob

    Python SDK for MPI-Operator  # noqa: E501

    The version of the OpenAPI document: v2beta1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mpijob
from mpijob.models.v1_list import V1List  # noqa: E501
from mpijob.rest import ApiException

class TestV1List(unittest.TestCase):
    """V1List unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1List
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mpijob.models.v1_list.V1List()  # noqa: E501
        if include_optional :
            return V1List(
                api_version = '', 
                items = [
                    mpijob.models.k8s/io/apimachinery/pkg/runtime/raw_extension.k8s.io.apimachinery.pkg.runtime.RawExtension()
                    ], 
                kind = '', 
                metadata = mpijob.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else :
            return V1List(
                items = [
                    mpijob.models.k8s/io/apimachinery/pkg/runtime/raw_extension.k8s.io.apimachinery.pkg.runtime.RawExtension()
                    ],
        )

    def testV1List(self):
        """Test V1List"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

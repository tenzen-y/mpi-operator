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
from mpijob.models.v1_api_versions import V1APIVersions  # noqa: E501
from mpijob.rest import ApiException

class TestV1APIVersions(unittest.TestCase):
    """V1APIVersions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1APIVersions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mpijob.models.v1_api_versions.V1APIVersions()  # noqa: E501
        if include_optional :
            return V1APIVersions(
                api_version = '', 
                kind = '', 
                server_address_by_client_cidrs = [
                    mpijob.models.v1/server_address_by_client_cidr.v1.ServerAddressByClientCIDR(
                        client_cidr = '', 
                        server_address = '', )
                    ], 
                versions = [
                    ''
                    ]
            )
        else :
            return V1APIVersions(
                server_address_by_client_cidrs = [
                    mpijob.models.v1/server_address_by_client_cidr.v1.ServerAddressByClientCIDR(
                        client_cidr = '', 
                        server_address = '', )
                    ],
                versions = [
                    ''
                    ],
        )

    def testV1APIVersions(self):
        """Test V1APIVersions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

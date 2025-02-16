# coding: utf-8

"""
    mpijob

    Python SDK for MPI-Operator  # noqa: E501

    The version of the OpenAPI document: v2beta1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mpijob.configuration import Configuration


class V1TableOptions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'api_version': 'str',
        'include_object': 'str',
        'kind': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'include_object': 'includeObject',
        'kind': 'kind'
    }

    def __init__(self, api_version=None, include_object=None, kind=None, local_vars_configuration=None):  # noqa: E501
        """V1TableOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._include_object = None
        self._kind = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if include_object is not None:
            self.include_object = include_object
        if kind is not None:
            self.kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this V1TableOptions.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1TableOptions.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1TableOptions.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1TableOptions.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def include_object(self):
        """Gets the include_object of this V1TableOptions.  # noqa: E501

        includeObject decides whether to include each object along with its columnar information. Specifying \"None\" will return no object, specifying \"Object\" will return the full object contents, and specifying \"Metadata\" (the default) will return the object's metadata in the PartialObjectMetadata kind in version v1beta1 of the meta.k8s.io API group.  # noqa: E501

        :return: The include_object of this V1TableOptions.  # noqa: E501
        :rtype: str
        """
        return self._include_object

    @include_object.setter
    def include_object(self, include_object):
        """Sets the include_object of this V1TableOptions.

        includeObject decides whether to include each object along with its columnar information. Specifying \"None\" will return no object, specifying \"Object\" will return the full object contents, and specifying \"Metadata\" (the default) will return the object's metadata in the PartialObjectMetadata kind in version v1beta1 of the meta.k8s.io API group.  # noqa: E501

        :param include_object: The include_object of this V1TableOptions.  # noqa: E501
        :type include_object: str
        """

        self._include_object = include_object

    @property
    def kind(self):
        """Gets the kind of this V1TableOptions.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1TableOptions.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1TableOptions.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1TableOptions.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1TableOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1TableOptions):
            return True

        return self.to_dict() != other.to_dict()

#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_servicebusnamespace_info
version_added: '2.9'
short_description: Get Namespace info.
description:
  - Get info of Namespace.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
  namespace_name:
    description:
      - The namespace name
  name:
    description:
      - Resource name
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource type
  location:
    description:
      - The Geo-location where the resource lives
  sku:
    description:
      - Properties of Sku
    suboptions:
      name:
        description:
          - Name of this SKU.
        required: true
      tier:
        description:
          - The billing tier of this particular SKU.
      capacity:
        description:
          - >-
            The specified messaging units for the tier. For Premium tier,
            capacity are 1,2 and 4.
  provisioning_state:
    description:
      - Provisioning state of the namespace.
  created_at:
    description:
      - The time the namespace was created.
  updated_at:
    description:
      - The time the namespace was updated.
  service_bus_endpoint:
    description:
      - Endpoint you can use to perform Service Bus operations.
  metric_id:
    description:
      - Identifier for Azure Insights metrics
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: NameSpaceList
  azure_rm_servicebusnamespace_info: {}
- name: NameSpaceListByResourceGroup
  azure_rm_servicebusnamespace_info:
    resource_group: myResourceGroup
- name: NameSpaceGet
  azure_rm_servicebusnamespace_info:
    resource_group: myResourceGroup
    namespace_name: my
- name: NameSpaceAuthorizationRuleListAll
  azure_rm_servicebusnamespace_info:
    resource_group: myResourceGroup
    namespace_name: my
- name: NameSpaceNetworkRuleSetGet
  azure_rm_servicebusnamespace_info:
    resource_group: myResourceGroup
    namespace_name: my
- name: NameSpaceAuthorizationRuleGet
  azure_rm_servicebusnamespace_info:
    resource_group: myResourceGroup
    namespace_name: my
    name: myAuthorizationRule

'''

RETURN = '''
namespaces:
  description: >-
    A list of dict results where the key is the name of the Namespace and the
    values are the facts for that Namespace.
  returned: always
  type: complex
  contains:
    namespace_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        location:
          description:
            - The Geo-location where the resource lives
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"13","$type":"DictionaryType","valueType":{"$id":"14","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"15","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"16","fixed":false},"deprecated":false}]
          sample: null
        sku:
          description:
            - Properties of Sku
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of this SKU.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - The billing tier of this particular SKU.
              returned: always
              type: str
              sample: null
            capacity:
              description:
                - >-
                  The specified messaging units for the tier. For Premium tier,
                  capacity are 1,2 and 4.
              returned: always
              type: number
              sample: null
        properties:
          description:
            - Properties of the namespace.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMNamespacesInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            namespace_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.namespace_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.tags = None
        self.sku = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMNamespacesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.namespace_name is not None and
            self.name is not None):
            self.results['namespaces'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group is not None and
              self.namespace_name is not None):
            self.results['namespaces'] = self.format_item(self.getnetworkruleset())
        elif (self.resource_group is not None and
              self.namespace_name is not None):
            self.results['namespaces'] = self.format_item(self.listauthorizationrules())
        elif (self.resource_group is not None and
              self.namespace_name is not None):
            self.results['namespaces'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['namespaces'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['namespaces'] = [self.format_item(self.list())]
        return self.results

    def getauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.get_authorization_rule(resource_group_name=self.resource_group,
                                                                          namespace_name=self.namespace_name,
                                                                          authorization_rule_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getnetworkruleset(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.get_network_rule_set(resource_group_name=self.resource_group,
                                                                        namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listauthorizationrules(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.list_authorization_rules(resource_group_name=self.resource_group,
                                                                            namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def get(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.get(resource_group_name=self.resource_group,
                                                       namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMNamespacesInfo()


if __name__ == '__main__':
    main()
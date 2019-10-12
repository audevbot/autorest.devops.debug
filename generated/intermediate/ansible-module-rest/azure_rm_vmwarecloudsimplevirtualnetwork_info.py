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
module: azure_rm_vmwarecloudsimplevirtualnetwork_info
version_added: '2.9'
short_description: Get VirtualNetwork info.
description:
  - Get info of VirtualNetwork.
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  pc_name:
    description:
      - The private cloud name
    required: true
    type: str
  resource_pool_name:
    description:
      - >-
        Resource pool used to derive vSphere cluster which contains virtual
        networks
    type: str
  name:
    description:
      - '{VirtualNetworkName}'
    type: str
  assignable:
    description:
      - can be used in vm creation/deletion
    type: boolean
  id:
    description:
      - 'virtual network id (privateCloudId:vsphereId)'
    type: str
  location:
    description:
      - Azure region
    type: str
  private_cloud_id:
    description:
      - The Private Cloud id
    type: str
  type:
    description:
      - '{resourceProviderNamespace}/{resourceType}'
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListVirtualNetworks
  azure_rm_vmwarecloudsimplevirtualnetwork_info:
    region_id: myLocation
    pc_name: myPrivateCloud
    resource_pool_name: >-
      /subscriptions/{{ subscription_id
      }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name
      }}/privateClouds/{{ private_cloud_name }}/resourcePools/{{
      resource_pool_name }}
- name: GetVirtualNetwork
  azure_rm_vmwarecloudsimplevirtualnetwork_info:
    region_id: myLocation
    pc_name: myPrivateCloud
    name: myVirtualNetwork

'''

RETURN = '''
virtual_networks:
  description: >-
    A list of dict results where the key is the name of the VirtualNetwork and
    the values are the facts for that VirtualNetwork.
  returned: always
  type: complex
  contains:
    virtualnetwork_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        assignable:
          description:
            - can be used in vm creation/deletion
          returned: always
          type: boolean
          sample: null
        id:
          description:
            - 'virtual network id (privateCloudId:vsphereId)'
          returned: always
          type: str
          sample: null
        location:
          description:
            - Azure region
          returned: always
          type: str
          sample: null
        name:
          description:
            - '{VirtualNetworkName}'
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Virtual Network properties
          returned: always
          type: dict
          sample: null
        type:
          description:
            - '{resourceProviderNamespace}/{resourceType}'
          returned: always
          type: str
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMVirtualNetworksInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=true
            ),
            pc_name=dict(
                type='str',
                required=true
            ),
            resource_pool_name=dict(
                type='raw',
                pattern=('//subscriptions/{{ subscription_id }}/providers'
                         '/Microsoft.VMwareCloudSimple/locations/{{ location_name }}'
                         '/privateClouds/{{ private_cloud_name }}/resourcePools/{{ name }}')
            ),
            name=dict(
                type='str'
            )
        )

        self.region_id = None
        self.pc_name = None
        self.resource_pool_name = None
        self.name = None
        self.assignable = None
        self.id = None
        self.location = None
        self.name = None
        self.properties = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualNetworksInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None and
            self.pc_name is not None and
            self.name is not None):
            self.results['virtual_networks'] = self.format_item(self.get())
        elif (self.region_id is not None and
              self.pc_name is not None and
              self.resource_pool_name is not None):
            self.results['virtual_networks'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.VMwareCloudSimple' +
                    '/locations' +
                    '/{{ location_name }}' +
                    '/privateClouds' +
                    '/{{ private_cloud_name }}' +
                    '/virtualNetworks' +
                    '/{{ virtual_network_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ location_name }}', self.location_name)
        self.url = self.url.replace('{{ private_cloud_name }}', self.private_cloud_name)
        self.url = self.url.replace('{{ virtual_network_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.VMwareCloudSimple' +
                    '/locations' +
                    '/{{ location_name }}' +
                    '/privateClouds' +
                    '/{{ private_cloud_name }}' +
                    '/virtualNetworks')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ location_name }}', self.location_name)
        self.url = self.url.replace('{{ private_cloud_name }}', self.private_cloud_name)
        self.url = self.url.replace('{{ virtual_network_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMVirtualNetworksInfo()


if __name__ == '__main__':
    main()

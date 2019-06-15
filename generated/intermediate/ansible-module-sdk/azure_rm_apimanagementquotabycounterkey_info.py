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
module: azure_rm_apimanagementquotabycounterkey_info
version_added: '2.9'
short_description: Get QuotaByCounterKey info.
description:
  - Get info of QuotaByCounterKey.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - The name of the API Management service.
    required: true
  quota_counter_key:
    description:
      - >-
        Quota counter key identifier.This is the result of expression defined in
        counter-key attribute of the quota-by-key policy.For Example, if you
        specify counter-key="boo" in the policy, then it’s accessible by "boo"
        counter key. But if it’s defined as counter-key="@("b"+"a")" then it
        will be accessible by "ba" key
    required: true
  value:
    description:
      - Quota counter values.
    type: list
    suboptions:
      counter_key:
        description:
          - The Key value of the Counter. Must not be empty.
        required: true
      period_key:
        description:
          - >-
            Identifier of the Period for which the counter was collected. Must
            not be empty.
        required: true
      period_start_time:
        description:
          - >-
            The date of the start of Counter Period. The date conforms to the
            following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
            8601 standard.
          - ''
        required: true
      period_end_time:
        description:
          - >-
            The date of the end of Counter Period. The date conforms to the
            following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
            8601 standard.
          - ''
        required: true
      value:
        description:
          - Quota Value Properties
        suboptions:
          calls_count:
            description:
              - Number of times Counter was called.
          kb_transferred:
            description:
              - Data Transferred in KiloBytes.
  count:
    description:
      - Total record count number across all pages.
  next_link:
    description:
      - Next page link if any.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementGetQuotaCounterKeys
  azure_rm_apimanagementquotabycounterkey_info:
    resource_group: myResourceGroup
    name: myService
    quota_counter_key: myQuota

'''

RETURN = '''
quota_by_counter_keys:
  description: >-
    A list of dict results where the key is the name of the QuotaByCounterKey
    and the values are the facts for that QuotaByCounterKey.
  returned: always
  type: complex
  contains:
    quotabycounterkey_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - Quota counter values.
          returned: always
          type: dict
          sample: null
          contains:
            counter_key:
              description:
                - The Key value of the Counter. Must not be empty.
              returned: always
              type: str
              sample: null
            period_key:
              description:
                - >-
                  Identifier of the Period for which the counter was collected.
                  Must not be empty.
              returned: always
              type: str
              sample: null
            period_start_time:
              description:
                - >
                  The date of the start of Counter Period. The date conforms to
                  the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by
                  the ISO 8601 standard.
              returned: always
              type: datetime
              sample: null
            period_end_time:
              description:
                - >
                  The date of the end of Counter Period. The date conforms to
                  the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by
                  the ISO 8601 standard.
              returned: always
              type: datetime
              sample: null
            value:
              description:
                - Quota Value Properties
              returned: always
              type: dict
              sample: null
              contains:
                calls_count:
                  description:
                    - Number of times Counter was called.
                  returned: always
                  type: number
                  sample: null
                kb_transferred:
                  description:
                    - Data Transferred in KiloBytes.
                  returned: always
                  type: number
                  sample: null
        count:
          description:
            - Total record count number across all pages.
          returned: always
          type: number
          sample: null
        next_link:
          description:
            - Next page link if any.
          returned: always
          type: str
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMQuotaByCounterKeysInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            ),
            quota_counter_key=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.name = None
        self.quota_counter_key = None
        self.value = None
        self.count = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMQuotaByCounterKeysInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.quota_counter_key is not None):
            self.results['quota_by_counter_keys'] = self.format_item(self.listbyservice())
        return self.results

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.quota_by_counter_keys.list_by_service(resource_group_name=self.resource_group,
                                                                              service_name=self.name,
                                                                              quota_counter_key=self.quota_counter_key)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMQuotaByCounterKeysInfo()


if __name__ == '__main__':
    main()
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
module: azure_rm_managementgroupsubscription
version_added: '2.9'
short_description: Manage Azure ManagementGroupSubscription instance.
description:
  - 'Create, update and delete instance of Azure ManagementGroupSubscription.'
options:
  group_id:
    description:
      - Management Group ID.
    required: true
  state:
    description:
      - Assert the state of the ManagementGroupSubscription.
      - >-
        Use C(present) to create or update an ManagementGroupSubscription and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: AddSubscriptionToManagementGroup
  azure_rm_managementgroupsubscription:
    group_id: myManagementGroup
- name: DeleteSubscriptionFromManagementGroup
  azure_rm_managementgroupsubscription:
    group_id: myManagementGroup
    state: absent

'''

RETURN = '''
{}

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.managementgroups import ManagementGroupsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagementGroupSubscriptions(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            group_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.group_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagementGroupSubscriptions, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                  supports_check_mode=True,
                                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(ManagementGroupsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if self.location is None:
            self.location = resource_group.location

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.management_group_subscriptions.create(group_id=self.group_id)
            else:
                response = self.mgmt_client.management_group_subscriptions.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagementGroupSubscription instance.')
            self.fail('Error creating the ManagementGroupSubscription instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ManagementGroupSubscription instance {0}'.format(self.))
        try:
            response = self.mgmt_client.management_group_subscriptions.delete(group_id=self.group_id)
        except CloudError as e:
            self.log('Error attempting to delete the ManagementGroupSubscription instance.')
            self.fail('Error deleting the ManagementGroupSubscription instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ManagementGroupSubscription instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.management_group_subscriptions.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagementGroupSubscriptions()


if __name__ == '__main__':
    main()
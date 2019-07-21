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
module: azure_rm_apimanagementsignupsetting
version_added: '2.9'
short_description: Manage Azure SignUpSetting instance.
description:
  - 'Create, update and delete instance of Azure SignUpSetting.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - Resource name.
    type: str
  enabled:
    description:
      - Allow users to sign up on a developer portal.
    type: boolean
  terms_of_service:
    description:
      - Terms of service contract properties.
    type: dict
    suboptions:
      text:
        description:
          - A terms of service text.
        type: str
      enabled:
        description:
          - Display terms of service during a sign-up process.
        type: boolean
      consent_required:
        description:
          - Ask user for consent to the terms of service.
        type: boolean
  id:
    description:
      - Resource ID.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  state:
    description:
      - Assert the state of the SignUpSetting.
      - >-
        Use C(present) to create or update an SignUpSetting and C(absent) to
        delete it.
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
- name: ApiManagementPortalSettingsUpdateSignUp
  azure_rm_apimanagementsignupsetting:
    resource_group: myResourceGroup
    name: myService
    enabled: true
    terms_of_service:
      text: Terms of service text.
      enabled: true
      consent_required: true
- name: ApiManagementPortalSettingsUpdateSignUp
  azure_rm_apimanagementsignupsetting:
    resource_group: myResourceGroup
    name: myService
    enabled: true
    terms_of_service:
      text: Terms of service text.
      enabled: true
      consent_required: true

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type for API Management resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Sign-up settings contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    enabled:
      description:
        - Allow users to sign up on a developer portal.
      returned: always
      type: boolean
      sample: null
    terms_of_service:
      description:
        - Terms of service contract properties.
      returned: always
      type: dict
      sample: null
      contains:
        text:
          description:
            - A terms of service text.
          returned: always
          type: str
          sample: null
        enabled:
          description:
            - Display terms of service during a sign-up process.
          returned: always
          type: boolean
          sample: null
        consent_required:
          description:
            - Ask user for consent to the terms of service.
          returned: always
          type: boolean
          sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSignUpSettings(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='serviceName',
                required=true
            ),
            enabled=dict(
                type='boolean',
                disposition='/properties/*'
            ),
            terms_of_service=dict(
                type='dict',
                disposition='/properties/termsOfService',
                options=dict(
                    text=dict(
                        type='str'
                    ),
                    enabled=dict(
                        type='boolean'
                    ),
                    consent_required=dict(
                        type='boolean',
                        disposition='consentRequired'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMSignUpSettings, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/portalsettings' +
                    '/signup')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("SignUpSetting instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('SignUpSetting instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the SignUpSetting instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('SignUpSetting instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('SignUpSetting instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the SignUpSetting instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the SignUpSetting instance.')
            self.fail('Error creating the SignUpSetting instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the SignUpSetting instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the SignUpSetting instance.')
            self.fail('Error deleting the SignUpSetting instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the SignUpSetting instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("SignUpSetting instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SignUpSetting instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMSignUpSettings()


if __name__ == '__main__':
    main()

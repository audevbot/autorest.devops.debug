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
module: azure_rm_batchcertificate
version_added: '2.9'
short_description: Manage Azure Certificate instance.
description:
  - 'Create, update and delete instance of Azure Certificate.'
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
  account_name:
    description:
      - The name of the Batch account.
    required: true
  name:
    description:
      - >-
        The identifier for the certificate. This must be made up of algorithm
        and thumbprint separated by a dash, and must match the certificate data
        in the request. For example SHA1-a3d1c5.
    required: true
  thumbprint_algorithm:
    description:
      - >-
        This must match the first portion of the certificate name. Currently
        required to be 'SHA1'.
  thumbprint:
    description:
      - This must match the thumbprint from the name.
  format:
    description:
      - >-
        The format of the certificate - either Pfx or Cer. If omitted, the
        default is Pfx.
  data:
    description:
      - The maximum size is 10KB.
    required: true
  password:
    description:
      - >-
        This is required if the certificate format is pfx and must be omitted if
        the certificate format is cer.
  provisioning_state_transition_time:
    description:
      - undefined
  previous_provisioning_state:
    description:
      - The previous provisioned state of the resource
  previous_provisioning_state_transition_time:
    description:
      - undefined
  public_data:
    description:
      - The public key of the certificate.
  delete_certificate_error:
    description:
      - >-
        This is only returned when the certificate provisioningState is
        'Failed'.
    suboptions:
      code:
        description:
          - >-
            An identifier for the error. Codes are invariant and are intended to
            be consumed programmatically.
        required: true
      message:
        description:
          - >-
            A message describing the error, intended to be suitable for display
            in a user interface.
        required: true
      target:
        description:
          - >-
            The target of the particular error. For example, the name of the
            property in error.
      details:
        description:
          - A list of additional details about the error.
        type: list
        suboptions:
          code:
            description:
              - >-
                An identifier for the error. Codes are invariant and are
                intended to be consumed programmatically.
            required: true
          message:
            description:
              - >-
                A message describing the error, intended to be suitable for
                display in a user interface.
            required: true
          target:
            description:
              - >-
                The target of the particular error. For example, the name of the
                property in error.
          details:
            description:
              - A list of additional details about the error.
            type: list
            suboptions:
              code:
                description:
                  - >-
                    An identifier for the error. Codes are invariant and are
                    intended to be consumed programmatically.
                required: true
              message:
                description:
                  - >-
                    A message describing the error, intended to be suitable for
                    display in a user interface.
                required: true
              target:
                description:
                  - >-
                    The target of the particular error. For example, the name of
                    the property in error.
              details:
                description:
                  - A list of additional details about the error.
                type: list
  id:
    description:
      - The ID of the resource.
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
  state:
    description:
      - Assert the state of the Certificate.
      - >-
        Use C(present) to create or update an Certificate and C(absent) to
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
- name: CreateCertificate - Minimal Pfx
  azure_rm_batchcertificate:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myCertificate
    data: MIIJsgIBAzCCCW4GCSqGSIb3DQE...
    password: KG0UY40e...
- name: CreateCertificate - Minimal Cer
  azure_rm_batchcertificate:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myCertificate
    format: Cer
    data: MIICrjCCAZagAwI...
- name: CreateCertificate - Full
  azure_rm_batchcertificate:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myCertificate
    thumbprint_algorithm: SHA1
    thumbprint: 0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E
    format: Pfx
    data: MIIJsgIBAzCCCW4GCSqGSIb3DQE...
    password: KG0UY40e...
- name: UpdateCertificate
  azure_rm_batchcertificate:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myCertificate
    data: MIIJsgIBAzCCCW4GCSqGSIb3DQE...
    password: KG0UY40e...
- name: CertificateDelete
  azure_rm_batchcertificate:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myCertificate
    state: absent

'''

RETURN = '''
id:
  description:
    - The ID of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
etag:
  description:
    - 'The ETag of the resource, used for concurrency statements.'
  returned: always
  type: str
  sample: null
properties:
  description:
    - The properties associated with the certificate.
  returned: always
  type: dict
  sample: null
  contains:
    thumbprint_algorithm:
      description:
        - >-
          This must match the first portion of the certificate name. Currently
          required to be 'SHA1'.
      returned: always
      type: str
      sample: null
    thumbprint:
      description:
        - This must match the thumbprint from the name.
      returned: always
      type: str
      sample: null
    format:
      description:
        - >-
          The format of the certificate - either Pfx or Cer. If omitted, the
          default is Pfx.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: str
      sample: null
    provisioning_state_transition_time:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: datetime
      sample: null
    previous_provisioning_state:
      description:
        - The previous provisioned state of the resource
      returned: always
      type: str
      sample: null
    previous_provisioning_state_transition_time:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: datetime
      sample: null
    public_data:
      description:
        - The public key of the certificate.
      returned: always
      type: str
      sample: null
    delete_certificate_error:
      description:
        - >-
          This is only returned when the certificate provisioningState is
          'Failed'.
      returned: always
      type: dict
      sample: null
      contains:
        code:
          description:
            - >-
              An identifier for the error. Codes are invariant and are intended
              to be consumed programmatically.
          returned: always
          type: str
          sample: null
        message:
          description:
            - >-
              A message describing the error, intended to be suitable for
              display in a user interface.
          returned: always
          type: str
          sample: null
        target:
          description:
            - >-
              The target of the particular error. For example, the name of the
              property in error.
          returned: always
          type: str
          sample: null
        details:
          description:
            - A list of additional details about the error.
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - >-
                  An identifier for the error. Codes are invariant and are
                  intended to be consumed programmatically.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  A message describing the error, intended to be suitable for
                  display in a user interface.
              returned: always
              type: str
              sample: null
            target:
              description:
                - >-
                  The target of the particular error. For example, the name of
                  the property in error.
              returned: always
              type: str
              sample: null
            details:
              description:
                - A list of additional details about the error.
              returned: always
              type: dict
              sample: null
              contains:
                code:
                  description:
                    - >-
                      An identifier for the error. Codes are invariant and are
                      intended to be consumed programmatically.
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - >-
                      A message describing the error, intended to be suitable
                      for display in a user interface.
                  returned: always
                  type: str
                  sample: null
                target:
                  description:
                    - >-
                      The target of the particular error. For example, the name
                      of the property in error.
                  returned: always
                  type: str
                  sample: null
                details:
                  description:
                    - A list of additional details about the error.
                  returned: always
                  type: dict
                  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.batch import BatchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCertificate(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            account_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='certificate_name',
                required=true
            ),
            thumbprint_algorithm=dict(
                type='str',
                disposition='/'
            ),
            thumbprint=dict(
                type='str',
                disposition='/'
            ),
            format=dict(
                type='str',
                disposition='/',
                choices=['Pfx',
                         'Cer']
            ),
            data=dict(
                type='str',
                disposition='/',
                required=true
            ),
            password=dict(
                type='str',
                no_log=True,
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.account_name = None
        self.name = None
        self.id = None
        self.etag = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCertificate, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagement,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

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

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["etag"] = response["etag"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.certificate.create(resource_group_name=self.resource_group,
                                                               account_name=self.account_name,
                                                               certificate_name=self.name,
                                                               parameters=self.body)
            else:
                response = self.mgmt_client.certificate.update(resource_group_name=self.resource_group,
                                                               account_name=self.account_name,
                                                               certificate_name=self.name,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Certificate instance.')
            self.fail('Error creating the Certificate instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Certificate instance {0}'.format(self.))
        try:
            response = self.mgmt_client.certificate.delete(resource_group_name=self.resource_group,
                                                           account_name=self.account_name,
                                                           certificate_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Certificate instance.')
            self.fail('Error deleting the Certificate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Certificate instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.certificate.get(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        certificate_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCertificate()


if __name__ == '__main__':
    main()

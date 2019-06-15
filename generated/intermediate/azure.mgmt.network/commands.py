# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.network._client_factory import cf_network
def load_command_table(self, _):

    network_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.network.operations#ApiManagementOperations.{}',
        client_factory=cf_network)


    with self.command_group('azurefirewalls', network_sdk, client_factory=cf_network) as g:
        g.custom_command('create', 'create_azurefirewalls')
        g.custom_command('delete', 'delete_azurefirewalls')
        g.custom_command('list', 'list_azurefirewalls')
        g.custom_command('show', 'show_azurefirewalls')
    with self.command_group('azurefirewalls', network_sdk, client_factory=cf_network) as g:
        g.custom_command('show', 'show_azurefirewalls')
        g.custom_command('list', 'list_azurefirewalls')
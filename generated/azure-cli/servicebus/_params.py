# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context(' list') as c:
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name.')
        c.argument('location', id_part=None, help='The Geo-location where the resource lives')
        c.argument('tags', id_part=None, help='Resource tags')
        c.argument('sku', id_part=None, help='Properties of Sku')
        c.argument('properties', id_part=None, help='Properties of the namespace.')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the namespace.')
        c.argument('created_at', id_part=None, help='The time the namespace was created.')
        c.argument('updated_at', id_part=None, help='The time the namespace was updated.')
        c.argument('service_bus_endpoint', id_part=None, help='Endpoint you can use to perform Service Bus operations.')
        c.argument('metric_id', id_part=None, help='Identifier for Azure Insights metrics')
        c.argument('id', id_part=None, help='Resource Id')
        c.argument('type', id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus update') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name.')
        c.argument('location', id_part=None, help='The Geo-location where the resource lives')
        c.argument('tags', id_part=None, help='Resource tags')
        c.argument('sku', id_part=None, help='Properties of Sku')
        c.argument('properties', id_part=None, help='Properties of the namespace.')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the namespace.')
        c.argument('created_at', id_part=None, help='The time the namespace was created.')
        c.argument('updated_at', id_part=None, help='The time the namespace was updated.')
        c.argument('service_bus_endpoint', id_part=None, help='Endpoint you can use to perform Service Bus operations.')
        c.argument('metric_id', id_part=None, help='Identifier for Azure Insights metrics')
        c.argument('id', id_part=None, help='Resource Id')
        c.argument('type', id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus authorizationrule list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The authorization rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus authorizationrule show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The authorization rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus disasterrecoveryconfig create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name')
        c.argument('alias', id_part=None, help='The Disaster Recovery configuration name')
        c.argument('properties', id_part=None, help='Properties required to the Create Or Update Alias(Disaster Recovery configurations)')
        c.argument('partner_namespace', id_part=None, help='ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing')
        c.argument('alternate_name', id_part=None, help='Primary/Secondary eventhub namespace name, which is part of GEO DR pairing')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the Alias(Disaster Recovery configuration) - possible values \'Accepted\' or \'Succeeded\' or \'Failed\'')
        c.argument('pending_replication_operations_count', id_part=None, help='Number of entities pending to be replicated.')
        c.argument('role', id_part=None, help='role of namespace in GEO DR - possible values \'Primary\' or \'PrimaryNotReplicating\' or \'Secondary\'')
        c.argument('id', id_part=None, help='Resource Id')
        c.argument('type', id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfig delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name')
        c.argument('alias', id_part=None, help='The Disaster Recovery configuration name')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfig list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name')
        c.argument('alias', id_part=None, help='The Disaster Recovery configuration name')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfig show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name')
        c.argument('alias', id_part=None, help='The Disaster Recovery configuration name')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus disasterrecoveryconfig authorizationrule list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('alias', id_part=None, help='The Disaster Recovery configuration name')
        c.argument('name', id_part=None, help='The authorization rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfig authorizationrule show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('alias', id_part=None, help='The Disaster Recovery configuration name')
        c.argument('name', id_part=None, help='The authorization rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus migrationconfiguration show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The configuration name. Should always be "$default".')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus migrationconfiguration list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The configuration name. Should always be "$default".')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus queue create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The queue name.')
        c.argument('properties', id_part=None, help='Queue Properties')
        c.argument('lock_duration', id_part=None, help='ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.')
        c.argument('max_size_in_megabytes', id_part=None, help='The maximum size of the queue in megabytes, which is the size of memory allocated for the queue. Default is 1024.')
        c.argument('requires_duplicate_detection', id_part=None, help='A value indicating if this queue requires duplicate detection.')
        c.argument('requires_session', id_part=None, help='A value that indicates whether the queue supports the concept of sessions.')
        c.argument('default_message_time_to_live', id_part=None, help='ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('dead_lettering_on_message_expiration', id_part=None, help='A value that indicates whether this queue has dead letter support when a message expires.')
        c.argument('duplicate_detection_history_time_window', id_part=None, help='ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.')
        c.argument('max_delivery_count', id_part=None, help='The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10.')
        c.argument('status', id_part=None, help='Enumerates the possible values for the status of a messaging entity.')
        c.argument('enable_batched_operations', id_part=None, help='Value that indicates whether server-side batched operations are enabled.')
        c.argument('auto_delete_on_idle', id_part=None, help='ISO 8061 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.')
        c.argument('enable_partitioning', id_part=None, help='A value that indicates whether the queue is to be partitioned across multiple message brokers.')
        c.argument('enable_express', id_part=None, help='A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.')
        c.argument('forward_to', id_part=None, help='Queue/Topic name to forward the messages')
        c.argument('forward_dead_lettered_messages_to', id_part=None, help='Queue/Topic name to forward the Dead Letter message')
        c.argument('count_details', id_part=None, help='Message Count Details.')
        c.argument('created_at', id_part=None, help='The exact time the message was created.')
        c.argument('updated_at', id_part=None, help='The exact time the message was updated.')
        c.argument('accessed_at', id_part=None, help='Last time a message was sent, or the last time there was a receive request to this queue.')
        c.argument('size_in_bytes', id_part=None, help='The size of the queue, in bytes.')
        c.argument('message_count', id_part=None, help='The number of messages in the queue.')
        c.argument('id', id_part=None, help='Resource Id')
        c.argument('type', id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus queue delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The queue name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus queue list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The queue name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus queue show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The queue name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus queue authorizationrule list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('queue_name', id_part=None, help='The queue name.')
        c.argument('name', id_part=None, help='The authorization rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus queue authorizationrule show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('queue_name', id_part=None, help='The queue name.')
        c.argument('name', id_part=None, help='The authorization rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus topic create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The topic name.')
        c.argument('properties', id_part=None, help='Properties of topic resource.')
        c.argument('default_message_time_to_live', id_part=None, help='ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('max_size_in_megabytes', id_part=None, help='Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.')
        c.argument('requires_duplicate_detection', id_part=None, help='Value indicating if this topic requires duplicate detection.')
        c.argument('duplicate_detection_history_time_window', id_part=None, help='ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.')
        c.argument('enable_batched_operations', id_part=None, help='Value that indicates whether server-side batched operations are enabled.')
        c.argument('status', id_part=None, help='Enumerates the possible values for the status of a messaging entity.')
        c.argument('support_ordering', id_part=None, help='Value that indicates whether the topic supports ordering.')
        c.argument('auto_delete_on_idle', id_part=None, help='ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.')
        c.argument('enable_partitioning', id_part=None, help='Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.')
        c.argument('enable_express', id_part=None, help='Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.')
        c.argument('size_in_bytes', id_part=None, help='Size of the topic, in bytes.')
        c.argument('created_at', id_part=None, help='Exact time the message was created.')
        c.argument('updated_at', id_part=None, help='The exact time the message was updated.')
        c.argument('accessed_at', id_part=None, help='Last time the message was sent, or a request was received, for this topic.')
        c.argument('subscription_count', id_part=None, help='Number of subscriptions.')
        c.argument('count_details', id_part=None, help='Message count details')
        c.argument('id', id_part=None, help='Resource Id')
        c.argument('type', id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The topic name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The topic name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('name', id_part=None, help='The topic name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus topic authorizationrule list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('name', id_part=None, help='The authorization rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic authorizationrule show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('name', id_part=None, help='The authorization rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus topic subscription create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('name', id_part=None, help='The subscription name.')
        c.argument('properties', id_part=None, help='Properties of subscriptions resource.')
        c.argument('lock_duration', id_part=None, help='ISO 8061 lock duration timespan for the subscription. The default value is 1 minute.')
        c.argument('requires_session', id_part=None, help='Value indicating if a subscription supports the concept of sessions.')
        c.argument('default_message_time_to_live', id_part=None, help='ISO 8061 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.')
        c.argument('dead_lettering_on_filter_evaluation_exceptions', id_part=None, help='Value that indicates whether a subscription has dead letter support on filter evaluation exceptions.')
        c.argument('dead_lettering_on_message_expiration', id_part=None, help='Value that indicates whether a subscription has dead letter support when a message expires.')
        c.argument('duplicate_detection_history_time_window', id_part=None, help='ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.')
        c.argument('max_delivery_count', id_part=None, help='Number of maximum deliveries.')
        c.argument('status', id_part=None, help='Enumerates the possible values for the status of a messaging entity.')
        c.argument('enable_batched_operations', id_part=None, help='Value that indicates whether server-side batched operations are enabled.')
        c.argument('auto_delete_on_idle', id_part=None, help='ISO 8061 timeSpan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.')
        c.argument('forward_to', id_part=None, help='Queue/Topic name to forward the messages')
        c.argument('forward_dead_lettered_messages_to', id_part=None, help='Queue/Topic name to forward the Dead Letter message')
        c.argument('message_count', id_part=None, help='Number of messages.')
        c.argument('created_at', id_part=None, help='Exact time the message was created.')
        c.argument('accessed_at', id_part=None, help='Last time there was a receive request to this subscription.')
        c.argument('updated_at', id_part=None, help='The exact time the message was updated.')
        c.argument('count_details', id_part=None, help='Message count details')
        c.argument('id', id_part=None, help='Resource Id')
        c.argument('type', id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('name', id_part=None, help='The subscription name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('name', id_part=None, help='The subscription name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('name', id_part=None, help='The subscription name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus topic subscription list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('name', id_part=None, help='The subscription name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('name', id_part=None, help='The subscription name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus topic subscription rule create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('subscription_name', id_part=None, help='The subscription name.')
        c.argument('name', id_part=None, help='The rule name.')
        c.argument('properties', id_part=None, help='Properties of Rule resource')
        c.argument('action', id_part=None, help='Represents the filter actions which are allowed for the transformation of a message that have been matched by a filter expression.')
        c.argument('filter_type', id_part=None, help='Filter type that is evaluated against a BrokeredMessage.')
        c.argument('sql_filter', id_part=None, help='Properties of sqlFilter')
        c.argument('correlation_filter', id_part=None, help='Properties of correlationFilter')
        c.argument('id', id_part=None, help='Resource Id')
        c.argument('type', id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription rule delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('subscription_name', id_part=None, help='The subscription name.')
        c.argument('name', id_part=None, help='The rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription rule list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('subscription_name', id_part=None, help='The subscription name.')
        c.argument('name', id_part=None, help='The rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription rule show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('subscription_name', id_part=None, help='The subscription name.')
        c.argument('name', id_part=None, help='The rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus topic subscription rule show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('subscription_name', id_part=None, help='The subscription name.')
        c.argument('name', id_part=None, help='The rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription rule list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('namespace_name', id_part=None, help='The namespace name')
        c.argument('topic_name', id_part=None, help='The topic name.')
        c.argument('subscription_name', id_part=None, help='The subscription name.')
        c.argument('name', id_part=None, help='The rule name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus list') as c:
        c.argument('sku', id_part=None, help='The sku type.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context(' list') as c:
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('servicebus list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='The namespace name')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])
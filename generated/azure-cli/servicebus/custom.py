# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def list_(cmd, client):
    return client.operations.list()


def create_servicebus(cmd, client,
                      resource_group,
                      name,
                      location=None,
                      tags=None,
                      sku=None,
                      properties=None,
                      provisioning_state=None,
                      created_at=None,
                      updated_at=None,
                      service_bus_endpoint=None,
                      metric_id=None,
                      id=None,
                      type=None):
    return client.namespaces.create()


def update_servicebus(cmd, client,
                      resource_group,
                      name,
                      location=None,
                      tags=None,
                      sku=None,
                      properties=None,
                      provisioning_state=None,
                      created_at=None,
                      updated_at=None,
                      service_bus_endpoint=None,
                      metric_id=None,
                      id=None,
                      type=None):
    return client.namespaces.update()


def delete_servicebus(cmd, client,
                      resource_group,
                      name):
    return client.namespaces.delete()


def list_servicebus(cmd, client,
                    resource_group,
                    name):
    return client.namespaces.list()


def show_servicebus(cmd, client,
                    resource_group,
                    name):
    return client.namespaces.show()


def list_servicebus_authorizationrule(cmd, client,
                                      resource_group,
                                      namespace_name,
                                      name):
    return client.namespaces.list()


def show_servicebus_authorizationrule(cmd, client,
                                      resource_group,
                                      namespace_name,
                                      name):
    return client.namespaces.show()


def create_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias,
                                             properties=None,
                                             partner_namespace=None,
                                             alternate_name=None,
                                             provisioning_state=None,
                                             pending_replication_operations_count=None,
                                             role=None,
                                             id=None,
                                             type=None):
    return client.disaster_recovery_configs.create()


def delete_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias):
    return client.disaster_recovery_configs.delete()


def list_servicebus_disasterrecoveryconfig(cmd, client,
                                           resource_group,
                                           name,
                                           alias):
    return client.disaster_recovery_configs.list()


def show_servicebus_disasterrecoveryconfig(cmd, client,
                                           resource_group,
                                           name,
                                           alias):
    return client.disaster_recovery_configs.show()


def list_servicebus_disasterrecoveryconfig_authorizationrule(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             alias,
                                                             name):
    return client.disaster_recovery_configs.list()


def show_servicebus_disasterrecoveryconfig_authorizationrule(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             alias,
                                                             name):
    return client.disaster_recovery_configs.show()


def show_servicebus_migrationconfiguration(cmd, client,
                                           resource_group,
                                           namespace_name,
                                           name):
    return client.migration_configs.show()


def list_servicebus_migrationconfiguration(cmd, client,
                                           resource_group,
                                           namespace_name,
                                           name):
    return client.migration_configs.list()


def create_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            properties=None,
                            lock_duration=None,
                            max_size_in_megabytes=None,
                            requires_duplicate_detection=None,
                            requires_session=None,
                            default_message_time_to_live=None,
                            dead_lettering_on_message_expiration=None,
                            duplicate_detection_history_time_window=None,
                            max_delivery_count=None,
                            status=None,
                            enable_batched_operations=None,
                            auto_delete_on_idle=None,
                            enable_partitioning=None,
                            enable_express=None,
                            forward_to=None,
                            forward_dead_lettered_messages_to=None,
                            count_details=None,
                            created_at=None,
                            updated_at=None,
                            accessed_at=None,
                            size_in_bytes=None,
                            message_count=None,
                            id=None,
                            type=None):
    return client.queues.create()


def delete_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name):
    return client.queues.delete()


def list_servicebus_queue(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.queues.list()


def show_servicebus_queue(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.queues.show()


def list_servicebus_queue_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            queue_name,
                                            name):
    return client.queues.list()


def show_servicebus_queue_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            queue_name,
                                            name):
    return client.queues.show()


def create_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            properties=None,
                            default_message_time_to_live=None,
                            max_size_in_megabytes=None,
                            requires_duplicate_detection=None,
                            duplicate_detection_history_time_window=None,
                            enable_batched_operations=None,
                            status=None,
                            support_ordering=None,
                            auto_delete_on_idle=None,
                            enable_partitioning=None,
                            enable_express=None,
                            size_in_bytes=None,
                            created_at=None,
                            updated_at=None,
                            accessed_at=None,
                            subscription_count=None,
                            count_details=None,
                            id=None,
                            type=None):
    return client.topics.create()


def delete_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name):
    return client.topics.delete()


def list_servicebus_topic(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.topics.list()


def show_servicebus_topic(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.topics.show()


def list_servicebus_topic_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            name):
    return client.topics.list()


def show_servicebus_topic_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            name):
    return client.topics.show()


def create_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name,
                                         properties=None,
                                         lock_duration=None,
                                         requires_session=None,
                                         default_message_time_to_live=None,
                                         dead_lettering_on_filter_evaluation_exceptions=None,
                                         dead_lettering_on_message_expiration=None,
                                         duplicate_detection_history_time_window=None,
                                         max_delivery_count=None,
                                         status=None,
                                         enable_batched_operations=None,
                                         auto_delete_on_idle=None,
                                         forward_to=None,
                                         forward_dead_lettered_messages_to=None,
                                         message_count=None,
                                         created_at=None,
                                         accessed_at=None,
                                         updated_at=None,
                                         count_details=None,
                                         id=None,
                                         type=None):
    return client.subscriptions.create()


def delete_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name):
    return client.subscriptions.delete()


def list_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.list()


def show_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.show()


def list_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.list()


def show_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.show()


def create_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name,
                                              properties=None,
                                              action=None,
                                              filter_type=None,
                                              sql_filter=None,
                                              correlation_filter=None,
                                              id=None,
                                              type=None):
    return client.rules.create()


def delete_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name):
    return client.rules.delete()


def list_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.list()


def show_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.show()


def show_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.show()


def list_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.list()


def list_servicebus(cmd, client,
                    sku):
    return client.regions.list()


def list_(cmd, client):
    return client.premium_messaging_regions.list()


def list_servicebus(cmd, client,
                    resource_group,
                    name):
    return client.event_hubs.list()
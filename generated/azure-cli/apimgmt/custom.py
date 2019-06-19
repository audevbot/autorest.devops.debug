# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api.create()


def update_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api.update()


def delete_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api.delete()


def list_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api.list()


def show_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api.show()


def show_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api.show()


def list_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api.list()


def list_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_revision.list()


def create_apimgmt apis releases(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_release.create()


def update_apimgmt apis releases(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_release.update()


def delete_apimgmt apis releases(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_release.delete()


def list_apimgmt apis releases(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_release.list()


def show_apimgmt apis releases(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_release.show()


def show_apimgmt apis releases(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_release.show()


def list_apimgmt apis releases(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_release.list()


def create_apimgmt apis operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation.create()


def update_apimgmt apis operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation.update()


def delete_apimgmt apis operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation.delete()


def list_apimgmt apis operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation.list()


def show_apimgmt apis operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation.show()


def show_apimgmt apis operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation.show()


def list_apimgmt apis operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation.list()


def create_apimgmt apis operations policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation_policy.create()


def delete_apimgmt apis operations policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation_policy.delete()


def list_apimgmt apis operations policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation_policy.list()


def show_apimgmt apis operations policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation_policy.show()


def show_apimgmt apis operations policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation_policy.show()


def list_apimgmt apis operations policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_operation_policy.list()


def create_apimgmt tags(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tag.create()


def update_apimgmt tags(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tag.update()


def delete_apimgmt tags(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tag.delete()


def list_apimgmt tags(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tag.list()


def show_apimgmt tags(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tag.show()


def list_apimgmt tags apis products operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tag.list()


def show_apimgmt tags apis products operations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tag.show()


def list_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_product.list()


def create_apimgmt apis policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_policy.create()


def delete_apimgmt apis policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_policy.delete()


def list_apimgmt apis policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_policy.list()


def show_apimgmt apis policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_policy.show()


def show_apimgmt apis policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_policy.show()


def list_apimgmt apis policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_policy.list()


def create_apimgmt apis schemas(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_schema.create()


def delete_apimgmt apis schemas(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_schema.delete()


def list_apimgmt apis schemas(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_schema.list()


def show_apimgmt apis schemas(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_schema.show()


def show_apimgmt apis schemas(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_schema.show()


def list_apimgmt apis schemas(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_schema.list()


def create_apimgmt apis diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_diagnostic.create()


def update_apimgmt apis diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_diagnostic.update()


def delete_apimgmt apis diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_diagnostic.delete()


def list_apimgmt apis diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_diagnostic.list()


def show_apimgmt apis diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_diagnostic.show()


def show_apimgmt apis diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_diagnostic.show()


def list_apimgmt apis diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_diagnostic.list()


def create_apimgmt apis issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue.create()


def update_apimgmt apis issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue.update()


def delete_apimgmt apis issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue.delete()


def list_apimgmt apis issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue.list()


def show_apimgmt apis issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue.show()


def show_apimgmt apis issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue.show()


def list_apimgmt apis issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue.list()


def create_apimgmt apis issues comments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_comment.create()


def delete_apimgmt apis issues comments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_comment.delete()


def list_apimgmt apis issues comments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_comment.list()


def show_apimgmt apis issues comments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_comment.show()


def show_apimgmt apis issues comments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_comment.show()


def list_apimgmt apis issues comments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_comment.list()


def create_apimgmt apis issues attachments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_attachment.create()


def delete_apimgmt apis issues attachments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_attachment.delete()


def list_apimgmt apis issues attachments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_attachment.list()


def show_apimgmt apis issues attachments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_attachment.show()


def show_apimgmt apis issues attachments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_attachment.show()


def list_apimgmt apis issues attachments(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_issue_attachment.list()


def create_apimgmt apis tagdescriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_tag_description.create()


def delete_apimgmt apis tagdescriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_tag_description.delete()


def list_apimgmt apis tagdescriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_tag_description.list()


def show_apimgmt apis tagdescriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_tag_description.show()


def show_apimgmt apis tagdescriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_tag_description.show()


def list_apimgmt apis tagdescriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_tag_description.list()


def list_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.operation.list()


def create_apimgmt apiversionsets(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_version_set.create()


def update_apimgmt apiversionsets(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_version_set.update()


def delete_apimgmt apiversionsets(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_version_set.delete()


def list_apimgmt apiversionsets(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_version_set.list()


def show_apimgmt apiversionsets(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_version_set.show()


def show_apimgmt apiversionsets(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_version_set.show()


def list_apimgmt apiversionsets(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_version_set.list()


def create_apimgmt authorizationservers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.authorization_server.create()


def update_apimgmt authorizationservers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.authorization_server.update()


def delete_apimgmt authorizationservers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.authorization_server.delete()


def list_apimgmt authorizationservers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.authorization_server.list()


def show_apimgmt authorizationservers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.authorization_server.show()


def show_apimgmt authorizationservers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.authorization_server.show()


def list_apimgmt authorizationservers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.authorization_server.list()


def create_apimgmt backends(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend.create()


def update_apimgmt backends(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend.update()


def delete_apimgmt backends(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend.delete()


def list_apimgmt backends(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend.list()


def show_apimgmt backends(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend.show()


def show_apimgmt backends(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend.show()


def list_apimgmt backends(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend.list()


def create_apimgmt caches(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.cache.create()


def update_apimgmt caches(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.cache.update()


def delete_apimgmt caches(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.cache.delete()


def list_apimgmt caches(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.cache.list()


def show_apimgmt caches(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.cache.show()


def show_apimgmt caches(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.cache.show()


def list_apimgmt caches(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.cache.list()


def create_apimgmt certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.create()


def delete_apimgmt certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.delete()


def list_apimgmt certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.list()


def show_apimgmt certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.show()


def show_apimgmt certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.show()


def list_apimgmt certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.list()


def list_(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_operations.list()


def list_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_service_skus.list()


def create_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_service.create()


def update_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_service.update()


def delete_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_service.delete()


def list_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_service.list()


def show_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_service.show()


def show_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_service.show()


def list_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_management_service.list()


def create_apimgmt diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.diagnostic.create()


def update_apimgmt diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.diagnostic.update()


def delete_apimgmt diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.diagnostic.delete()


def list_apimgmt diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.diagnostic.list()


def show_apimgmt diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.diagnostic.show()


def show_apimgmt diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.diagnostic.show()


def list_apimgmt diagnostics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.diagnostic.list()


def create_apimgmt templates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.email_template.create()


def update_apimgmt templates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.email_template.update()


def delete_apimgmt templates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.email_template.delete()


def list_apimgmt templates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.email_template.list()


def show_apimgmt templates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.email_template.show()


def show_apimgmt templates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.email_template.show()


def list_apimgmt templates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.email_template.list()


def create_apimgmt groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group.create()


def update_apimgmt groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group.update()


def delete_apimgmt groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group.delete()


def list_apimgmt groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group.list()


def show_apimgmt groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group.show()


def show_apimgmt groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group.show()


def list_apimgmt groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group.list()


def create_apimgmt groups users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group_user.create()


def delete_apimgmt groups users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group_user.delete()


def list_apimgmt groups users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group_user.list()


def list_apimgmt groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.group_user.list()


def create_apimgmt identityproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.identity_provider.create()


def update_apimgmt identityproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.identity_provider.update()


def delete_apimgmt identityproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.identity_provider.delete()


def list_apimgmt identityproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.identity_provider.list()


def show_apimgmt identityproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.identity_provider.show()


def show_apimgmt identityproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.identity_provider.show()


def list_apimgmt identityproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.identity_provider.list()


def show_apimgmt issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.issue.show()


def list_apimgmt issues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.issue.list()


def create_apimgmt loggers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.logger.create()


def update_apimgmt loggers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.logger.update()


def delete_apimgmt loggers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.logger.delete()


def list_apimgmt loggers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.logger.list()


def show_apimgmt loggers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.logger.show()


def show_apimgmt loggers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.logger.show()


def list_apimgmt loggers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.logger.list()


def list_apimgmt locations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.network_status.list()


def create_apimgmt notifications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification.create()


def list_apimgmt notifications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification.list()


def show_apimgmt notifications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification.show()


def show_apimgmt notifications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification.show()


def list_apimgmt notifications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification.list()


def create_apimgmt notifications recipientusers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification_recipient_user.create()


def delete_apimgmt notifications recipientusers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification_recipient_user.delete()


def list_apimgmt notifications recipientusers(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification_recipient_user.list()


def list_apimgmt notifications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification_recipient_user.list()


def create_apimgmt notifications recipientemails(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification_recipient_email.create()


def delete_apimgmt notifications recipientemails(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification_recipient_email.delete()


def list_apimgmt notifications recipientemails(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification_recipient_email.list()


def list_apimgmt notifications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.notification_recipient_email.list()


def create_apimgmt openidconnectproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.open_id_connect_provider.create()


def update_apimgmt openidconnectproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.open_id_connect_provider.update()


def delete_apimgmt openidconnectproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.open_id_connect_provider.delete()


def list_apimgmt openidconnectproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.open_id_connect_provider.list()


def show_apimgmt openidconnectproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.open_id_connect_provider.show()


def show_apimgmt openidconnectproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.open_id_connect_provider.show()


def list_apimgmt openidconnectproviders(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.open_id_connect_provider.list()


def create_apimgmt policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.policy.create()


def delete_apimgmt policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.policy.delete()


def list_apimgmt policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.policy.list()


def show_apimgmt policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.policy.show()


def show_apimgmt policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.policy.show()


def list_apimgmt policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.policy.list()


def list_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.policy_snippet.list()


def create_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.sign_in_settings.create()


def update_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.sign_in_settings.update()


def show_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.sign_in_settings.show()


def show_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.sign_in_settings.show()


def create_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.sign_up_settings.create()


def update_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.sign_up_settings.update()


def show_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.sign_up_settings.show()


def show_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.sign_up_settings.show()


def create_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.delegation_settings.create()


def update_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.delegation_settings.update()


def show_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.delegation_settings.show()


def show_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.delegation_settings.show()


def create_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product.create()


def update_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product.update()


def delete_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product.delete()


def list_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product.list()


def show_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product.show()


def show_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product.show()


def list_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product.list()


def create_apimgmt products apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_api.create()


def delete_apimgmt products apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_api.delete()


def list_apimgmt products apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_api.list()


def list_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_api.list()


def create_apimgmt products groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_group.create()


def delete_apimgmt products groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_group.delete()


def list_apimgmt products groups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_group.list()


def list_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_group.list()


def list_apimgmt products(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_subscriptions.list()


def create_apimgmt products policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_policy.create()


def delete_apimgmt products policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_policy.delete()


def list_apimgmt products policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_policy.list()


def show_apimgmt products policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_policy.show()


def show_apimgmt products policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_policy.show()


def list_apimgmt products policies(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.product_policy.list()


def create_apimgmt properties(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.property.create()


def update_apimgmt properties(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.property.update()


def delete_apimgmt properties(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.property.delete()


def list_apimgmt properties(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.property.list()


def show_apimgmt properties(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.property.show()


def show_apimgmt properties(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.property.show()


def list_apimgmt properties(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.property.list()


def list_apimgmt quotas(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.quota_by_counter_keys.list()


def show_apimgmt quotas periods(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.quota_by_period_keys.show()


def list_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.region.list()


def list_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.reports.list()


def create_apimgmt subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscription.create()


def update_apimgmt subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscription.update()


def delete_apimgmt subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscription.delete()


def list_apimgmt subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscription.list()


def show_apimgmt subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscription.show()


def list_apimgmt subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscription.list()


def show_apimgmt subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscription.show()


def list_apimgmt(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tag_resource.list()


def show_apimgmt tenant(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tenant_access.show()


def show_apimgmt tenant(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.tenant_access_git.show()


def create_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user.create()


def update_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user.update()


def delete_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user.delete()


def list_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user.list()


def show_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user.show()


def show_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user.show()


def list_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user.list()


def list_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user_group.list()


def list_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user_subscription.list()


def list_apimgmt users(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.user_identities.list()


def show_apimgmt apis(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.api_export.show()
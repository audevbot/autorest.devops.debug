# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_automationjob_job(cmd, client,
                             resource_group,
                             automation_account_name,
                             name,
                             properties=None,
                             runbook=None,
                             parameters=None,
                             run_on=None,
                             started_by=None,
                             job_id=None,
                             creation_time=None,
                             status=None,
                             status_details=None,
                             start_time=None,
                             end_time=None,
                             exception=None,
                             last_modified_time=None,
                             last_status_modified_time=None,
                             provisioning_state=None,
                             client_request_id=None,
                             id=None,
                             type=None):
    body={}
    body['properties'] = properties
    body['runbook'] = runbook
    body['parameters'] = parameters
    body['run_on'] = run_on
    body['started_by'] = started_by
    body['job_id'] = job_id
    body['creation_time'] = creation_time
    body['status'] = status
    body['status_details'] = status_details
    body['start_time'] = start_time
    body['end_time'] = end_time
    body['exception'] = exception
    body['last_modified_time'] = last_modified_time
    body['last_status_modified_time'] = last_status_modified_time
    body['provisioning_state'] = provisioning_state
    return client.job.create(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name, parameters=body)


def list_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name):
    body={}
    return client.job.list_by_automation_account(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name)


def show_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name):
    body={}
    return client.job.get(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name)


def show_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name):
    body={}
    return client.job.get(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name)


def list_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name):
    body={}
    return client.job.list_by_automation_account(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name)


def show_automationjob_job_stream(cmd, client,
                                  resource_group,
                                  automation_account_name,
                                  name,
                                  job_stream_id):
    body={}
    return client.job_stream.get(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name, job_stream_id=job_stream_id)


def list_automationjob_job_stream(cmd, client,
                                  resource_group,
                                  automation_account_name,
                                  name,
                                  job_stream_id):
    body={}
    return client.job_stream.list_by_job(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name, job_stream_id=job_stream_id)
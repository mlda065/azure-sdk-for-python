# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportConfigDeliveryDestination(Model):
    """The destination information for the delivery of the report.

    :param subscription_id: The subscription id of the storage account where
     reports will be delivered.
    :type subscription_id: str
    :param resource_group: The resource group of the storage account here
     reports will be delivered.
    :type resource_group: str
    :param storage_account: The storage account here reports will be
     delivered.
    :type storage_account: str
    :param endpoint: The endpoint of the storage service where reports will be
     delivered.
    :type endpoint: str
    :param container: The name of the container where reports will be
     uploaded.
    :type container: str
    :param category: The name of the directory where reports will be uploaded.
    :type category: str
    """

    _validation = {
        'subscription_id': {'required': True},
        'resource_group': {'required': True},
        'storage_account': {'required': True},
        'endpoint': {'required': True},
        'container': {'required': True},
        'category': {'required': True},
    }

    _attribute_map = {
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'storage_account': {'key': 'storageAccount', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'container': {'key': 'container', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
    }

    def __init__(self, subscription_id, resource_group, storage_account, endpoint, container, category):
        super(ReportConfigDeliveryDestination, self).__init__()
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.storage_account = storage_account
        self.endpoint = endpoint
        self.container = container
        self.category = category

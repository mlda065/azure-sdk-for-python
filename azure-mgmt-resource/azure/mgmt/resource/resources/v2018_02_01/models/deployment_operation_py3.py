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


class DeploymentOperation(Model):
    """Deployment operation information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Full deployment operation ID.
    :vartype id: str
    :ivar operation_id: Deployment operation ID.
    :vartype operation_id: str
    :param properties: Deployment properties.
    :type properties:
     ~azure.mgmt.resource.resources.v2018_02_01.models.DeploymentOperationProperties
    """

    _validation = {
        'id': {'readonly': True},
        'operation_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'operation_id': {'key': 'operationId', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'DeploymentOperationProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(DeploymentOperation, self).__init__(**kwargs)
        self.id = None
        self.operation_id = None
        self.properties = properties

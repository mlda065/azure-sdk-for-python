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


class WebMetaTag(Model):
    """Defines a webpage's metadata.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The metadata.
    :vartype name: str
    :ivar content: The name of the metadata.
    :vartype content: str
    """

    _validation = {
        'name': {'readonly': True},
        'content': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
    }

    def __init__(self):
        super(WebMetaTag, self).__init__()
        self.name = None
        self.content = None
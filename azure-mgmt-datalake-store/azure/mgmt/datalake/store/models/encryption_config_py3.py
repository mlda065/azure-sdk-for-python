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


class EncryptionConfig(Model):
    """The encryption configuration for the account.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The type of encryption configuration being used.
     Currently the only supported types are 'UserManaged' and 'ServiceManaged'.
     Possible values include: 'UserManaged', 'ServiceManaged'
    :type type: str or ~azure.mgmt.datalake.store.models.EncryptionConfigType
    :param key_vault_meta_info: The Key Vault information for connecting to
     user managed encryption keys.
    :type key_vault_meta_info:
     ~azure.mgmt.datalake.store.models.KeyVaultMetaInfo
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'EncryptionConfigType'},
        'key_vault_meta_info': {'key': 'keyVaultMetaInfo', 'type': 'KeyVaultMetaInfo'},
    }

    def __init__(self, *, type, key_vault_meta_info=None, **kwargs) -> None:
        super(EncryptionConfig, self).__init__(**kwargs)
        self.type = type
        self.key_vault_meta_info = key_vault_meta_info

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

from enum import Enum


class ProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    succeeded = "Succeeded"
    failed = "Failed"
    deleting = "Deleting"


class ProvisioningErrorCode(str, Enum):

    bad_source_type = "BadSourceType"
    bad_pir_source = "BadPIRSource"
    bad_iso_source = "BadISOSource"
    bad_managed_image_source = "BadManagedImageSource"
    bad_shared_image_version_source = "BadSharedImageVersionSource"
    bad_customizer_type = "BadCustomizerType"
    unsupported_customizer_type = "UnsupportedCustomizerType"
    no_customizer_script = "NoCustomizerScript"
    bad_distribute_type = "BadDistributeType"
    bad_shared_image_distribute = "BadSharedImageDistribute"
    server_error = "ServerError"
    other = "Other"


class RunState(str, Enum):

    running = "Running"
    succeeded = "Succeeded"
    partially_succeeded = "PartiallySucceeded"
    failed = "Failed"


class RunSubState(str, Enum):

    queued = "Queued"
    building = "Building"
    customizing = "Customizing"
    distributing = "Distributing"


class ResourceIdentityType(str, Enum):

    user_assigned = "UserAssigned"
    none = "None"

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


class JobCreateParameters(Model):
    """Job creation parameters.

    All required parameters must be populated in order to send to Azure.

    :param scheduling_priority: Scheduling priority. Scheduling priority
     associated with the job. Possible values: low, normal, high. Possible
     values include: 'low', 'normal', 'high'. Default value: "normal" .
    :type scheduling_priority: str or ~azure.mgmt.batchai.models.JobPriority
    :param cluster: Required. Cluster. Resource ID of the cluster on which
     this job will run.
    :type cluster: ~azure.mgmt.batchai.models.ResourceId
    :param mount_volumes: Mount volumes. Information on mount volumes to be
     used by the job. These volumes will be mounted before the job execution
     and will be unmouted after the job completion. The volumes will be mounted
     at location specified by $AZ_BATCHAI_JOB_MOUNT_ROOT environment variable.
    :type mount_volumes: ~azure.mgmt.batchai.models.MountVolumes
    :param node_count: Required. Node count. Number of compute nodes to run
     the job on. The job will be gang scheduled on that many compute nodes.
    :type node_count: int
    :param container_settings: Container settings. Docker container settings
     for the job. If not provided, the job will run directly on the node.
    :type container_settings: ~azure.mgmt.batchai.models.ContainerSettings
    :param cntk_settings: CNTK settings. Settings for CNTK (aka Microsoft
     Cognitive Toolkit) job.
    :type cntk_settings: ~azure.mgmt.batchai.models.CNTKsettings
    :param py_torch_settings: pyTorch settings. Settings for pyTorch job.
    :type py_torch_settings: ~azure.mgmt.batchai.models.PyTorchSettings
    :param tensor_flow_settings: TensorFlow settings. Settings for Tensor Flow
     job.
    :type tensor_flow_settings: ~azure.mgmt.batchai.models.TensorFlowSettings
    :param caffe_settings: Caffe settings. Settings for Caffe job.
    :type caffe_settings: ~azure.mgmt.batchai.models.CaffeSettings
    :param caffe2_settings: Caffe2 settings. Settings for Caffe2 job.
    :type caffe2_settings: ~azure.mgmt.batchai.models.Caffe2Settings
    :param chainer_settings: Chainer settings. Settings for Chainer job.
    :type chainer_settings: ~azure.mgmt.batchai.models.ChainerSettings
    :param custom_toolkit_settings: Custom tool kit job. Settings for custom
     tool kit job.
    :type custom_toolkit_settings:
     ~azure.mgmt.batchai.models.CustomToolkitSettings
    :param custom_mpi_settings: Custom MPI settings. Settings for custom MPI
     job.
    :type custom_mpi_settings: ~azure.mgmt.batchai.models.CustomMpiSettings
    :param horovod_settings: Horovod settings. Settings for Horovod job.
    :type horovod_settings: ~azure.mgmt.batchai.models.HorovodSettings
    :param job_preparation: Job preparation. A command line to be executed on
     each node allocated for the job before tool kit is launched.
    :type job_preparation: ~azure.mgmt.batchai.models.JobPreparation
    :param std_out_err_path_prefix: Required. Standard output path prefix. The
     path where the Batch AI service will store stdout, stderror and execution
     log of the job.
    :type std_out_err_path_prefix: str
    :param input_directories: Input directories. A list of input directories
     for the job.
    :type input_directories: list[~azure.mgmt.batchai.models.InputDirectory]
    :param output_directories: Output directories. A list of output
     directories for the job.
    :type output_directories: list[~azure.mgmt.batchai.models.OutputDirectory]
    :param environment_variables: Environment variables. A list of user
     defined environment variables which will be setup for the job.
    :type environment_variables:
     list[~azure.mgmt.batchai.models.EnvironmentVariable]
    :param secrets: Secrets. A list of user defined environment variables with
     secret values which will be setup for the job. Server will never report
     values of these variables back.
    :type secrets:
     list[~azure.mgmt.batchai.models.EnvironmentVariableWithSecretValue]
    :param constraints: Constraints associated with the Job.
    :type constraints: ~azure.mgmt.batchai.models.JobBasePropertiesConstraints
    """

    _validation = {
        'cluster': {'required': True},
        'node_count': {'required': True},
        'std_out_err_path_prefix': {'required': True},
    }

    _attribute_map = {
        'scheduling_priority': {'key': 'properties.schedulingPriority', 'type': 'str'},
        'cluster': {'key': 'properties.cluster', 'type': 'ResourceId'},
        'mount_volumes': {'key': 'properties.mountVolumes', 'type': 'MountVolumes'},
        'node_count': {'key': 'properties.nodeCount', 'type': 'int'},
        'container_settings': {'key': 'properties.containerSettings', 'type': 'ContainerSettings'},
        'cntk_settings': {'key': 'properties.cntkSettings', 'type': 'CNTKsettings'},
        'py_torch_settings': {'key': 'properties.pyTorchSettings', 'type': 'PyTorchSettings'},
        'tensor_flow_settings': {'key': 'properties.tensorFlowSettings', 'type': 'TensorFlowSettings'},
        'caffe_settings': {'key': 'properties.caffeSettings', 'type': 'CaffeSettings'},
        'caffe2_settings': {'key': 'properties.caffe2Settings', 'type': 'Caffe2Settings'},
        'chainer_settings': {'key': 'properties.chainerSettings', 'type': 'ChainerSettings'},
        'custom_toolkit_settings': {'key': 'properties.customToolkitSettings', 'type': 'CustomToolkitSettings'},
        'custom_mpi_settings': {'key': 'properties.customMpiSettings', 'type': 'CustomMpiSettings'},
        'horovod_settings': {'key': 'properties.horovodSettings', 'type': 'HorovodSettings'},
        'job_preparation': {'key': 'properties.jobPreparation', 'type': 'JobPreparation'},
        'std_out_err_path_prefix': {'key': 'properties.stdOutErrPathPrefix', 'type': 'str'},
        'input_directories': {'key': 'properties.inputDirectories', 'type': '[InputDirectory]'},
        'output_directories': {'key': 'properties.outputDirectories', 'type': '[OutputDirectory]'},
        'environment_variables': {'key': 'properties.environmentVariables', 'type': '[EnvironmentVariable]'},
        'secrets': {'key': 'properties.secrets', 'type': '[EnvironmentVariableWithSecretValue]'},
        'constraints': {'key': 'properties.constraints', 'type': 'JobBasePropertiesConstraints'},
    }

    def __init__(self, **kwargs):
        super(JobCreateParameters, self).__init__(**kwargs)
        self.scheduling_priority = kwargs.get('scheduling_priority', "normal")
        self.cluster = kwargs.get('cluster', None)
        self.mount_volumes = kwargs.get('mount_volumes', None)
        self.node_count = kwargs.get('node_count', None)
        self.container_settings = kwargs.get('container_settings', None)
        self.cntk_settings = kwargs.get('cntk_settings', None)
        self.py_torch_settings = kwargs.get('py_torch_settings', None)
        self.tensor_flow_settings = kwargs.get('tensor_flow_settings', None)
        self.caffe_settings = kwargs.get('caffe_settings', None)
        self.caffe2_settings = kwargs.get('caffe2_settings', None)
        self.chainer_settings = kwargs.get('chainer_settings', None)
        self.custom_toolkit_settings = kwargs.get('custom_toolkit_settings', None)
        self.custom_mpi_settings = kwargs.get('custom_mpi_settings', None)
        self.horovod_settings = kwargs.get('horovod_settings', None)
        self.job_preparation = kwargs.get('job_preparation', None)
        self.std_out_err_path_prefix = kwargs.get('std_out_err_path_prefix', None)
        self.input_directories = kwargs.get('input_directories', None)
        self.output_directories = kwargs.get('output_directories', None)
        self.environment_variables = kwargs.get('environment_variables', None)
        self.secrets = kwargs.get('secrets', None)
        self.constraints = kwargs.get('constraints', None)

"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from comfydeploy import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostV1MachinesRequestBody:
    default_machine: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_machine'), 'exclude': lambda f: f is None }})
    



class PostV1MachinesType(str, Enum):
    COMFY_DEPLOY_SERVERLESS = 'comfy-deploy-serverless'


class PostV1MachinesStatus(str, Enum):
    BUILDING = 'building'


class PostV1MachinesGpu(str, Enum):
    A10_G = 'A10G'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostV1MachinesResponseBody:
    r"""Machine created successfully"""
    UNSET='__SPEAKEASY_UNSET__'
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    org_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})
    endpoint: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at') }})
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    type: PostV1MachinesType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    status: PostV1MachinesStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    machine_version: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('machine_version') }})
    machine_builder_version: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('machine_builder_version') }})
    models: List[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('models') }})
    gpu: PostV1MachinesGpu = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gpu') }})
    pod_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pod_id') }})
    base_docker_image: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_docker_image') }})
    allow_concurrent_inputs: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allow_concurrent_inputs') }})
    concurrency_limit: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('concurrency_limit') }})
    legacy_mode: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legacy_mode') }})
    ws_timeout: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ws_timeout') }})
    run_timeout: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run_timeout') }})
    idle_timeout: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('idle_timeout') }})
    build_machine_instance_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('build_machine_instance_id') }})
    build_log: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('build_log') }})
    modal_app_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modal_app_id') }})
    target_workflow_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_workflow_id') }})
    install_custom_node_with_gpu: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('install_custom_node_with_gpu') }})
    deleted: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted') }})
    keep_warm: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keep_warm') }})
    allow_background_volume_commits: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allow_background_volume_commits') }})
    gpu_workspace: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gpu_workspace') }})
    snapshot: Optional[Any] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('snapshot'), 'exclude': lambda f: f is PostV1MachinesResponseBody.UNSET }})
    ws_gpu: Optional[Any] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ws_gpu'), 'exclude': lambda f: f is PostV1MachinesResponseBody.UNSET }})
    object_info: Optional[Any] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_info'), 'exclude': lambda f: f is PostV1MachinesResponseBody.UNSET }})
    dependencies: Optional[Any] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dependencies'), 'exclude': lambda f: f is PostV1MachinesResponseBody.UNSET }})
    extra_docker_commands: Optional[Any] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extra_docker_commands'), 'exclude': lambda f: f is PostV1MachinesResponseBody.UNSET }})
    docker_command_steps: Optional[Any] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('docker_command_steps'), 'exclude': lambda f: f is PostV1MachinesResponseBody.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostV1MachinesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[PostV1MachinesResponseBody] = dataclasses.field(default=None)
    r"""Machine created successfully"""
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from comfydeploy import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class WorkflowJSON:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostV1WorkflowsRequestBody:
    workflow_name: Optional[str] = dataclasses.field(default='new workflow', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow_name'), 'exclude': lambda f: f is None }})
    workflow_json: Optional[WorkflowJSON] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow_json'), 'exclude': lambda f: f is None }})
    create_machine: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('create_machine'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostV1WorkflowsResponseBody:
    r"""Workflow created successfully"""
    workflow_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow_id') }})
    workflow_version: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow_version') }})
    machine_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('machine_id'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostV1WorkflowsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[PostV1WorkflowsResponseBody] = dataclasses.field(default=None)
    r"""Workflow created successfully"""
    

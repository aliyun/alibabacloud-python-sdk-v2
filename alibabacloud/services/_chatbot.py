# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, \
    _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _CHATBOTResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'chatbot', _client=_client)
        self.categories = _create_special_resource_collection(
            _CHATBOTCategoryResource, _client, _client.query_categories,
            'Categories.Category', 'CategoryId',
        )
        self.core_words = _create_resource_collection(
            _CHATBOTCoreWordResource, _client, _client.query_core_words,
            'CoreWords.CoreWord', 'CoreWordName',
        )
        self.dialogs = _create_resource_collection(
            _CHATBOTDialogResource, _client, _client.query_dialogs,
            'Dialogs.Dialog', 'DialogId',
        )
        self.entities = _create_resource_collection(
            _CHATBOTEntityResource, _client, _client.query_entities,
            'Entities.Entity', 'EntityId',
        )
        self.intents = _create_resource_collection(
            _CHATBOTIntentResource, _client, _client.query_intents,
            'Intents.Intent', 'IntentId',
        )
        self.knowledges = _create_resource_collection(
            _CHATBOTKnowledgeResource, _client, _client.query_knowledges,
            'Knowledges.Knowledge', 'KnowledgeId',
        )
        self.knowledges = _create_resource_collection(
            _CHATBOTKnowledgeResource, _client, _client.query_knowledges,
            'Knowledges.Knowledge', 'KnowledgeId',
        )
        self.perspectives = _create_special_resource_collection(
            _CHATBOTPerspectiveResource, _client, _client.query_perspectives,
            'Perspectives.Perspective', 'PerspectiveId',
        )

    def create_category(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_category(**_params)
        category_id = _new_get_key_in_response(response, 'CategoryId')
        return _CHATBOTCategoryResource(category_id, _client=self._client)

    def create_core_word(self, **params):
        _params = _transfer_params(params)
        self._client.create_core_word(**_params)
        core_word_name = _params.get("core_word_name")
        return _CHATBOTCoreWordResource(core_word_name, _client=self._client)

    def create_dialog(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_dialog(**_params)
        dialog_id = _new_get_key_in_response(response, 'DialogId')
        return _CHATBOTDialogResource(dialog_id, _client=self._client)

    def create_entity(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_entity(**_params)
        entity_id = _new_get_key_in_response(response, 'EntityId')
        return _CHATBOTEntityResource(entity_id, _client=self._client)

    def delete_entity(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_entity(**_params)
        entity_id = _new_get_key_in_response(response, 'EntityId')
        return _CHATBOTEntityResource(entity_id, _client=self._client)

    def update_entity(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_entity(**_params)
        entity_id = _new_get_key_in_response(response, 'EntityId')
        return _CHATBOTEntityResource(entity_id, _client=self._client)

    def create_intent(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_intent(**_params)
        intent_id = _new_get_key_in_response(response, 'IntentId')
        return _CHATBOTIntentResource(intent_id, _client=self._client)

    def delete_intent(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_intent(**_params)
        intent_id = _new_get_key_in_response(response, 'IntentId')
        return _CHATBOTIntentResource(intent_id, _client=self._client)

    def update_intent(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_intent(**_params)
        intent_id = _new_get_key_in_response(response, 'IntentId')
        return _CHATBOTIntentResource(intent_id, _client=self._client)

    def create_knowledge(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_knowledge(**_params)
        knowledge_id = _new_get_key_in_response(response, 'KnowledgeId')
        return _CHATBOTKnowledgeResource(knowledge_id, _client=self._client)

    def update_knowledge(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_knowledge(**_params)
        knowledge_id = _new_get_key_in_response(response, 'KnowledgeId')
        return _CHATBOTKnowledgeResource(knowledge_id, _client=self._client)

    def create_perspective(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_perspective(**_params)
        perspective_id = _new_get_key_in_response(response, 'PerspectiveId')
        return _CHATBOTPerspectiveResource(perspective_id, _client=self._client)


class _CHATBOTCategoryResource(ServiceResource):

    def __init__(self, category_id, _client=None):
        ServiceResource.__init__(self, "chatbot.category", _client=_client)
        self.category_id = category_id

        self.childrens = None
        self.name = None
        self.parent_category_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_category(category_id=self.category_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_category(category_id=self.category_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_category(category_id=self.category_id, **_params)


class _CHATBOTCoreWordResource(ServiceResource):

    def __init__(self, core_word_name, _client=None):
        ServiceResource.__init__(self, "chatbot.core_word", _client=_client)
        self.core_word_name = core_word_name

        self.core_word_code = None
        self.create_time = None
        self.modify_time = None
        self.synonyms = None

    def add_synonym(self, **params):
        _params = _transfer_params(params)
        return self._client.add_synonym(core_word_name=self.core_word_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_core_word(core_word_name=self.core_word_name, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_core_word(core_word_name=self.core_word_name, **_params)

    def remove_synonym(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_synonym(core_word_name=self.core_word_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_core_word(core_word_name=self.core_word_name, **_params)


class _CHATBOTDialogResource(ServiceResource):

    def __init__(self, dialog_id, _client=None):
        ServiceResource.__init__(self, "chatbot.dialog", _client=_client)
        self.dialog_id = dialog_id

        self.create_time = None
        self.create_user_id = None
        self.create_user_name = None
        self.description = None
        self.dialog_name = None
        self.is_online = None
        self.is_sample_dialog = None
        self.modify_time = None
        self.modify_user_id = None
        self.modify_user_name = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_dialog(dialog_id=self.dialog_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dialog(dialog_id=self.dialog_id, **_params)

    def describe_dialog_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dialog_flow(dialog_id=self.dialog_id, **_params)

    def disable_dialog_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_dialog_flow(dialog_id=self.dialog_id, **_params)

    def publish_dialog_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.publish_dialog_flow(dialog_id=self.dialog_id, **_params)

    def test_dialog_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.test_dialog_flow(dialog_id=self.dialog_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_dialog(dialog_id=self.dialog_id, **_params)

    def update_dialog_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.update_dialog_flow(dialog_id=self.dialog_id, **_params)


class _CHATBOTEntityResource(ServiceResource):

    def __init__(self, entity_id, _client=None):
        ServiceResource.__init__(self, "chatbot.entity", _client=_client)
        self.entity_id = entity_id

        self.create_time = None
        self.create_user_id = None
        self.create_user_name = None
        self.entity_name = None
        self.entity_type = None
        self.members = None
        self.modify_time = None
        self.modify_user_id = None
        self.modify_user_name = None
        self.regex = None

    def append_entity_member(self, **params):
        _params = _transfer_params(params)
        return self._client.append_entity_member(entity_id=self.entity_id, **_params)

    def describe_entities(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_entities(entity_id=self.entity_id, **_params)

    def remove_entity_member(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_entity_member(entity_id=self.entity_id, **_params)


class _CHATBOTIntentResource(ServiceResource):

    def __init__(self, intent_id, _client=None):
        ServiceResource.__init__(self, "chatbot.intent", _client=_client)
        self.intent_id = intent_id

        self.create_time = None
        self.create_user_id = None
        self.create_user_name = None
        self.modify_time = None
        self.modify_user_id = None
        self.modify_user_name = None
        self.name = None
        self.rule_check = None
        self.slot = None
        self.user_say = None

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_intent(intent_id=self.intent_id, **_params)


class _CHATBOTKnowledgeResource(ServiceResource):

    def __init__(self, knowledge_id, _client=None):
        ServiceResource.__init__(self, "chatbot.knowledge", _client=_client)
        self.knowledge_id = knowledge_id

        self.outline_id = None
        self.title = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_knowledge(knowledge_id=self.knowledge_id, **_params)

    def disable(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_knowledge(knowledge_id=self.knowledge_id, **_params)

    def publish(self, **params):
        _params = _transfer_params(params)
        return self._client.publish_knowledge(knowledge_id=self.knowledge_id, **_params)

    def move_knowledge_category(self, **params):
        _params = _transfer_params(params)
        return self._client.move_knowledge_category(knowledge_id=self.knowledge_id, **_params)


class _CHATBOTPerspectiveResource(ServiceResource):

    def __init__(self, perspective_id, _client=None):
        ServiceResource.__init__(self, "chatbot.perspective", _client=_client)
        self.perspective_id = perspective_id

        self.create_time = None
        self.create_user_name = None
        self.modify_time = None
        self.modify_user_name = None
        self.name = None
        self.perspective_code = None
        self.self_define = None
        self.status = None

    def activate(self, **params):
        _params = _transfer_params(params)
        return self._client.activate_perspective(perspective_id=self.perspective_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_perspective(perspective_id=self.perspective_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_perspective(perspective_id=self.perspective_id, **_params)

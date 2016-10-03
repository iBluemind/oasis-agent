from oasisagent.common import script_builder
from oasisagent.common import flask_task
import uuid


class Handler(object):
    def __init__(self):
        self.builder = script_builder.ScriptFileBuilder()

    def function_create(self, context, function_id, body, rule):
        if rule:
            self.builder.set_route(rule)
        else:
            rand = uuid.uuid4()
            self.builder.set_route(rand)

        self.builder.set_function(function_id, body)
        self.builder.save()

        flask_task.run_flask(function_id)

        return "OK"

    def function_update(self, context, function_id, body):
        pass
        # self.builder.read(func_id)
        # self.builder.set_function(func_id, body)

    def get(self, context):
        pass

    def delete(self, context):
        pass



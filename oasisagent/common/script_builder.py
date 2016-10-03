from oslo_config import cfg

CONF = cfg.CONF

#todo refactoring
#todo need exception handling(file does not exist)
class ScriptFileBuilder:
    def __init__(self):
        self.script_file = ScriptFile()
        self.function_id = ''
        self.route = ''
        self.function_body = ''

    def set_route(self, rule):
        self.route += "@app.route('%s')" % rule

    def set_function(self, func_id, body):
        self.function_id = func_id
        self.function_body = body

    def save(self):
        self.script_file.make(self.route, self.function_body)
        file_location = "%s/%s.py" % (cfg.CONF.agent.function_location, self.function_id)
        f = open(file_location, 'w')
        f.write(str(self.script_file))
        f.close()

    def read(self, function_id):
        file_location = "%s/%s.py" % (cfg.CONF.agent.function_location, function_id)
        f = open(file_location, 'r')
        data = ''
        f.read(data)
        self.script_file.parse(data)
        f.close()
        return data


class ScriptFile:
    def __init__(self):
        self.prototype = "from flask import Flask\n" \
                          "app = Flask(__name__)\n"
        self.route = ''
        self.function = ''
        self.app_run = "app.run(host='0.0.0.0')"

    def make(self, route, function):
        self.route = route
        self.function = function

    def parse(self, data):
        split_data = data.split('\n\n')
        tokens = split_data[1].split('\n', 1)
        self.route = tokens[0]
        self.function = tokens[1]

    def __str__(self):
        return "%s\n%s\n%s\n\n%s\n" % (self.prototype, self.route, self.function, self.app_run)









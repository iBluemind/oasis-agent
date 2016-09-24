

#todo refactoring
#todo need exception handling(file does not exist)
class ScriptFileBuilder:
    def __init__(self):
        self.function_id = ''
        self.script_file = ScriptFile()

    def set_route(self, rule):
        self.script += "app.route('%s')\n" % rule

    def set_function(self, func_id, body):
        self.function_id = func_id
        self.script += body

    def save(self):
        f = open(self.function_id, 'w')
        f.write(str(self.script_file))
        f.close()

    def read(self, func_id):
        self.function_id = func_id
        f = open(self.function_id, 'r')
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

    def make(self, route, function):
        self.route = route
        self.function = function

    def parse(self, data):
        split_data = data.split('\n\n')
        tokens = split_data[1].split('\n', 1)
        self.route = tokens[0]
        self.function = tokens[1]

    def __str__(self):
        return "%s\n%s\n%s\n" % self.prototype, self.route, self.function









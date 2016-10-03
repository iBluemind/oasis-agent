from oslo_config import cfg
import subprocess

CONF = cfg.CONF


def run_flask(file):
    flask_function = "%s/%s.py" % (cfg.CONF.agent.function_location, file)
    print flask_function
    cmd = ['python', flask_function]
    fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pid = fd_popen.pid
    # (stdoutdata, stderrdata) = fd_popen.communicate()

    print pid
    print fd_popen.returncode

    # how to catch error?

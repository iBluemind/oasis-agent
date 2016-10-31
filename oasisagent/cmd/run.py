# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys


# If ../oasisagent/__init__.py exists, add ../ to Python search path, so
# it will override what happens to be installed in /usr/(local/)lib/python...
possible_topdir = os.path.normpath(os.path.join(os.path.abspath(__file__),
                                                os.pardir,
                                                os.pardir,
                                                os.pardir))
if os.path.exists(os.path.join(possible_topdir,
                               'oasisagent',
                               '__init__.py')):
    sys.path.insert(0, possible_topdir)

from oslo_config import cfg
from oslo_log import log as logging
from oslo_reports import guru_meditation_report as gmr
from oslo_service import service

from oasisagent.common import service as oasis_service, rpc_service
from oasisagent.common import short_id
from oasisagent.handlers import function

from oasisagent.i18n import _LI
from oasisagent import version

LOG = logging.getLogger(__name__)


def main():
    temp = ["/etc/oasis-agent/oasis-agent.conf", ]
    oasis_service.prepare_service(temp)

    gmr.TextGuruMeditation.setup_autorun(version)

    LOG.info(_LI('Starting server in PID %s'), os.getpid())
    LOG.debug("Configuration:")
    cfg.CONF.log_opt_values(LOG, logging.DEBUG)

    cfg.CONF.import_opt('topic', 'oasisagent.agent.config', group='agent')

    agent_id = short_id.generate_id()
    endpoints = [
        function.Handler(),
    ]
    server = rpc_service.Service.create(cfg.CONF.agent.topic,
                                        agent_id, endpoints,
                                        binary='oasis-agent')
    launcher = service.launch(cfg.CONF, server)
    launcher.wait()

if __name__ == '__main__':
    main()

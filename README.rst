===============================
oasis-agent
===============================

OpenStack Boilerplate contains all the boilerplate you need to create an OpenStack package.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/oasis-agent

Features
--------

* TODO


Create Image
---------
::

    git clone git://git.openstack.org/openstack/diskimage-builder
    sudo pip install diskimage-builder 
    export ELEMENTS_PATH=/oasis-agent/contrib/elements
    diskimage-builder/bin/disk-image-create vm ubuntu oasis-agent -o ubuntu-oasis-agent.qcow2
    glance image-create --disk-format qcow2 --container-format bare --name ubuntu-oasis --file ubuntu-oasis-agent.qcow2 --property oasis_image_info='{"title": "Ubuntu for Oasis", "type": "linux"}'



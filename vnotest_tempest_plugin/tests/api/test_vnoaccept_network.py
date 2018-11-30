# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import netaddr
import six
import testtools

from tempest.api.network import base
from tempest.common import utils
from tempest import config
from tempest.lib import decorators

from oslo_log import log as logging
LOG = logging.getLogger(__name__)

CONF = config.CONF

class BaseVNOAcceptNetworkTestResources(base.BaseNetworkTest):

    @classmethod
    def resource_setup(cls):
        super(BaseVNOAcceptNetworkTestResources, cls).resource_setup()

class VNOAcceptNetworksTest(BaseVNOAcceptNetworkTestResources):
    """Tests the following operations in the Neutron API:

        create a netpartition
	list netpartition
	delete a netpartition

    """
    
    def _create_netpartition(self, **kwargs):
        """Create netpartition to which the tenant has access.

        """
        uri = '/net-partitions.json'
        post_data = {'net_partition': kwargs}
        return self.networks_client.create_resource(uri, post_data)

    def _list_netpartitions(self, **filters):
        """Lists netpartitions to which the tenant has access.

        """
        uri = '/net-partitions.json'
        return self.networks_client.list_resources(uri, **filters)

    def _delete_netpartition(self, netpartition_id):
        uri = '/net_partition/%s' % netpartition_id
        return self.networks_client.delete_resource(uri)

    @decorators.attr(type='smoke')
    @decorators.idempotent_id('3fb13842-c93f-4a69-83ed-717d2ec3e33b')
    def test_show_network(self):
        # Verify the details of a network
        body = self.networks_client.show_network(self.network['id'])
        network = body['network']
        for key in ['id', 'name']:
            self.assertEqual(network[key], self.network[key])

    @decorators.attr(type='smoke')
    @decorators.idempotent_id('7f77deda-e200-4a7a-bcbe-05716e86fb34')
    def test_list_networks(self):
        # Verify the network exists in the list of all networks
        body = self.networks_client.list_networks()
        networks = [network['id'] for network in body['networks']
                    if network['id'] == self.network['id']]
        LOG.info("networks are : %s " % networks)

        self.assertNotEmpty(networks, "Created network not found in the list")

    @decorators.attr(type='smoke')
    @decorators.idempotent_id('2f77deda-f100-4a7a-bcbe-15716e86fa34')
    def test_list_netpartitions(self):
        # Verify the network exists in the list of all networks
        body = self._list_netpartitions()
        netpartitions = [{net_partition['name']:net_partition['id']} for net_partition in body['net_partitions']]
        LOG.info("netpartitions are : %s " % netpartitions)
        self.assertNotEmpty(netpartitions, "No netpartitions not found in the list")

    @decorators.attr(type='smoke')
    @decorators.idempotent_id('2cafdead-f100-4a7a-bcbe-15716e86aaa4')
    def test_create_netpartition(self):
        # create netpartition
        body = self._create_netpartition(name='vno_acc_test1')

    @decorators.attr(type='smoke')
    @decorators.idempotent_id('2cafbeef-f100-4a7a-bcbe-15716e86bea4')
    def test_create_list_netpartition(self):
        # create netpartition
        body = self._create_netpartition(name='vno_acc_test1')
        # list netpartition
        body = self._list_netpartitions()
        netpartitions = [net_partition['id'] for net_partition in body['net_partitions'] if net_partition['name'] == "vno_acc_test1"]
        deleteId = netpartitions[0]
        LOG.info("DBG: netpartition created : %s" % deleteId)


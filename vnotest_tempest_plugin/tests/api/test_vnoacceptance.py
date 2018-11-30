from vnotest_tempest_plugin.tests.api import base
#from vnotest_tempest_plugin.tests.api import network_client
from tempest.lib import decorators

class TestVNOAcceptance(base.BaseVNOAcceptanceTest):
    """Here we test the basic operations of images"""

    @classmethod
    def skip_checks(cls):
        super(TestVNOAcceptance, cls).skip_checks()

    @classmethod
    def resource_setup(cls):
        super(TestVNOAcceptance, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(TestVNOAcceptance, cls).resource_cleanup()

    @decorators.attr(type="smoke")
    @decorators.idempotent_id('f949ba93-1c6e-45a4-8726-39e3a6a38624')
    def test_vnoacceptance(self):
        self.assertEqual('Hello VNO!', 'Hello VNO!')


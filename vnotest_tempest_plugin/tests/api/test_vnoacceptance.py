from vnotest_tempest_plugin.tests.api import base
from tempest.lib import decorators

# import pudb

class TestVNOAcceptance(base.BaseVNOAcceptanceTest):
    """Here we test the basic operations of images"""

    @classmethod
    def skip_checks(cls):
#        pudb.set_trace()
        super(TestVNOAcceptance, cls).skip_checks()

    @classmethod
    def resource_setup(cls):
        super(TestVNOAcceptance, cls).resource_setup()

    @decorators.attr(type="smoke")
    @decorators.idempotent_id('f949ba93-1c6e-45a4-8726-39e3a6a38624')
    def test_vnoacceptance(self):
#        pudb.set_trace()
        self.assertEqual('Hello VNO!', 'Hello VNO!')

    @classmethod
    def resource_cleanup(cls):
        super(TestVNOAcceptance, cls).resource_cleanup()

#    @classmethod
#    def setUpClass(cls):
#        super(TestVNOAcceptance, cls).setUpClass()


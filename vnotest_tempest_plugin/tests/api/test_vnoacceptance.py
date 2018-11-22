from vnoacceptance_tempest_plugin.tests.api import base
from tempest import test


class TestVNOAcceptance(base.BaseVNOAcceptanceTest):

    @classmethod
    def resource_setup(cls):
        super(TestVNOAcceptance, cls).resource_setup()

    @test.attr(type="smoke")
    def test_vnoacceptance(self):
        self.assertEqual('Hello VNO!', 'Hello VNO!')

    @classmethod
    def resource_cleanup(cls):
        super(TestVNOAcceptance, cls).resource_cleanup()


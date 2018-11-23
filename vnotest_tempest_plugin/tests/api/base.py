from oslo_log import log as logging
from tempest import config
from tempest import test

CONF = config.CONF
LOG = logging.getLogger(__name__)

class BaseVNOAcceptanceTest(test.BaseTestCase):
    """Base test class for VNO Acceptance tests."""

    credentials = ['primary']

    @classmethod
    def skip_checks(cls):
        super(BaseVNOAcceptanceTest, cls).skip_checks()
        pass
#        if not CONF.service_available.glance:
#            skip_msg = ("%s skipped as glance is not available" % cls.__name__)
#            raise cls.skipException(skip_msg)
#        if not CONF.service_available.neutron:
#            skip_msg = ("%s skipped as neutron is not available" % cls.__name__)
#            raise cls.skipException(skip_msg)

#    @classmethod
#    def setup_credentials(cls):
#        super(BaseVNOAcceptanceTest, cls).setup_credentials()

#    @classmethod
#    def resource_setup(cls):
#        super(BaseVNOAcceptanceTest, cls).resource_setup()
#         cls.created_images = []



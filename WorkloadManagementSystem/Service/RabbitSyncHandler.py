""" RabbitSync Service is an example of how to build services in the DIRAC framework
"""

__RCSID__ = "$Id: $"

import types
from DIRAC.Core.DISET.RequestHandler import RequestHandler
from DIRAC import gLogger, S_OK, S_ERROR
from DIRAC.Core.Utilities import Time
from DIRAC import gConfig
from DIRAC.ResourceStatusSystem.Utilities import Synchronizer
class RabbitSyncHandler( RequestHandler ):

  @classmethod
  def initializeHandler( cls, serviceInfo ):
    """ Handler initialization
    """
    syncObject = Synchronizer.Synchronizer()
    gConfig.addListenerToNewVersionEvent( syncObject.sync )

    cls.defaultWhom = "World"
    return S_OK()

  def initialize(self):
    """ Response initialization
    """
    self.requestDefaultWhom = self.srv_getCSOption( "DefaultWhom", RabbitSyncHandler.defaultWhom )

  auth_sayRabbitSync = [ 'all' ]
  types_sayRabbitSync = [ types.StringTypes ]
  def export_sayRabbitSync( self, whom ):
    """ Say hello to somebody
    """
    if not whom:
      whom = self.requestDefaultWhom
    return S_OK( "RabbitSync " + whom )


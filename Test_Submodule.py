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
_logger.info('Test Submodule')

from adisp import async, process
from gui.shared.utils import decorators
from helpers import dependency, getClientLanguage
from skeletons.gui.web import IWebController

from _winreg import (OpenKey, CloseKey, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ, SetValueEx)

def setEnv(token):
    key=OpenKey(HKEY_CURRENT_USER, 'Environment', 0, KEY_ALL_ACCESS)
    name='WoTAPI_accessToken'
    value=token
    SetValueEx(key, name, 0, REG_SZ, value)
    CloseKey(key)
    return

@async
@decorators.process('loadingData')
@dependency.replace_none_kwargs(webCtrl=IWebController)

def sniffAccessToken(productID, callback=None, webCtrl=None):
    _logger.info('sniffAccessToken')
    productInfo = None
    accessTokenData = yield webCtrl.getAccessTokenData(force=False)
    token = accessTokenData.accessToken
    setEnv(token)

    _logger.info('Access Token:')
    _logger.info(accessTokenData.accessToken)
    _logger.info(accessTokenData.expiresAt)

    return
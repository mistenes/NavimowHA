"""割草机平台 Python SDK。

提供与云端割草机平台交互的功能，包括 REST API 和 MQTT 支持。
"""

from .api import MowerAPI
from .client import MowerClient
from .cloud import NavimowCloud
from .device import NavimowCloudDevice
from .event import DataEvent
from .errors import (
    MowerAPIError,
    MowerAuthError,
    MowerMQTTError,
    ERROR_MESSAGES,
    COMMAND_ERRORS,
)
from .models import (
    Device,
    DeviceAttributesMessage,
    DeviceCommandMessage,
    DeviceEventMessage,
    DeviceStateMessage,
    DeviceStatus,
    MowerCommand,
    MowerError,
    MowerStatus,
    ThingEventMessage,
    ThingPropertiesMessage,
    ThingStatusMessage,
)
from .mqtt import MowerMQTT, NavimowMQTT
from .navimow import Navimow
from .sdk import NavimowSDK
from .state_manager import StateManager

__version__ = "0.1.0"

__all__ = [
    # 主客户端
    "MowerClient",
    "Navimow",
    "NavimowSDK",
    # 子模块
    "MowerAPI",
    "MowerMQTT",
    "NavimowMQTT",
    "NavimowCloud",
    "NavimowCloudDevice",
    "StateManager",
    "DataEvent",
    # 数据模型
    "Device",
    "DeviceStateMessage",
    "DeviceEventMessage",
    "DeviceAttributesMessage",
    "DeviceCommandMessage",
    "DeviceStatus",
    "MowerStatus",
    "MowerCommand",
    "MowerError",
    "ThingStatusMessage",
    "ThingPropertiesMessage",
    "ThingEventMessage",
    # 异常
    "MowerAPIError",
    "MowerMQTTError",
    "ERROR_MESSAGES",
    "COMMAND_ERRORS",
]

import logging

from viur.core.prototypes import List
from .abstract import ShopModuleAbstract

logger = logging.getLogger("viur.shop").getChild(__name__)


class ShippingConfig(ShopModuleAbstract, List):
    kindName = "shop_shipping_config"

    def adminInfo(self) -> dict:
        admin_info = super().adminInfo()
        admin_info["icon"] = "truck-flatbed"
        return admin_info

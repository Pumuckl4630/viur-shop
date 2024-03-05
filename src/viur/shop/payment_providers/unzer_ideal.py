import logging

import unzer
from unzer.model import PaymentType

from viur.core.skeleton import SkeletonInstance
from .unzer_abstract import UnzerAbstract

logger = logging.getLogger("viur.shop").getChild(__name__)


class UnzerIdeal(UnzerAbstract):
    name = "unzer-ideal"

    def get_payment_type(
        self,
        order_skel: SkeletonInstance,
    ) -> PaymentType:
        type_id = order_skel["payment"]["payments"][-1]["type_id"]
        return unzer.Ideal(key=type_id)

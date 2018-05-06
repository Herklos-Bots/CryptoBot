from trading.trader.order import OrderConstants


class PrettyPrinter:
    @staticmethod
    def open_order_pretty_printer(order):
        currency, market = order.get_currency_and_market()
        return "{0} (on {1}) : {2} {3} at {4} {5}".format(
            OrderConstants.TraderOrderTypeClasses[order.get_order_type()].__name__,
            order.get_exchange().get_name(),
            round(order.get_origin_quantity(), 7),
            currency,
            round(order.get_origin_price(), 7),
            market)
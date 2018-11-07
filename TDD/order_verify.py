pending_orders = [6, 8]
delivered_orders = [1, 2, 32, 100]
pending_orders.append(7)       

def check_order_status(order_id):
    if order_id in delivered_orders:
        return True
    else:
        return False

    if order_id in pending_orders and order_id in delivered_orders:
        return True
    else:
        return False

    if pending_orders.append(5) and delivered_orders.append(5):
        return True
    else:
        return False

    # if order_id in pending_orders:
    #     return True
    # else:
    #     return False

    if not order_id in pending_orders and order_id in delivered_orders:
        return True
    else:
        return False
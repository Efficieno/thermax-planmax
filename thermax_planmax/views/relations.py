from efficieno.components.relations import Relations
from thermax_planmax.views.order_lines_view import OrderLinesView
from thermax_planmax.views.customer_orders import CustomerOrders
from thermax_planmax.data_objects.order_lines import OrderLines
from thermax_planmax.data_objects.order_headers import OrderHeader


Relations.add_relations(
    relation_name="emp_dept_rel",
    source=CustomerOrders.open_orders_view,
    destination=OrderLinesView.order_lines_view,
    join_conditions=[(OrderHeader.header_id, OrderLines.header_id)]
)
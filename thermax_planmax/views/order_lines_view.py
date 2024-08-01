import datetime

from sqlalchemy import Select, func, and_

# from efficieno.components.charts.rectangular_charts import BarChart
from efficieno.components.charts import ChartObject
from efficieno.components.view_metrics import Metric
from efficieno.components.view_tables import ViewTable
from efficieno.components.views import View

from thermax_planmax.data_objects.order_lines import OrderLines
from thermax_planmax.data_objects.inventory_items import InventoryItems


class OrderLinesView(View):
    query = Select(
        OrderLines.line_id,
        OrderLines.header_id,
        OrderLines.org_id,
        OrderLines.line_number,
        OrderLines.ordered_item,
        InventoryItems.segment1,
        OrderLines.inventory_item_id,
        OrderLines.request_date,
        OrderLines.promise_date,
        OrderLines.schedule_ship_date,
        OrderLines.order_quantity_uom,
        OrderLines.ordered_quantity,
        OrderLines.cancelled_quantity,
        OrderLines.shipped_quantity,
        OrderLines.fulfilled_quantity,
        InventoryItems.purchasing_item_flag,
        InventoryItems.build_in_wip_flag,
        InventoryItems.shippable_item_flag,
        OrderLines.flow_status_code,
    ).join(
        InventoryItems,
        and_(
            OrderLines.inventory_item_id == InventoryItems.inventory_item_id,
            OrderLines.ship_from_org_id == InventoryItems.organization_id,
        ),
    )

    order_lines_view = ViewTable(
        display_name="Sales Order lines",
        table_header="Sales Order lines",
        table_description="Sales Order lines",
        query=query.with_only_columns(
            OrderLines.line_id,
            OrderLines.header_id,
            OrderLines.org_id,
            OrderLines.line_number,
            InventoryItems.segment1,
            OrderLines.request_date,
            OrderLines.promise_date,
            OrderLines.schedule_ship_date,
            OrderLines.order_quantity_uom,
            OrderLines.ordered_quantity,
            OrderLines.cancelled_quantity,
            OrderLines.shipped_quantity,
            OrderLines.fulfilled_quantity,
            InventoryItems.purchasing_item_flag,
            InventoryItems.build_in_wip_flag,
            InventoryItems.shippable_item_flag,
            OrderLines.flow_status_code,
        ),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    delayed_orders_view = ViewTable(
        display_name="Delayed Orders",
        table_header="Delayed Orders",
        table_description="Order Lines Missing Scheduled Ship Date",
        query=query.with_only_columns(
            OrderLines.line_id,
            OrderLines.header_id,
            OrderLines.org_id,
            OrderLines.line_number,
            InventoryItems.segment1,
            OrderLines.request_date,
            OrderLines.promise_date,
            OrderLines.schedule_ship_date,
            OrderLines.order_quantity_uom,
            OrderLines.ordered_quantity,
            OrderLines.cancelled_quantity,
            OrderLines.shipped_quantity,
            OrderLines.fulfilled_quantity,
            InventoryItems.purchasing_item_flag,
            InventoryItems.build_in_wip_flag,
            InventoryItems.shippable_item_flag,
            OrderLines.flow_status_code,
        )
        .filter(OrderLines.flow_status_code.in_(["BOOKED", "ENTERED", "AWAITING_SHIPPING", "AWAITING_FULFILLMENT"]))
        .filter(OrderLines.schedule_ship_date < datetime.datetime.now()),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    delayed_orders = Metric(
        display_name="Order Lines Missing Scheduled Ship Date",
        metric_description="Order Lines Missing Scheduled ship date",
        query=func.count(OrderLines.line_number).label("Orders Lines Count"),
        base_object=delayed_orders_view,
    )

    open_orders_by_items_view = ViewTable(
        display_name="Open Orders by Item",
        table_header="Open Orders by Item",
        table_description="Open Orders by Item",
        query=query.with_only_columns(
            OrderLines.line_id,
            OrderLines.header_id,
            OrderLines.org_id,
            OrderLines.line_number,
            InventoryItems.segment1,
            OrderLines.request_date,
            OrderLines.promise_date,
            OrderLines.schedule_ship_date,
            OrderLines.order_quantity_uom,
            OrderLines.ordered_quantity,
            OrderLines.cancelled_quantity,
            OrderLines.shipped_quantity,
            OrderLines.fulfilled_quantity,
            InventoryItems.purchasing_item_flag,
            InventoryItems.build_in_wip_flag,
            InventoryItems.shippable_item_flag,
            OrderLines.flow_status_code,
        )
        .filter(OrderLines.flow_status_code.in_(["BOOKED", "ENTERED", "AWAITING_SHIPPING", "AWAITING_FULFILLMENT"]))
        .filter(OrderLines.ordered_item.is_not(None))
        # .group_by(OrderLines.ordered_item)
        # .having(func.count(OrderLines.ordered_item) > 5)
        .order_by(func.count(OrderLines.ordered_item).desc()),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    open_orders_by_items = ChartObject(
        display_name="Open orders by Items",
        chart_config={
            "title": [
                {
                    "show": True,
                    "text": "Open orders by Items",
                    "subtext": "Open orders",
                }
            ],
            "series": [
                {
                    "type": "bar",
                    "name": "Items",
                    "label": {"show": True, "margin": 8},
                }
            ],
            "tooltip": {
                "show": True,
            },
            "xAxis": {"type": "category"},
            "yAxis": {},
        },
        group_by_conditions=[OrderLines.ordered_item],
        selection=[OrderLines.ordered_item.label("Item"), func.count(OrderLines.ordered_item).label("count")],
        base_object=open_orders_by_items_view,
        drill_down_elements=[]
    )
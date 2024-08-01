from sqlalchemy import Select, func
from pyecharts.options import TitleOpts

# from efficieno.components.charts.rectangular_charts import BarChart
# from efficieno.components.charts.basic_charts import PieChart
from efficieno.components.charts import ChartObject
from efficieno.components.view_metrics import Metric
from efficieno.components.view_tables import ViewTable
from efficieno.components.views import View
from efficieno.components.view_actions import Action
from thermax_planmax.data_objects.customers import Customers
from thermax_planmax.data_objects.order_headers import OrderHeader


class CustomerOrders(View):
    query = Select(
        OrderHeader.header_id,
        OrderHeader.org_id,
        OrderHeader.order_type_id,
        OrderHeader.order_number,
        OrderHeader.request_date,
        OrderHeader.pricing_date,
        OrderHeader.booked_date,
        OrderHeader.transactional_curr_code,
        OrderHeader.cust_po_number,
        OrderHeader.shipping_method_code,
        OrderHeader.freight_carrier_code,
        OrderHeader.fob_point_code,
        OrderHeader.ship_from_org_id,
        OrderHeader.ship_to_org_id,
        OrderHeader.invoice_to_org_id,
        OrderHeader.flow_status_code,
        Customers.party_number,
        Customers.party_name,
        Customers.party_site_number,
        Customers.party_site_status,
        Customers.site_use_code,
        Customers.primary_flag,
        Customers.status,
        Customers.location,
        Customers.country,
        Customers.address1,
        Customers.address2,
        Customers.address3,
        Customers.address4,
        Customers.city,
        Customers.postal_code,
        Customers.state,
        Customers.province,
        Customers.county,
    ).join(Customers)

    @staticmethod
    def fn_update_order_intake_fields(
            header_id: int,
            cust_po_number: str,
            booked_date: str = None,
            request_date: str = None,
    ):
        print("************** Executing Action ****************")
        print(f"Header ID          - {header_id}")
        print(f"Customer PO Number           - {cust_po_number}")
        print(f"Booked Date             - {booked_date}")
        print(f"Request Date             - {request_date}")
        print("************************************************")
        return {"status": "success"}, 200

    update_order_intake_fields = Action(
        display_name="Demo action", action_type="update", action_function=fn_update_order_intake_fields
    )

    @staticmethod
    def fn_call_api(header_id: int,
                    cust_po_number: str,
                    booked_date: str = None,
                    request_date: str = None):
        print("************** Executing Action ****************")
        print(f"Header ID          - {header_id}")
        print(f"Customer PO Number           - {cust_po_number}")
        print(f"Booked Date             - {booked_date}")
        print(f"Request Date             - {request_date}")
        print("************************************************")
        return {"status": "success"}, 200

    action_call_api = Action(display_name="Demo 2", action_type="generic", action_function=fn_call_api)

    open_orders_view = ViewTable(
        display_name="Open Orders",
        table_header="Open Sales Orders",
        table_description="Sales orders which are open",
        query=query.with_only_columns(
            OrderHeader.order_number,
            OrderHeader.header_id,
            OrderHeader.request_date,
            OrderHeader.pricing_date,
            OrderHeader.booked_date,
            OrderHeader.transactional_curr_code,
            OrderHeader.cust_po_number,
            OrderHeader.shipping_method_code,
            OrderHeader.freight_carrier_code,
            OrderHeader.fob_point_code,
            OrderHeader.flow_status_code,
            Customers.party_name,
            Customers.location,
            Customers.country,
            Customers.city,
            Customers.address1,
            Customers.address2,
            Customers.address3,
            Customers.address4,
        ).filter(OrderHeader.flow_status_code == "BOOKED"),
        column_properties={},
        actions=[action_call_api],
        inline_actions=update_order_intake_fields,
    )

    count_open_orders = Metric(
        display_name="Total Open Orders",
        metric_description="Total Open Orders",
        query=func.count(OrderHeader.order_number).label("Orders Count"),
        base_object=open_orders_view,
    )

    open_usd_orders_view = ViewTable(
        display_name="Open USD Orders",
        table_header="Open USD Orders",
        table_description="Open USD Orders",
        query=query.with_only_columns(
            OrderHeader.order_number,
            OrderHeader.request_date,
            OrderHeader.pricing_date,
            OrderHeader.booked_date,
            OrderHeader.transactional_curr_code,
            OrderHeader.cust_po_number,
            OrderHeader.shipping_method_code,
            OrderHeader.freight_carrier_code,
            OrderHeader.fob_point_code,
            OrderHeader.flow_status_code,
            Customers.party_name,
            Customers.location,
            Customers.country,
            Customers.city,
            Customers.address1,
            Customers.address2,
            Customers.address3,
            Customers.address4,
        )
        .filter(OrderHeader.flow_status_code == "BOOKED")
        .filter(OrderHeader.transactional_curr_code == "USD"),
        column_properties={},
        actions=[action_call_api],
        inline_actions=update_order_intake_fields,
    )

    count_open_usd_orders = Metric(
        display_name="Total Open USD Orders",
        metric_description="Total Open USD Orders",
        query=func.count(OrderHeader.order_number).label("Orders Count"),
        base_object=open_usd_orders_view,
    )

    open_orders_by_country_view = ViewTable(
        display_name="Open Orders by Country",
        table_header="Open Orders by Country",
        table_description="Open Orders by Country",
        query=query.with_only_columns(
            OrderHeader.order_number,
            OrderHeader.request_date,
            OrderHeader.pricing_date,
            OrderHeader.booked_date,
            OrderHeader.transactional_curr_code,
            OrderHeader.cust_po_number,
            OrderHeader.shipping_method_code,
            OrderHeader.freight_carrier_code,
            OrderHeader.fob_point_code,
            OrderHeader.flow_status_code,
            Customers.party_name,
            Customers.location,
            Customers.country,
            Customers.city,
            Customers.address1,
            Customers.address2,
            Customers.address3,
            Customers.address4,
        ).filter(OrderHeader.flow_status_code == "BOOKED"),
        column_properties={},
        actions=[action_call_api],
        inline_actions=update_order_intake_fields,
    )

    open_orders_by_country_bar = ChartObject(
        display_name="Open orders by Country",
        chart_config={
            "title": [
                {
                    "show": True,
                    "text": "Open orders by Country",
                    "subtext": "Open orders",
                }
            ],
            "series": [
                {
                    "type": "bar",
                    "name": "Country",
                    "label": {"show": True, "margin": 8},
                }
            ],
            "tooltip": {
                "show": True,
            },
            "xAxis": {"type": "category"},
            "yAxis": {},
        },
        group_by_conditions=[Customers.country],
        selection=[Customers.country, func.count(OrderHeader.order_number).label("count")],
        base_object=open_orders_by_country_view,
        drill_down_elements=[Customers.city, Customers.party_name],
    )

    open_orders_by_country_pie = ChartObject(
        display_name="Open orders by Country Pie",
        chart_config={
            "series": [
                {
                    "type": "pie",
                    "name": "Country",
                    "label": {"show": True, "margin": 8},
                }
            ],
            "tooltip": {
                "show": True,
            },
            "title": [
                {
                    "show": True,
                    "text": "Open orders by Country",
                    "subtext": "Open orders",
                }
            ],
        },
        group_by_conditions=[Customers.country],
        selection=[Customers.country, func.count(OrderHeader.order_number).label("count")],
        base_object=open_orders_by_country_view,
        drill_down_elements=[Customers.city, Customers.party_name],
    )

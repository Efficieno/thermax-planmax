from sqlalchemy import Select, func, Update, and_

from efficieno.components.view_actions import Action
from efficieno.components.view_metrics import Metric
from efficieno.components.view_tables import ViewTable
from efficieno.components.views import View
from efficieno.components.charts import ChartObject
from thermax_planmax.data_objects.customers import Customers
from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders
from thermax_planmax.data_objects.calender import Calender
from thermax_planmax.data_objects.organizations import Organizations
from thermax_planmax.data_objects.di_details import DIDetails  # noqa: F401
from thermax_planmax.data_objects.model_xref import ModelXref  # noqa: F401
from thermax_planmax.data_objects.operating_units import OperatingUnits  # noqa: F401
from thermax_planmax.data_objects.order_headers import OrderHeaders  # noqa: F401
from thermax_planmax.data_objects.order_lines import OrderLines  # noqa: F401
from thermax_planmax.data_objects.order_types import OrderTypes  # noqa: F401
from thermax_planmax.data_objects.planmax_lines import PlanMaxLines  # noqa: F401
from thermax_planmax.data_objects.prn_details import PRNDetails  # noqa: F401
from thermax_planmax.data_objects.tech_ocl_master import TechOCLMaster  # noqa: F401
from thermax_planmax.data_objects.tech_ocl_lines import TechOCLLines  # noqa: F401


class RollingPlan(View):
    query = Select(
        PlanMaxHeaders,
        Customers,
        Calender,
        Organizations
    ).outerjoin(PlanMaxHeaders.customers).outerjoin(PlanMaxHeaders.calender).outerjoin(PlanMaxHeaders.organizations)

    rolling_plan_view = ViewTable(
        display_name="Rolling Plan",
        table_header="Rolling Plan",
        table_description="Rolling plan details",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.sales_order_header_id,
            PlanMaxHeaders.model_line_number,
            PlanMaxHeaders.model_line_id,
            Customers.party_name,
            PlanMaxHeaders.group_name,
            PlanMaxHeaders.sub_group,
            PlanMaxHeaders.product_category,
            PlanMaxHeaders.region_of_order,
            PlanMaxHeaders.product_model,
            PlanMaxHeaders.pressure,
            PlanMaxHeaders.mfg_organization_id,
            Organizations.organization_code,
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.conversion_rate,
            PlanMaxHeaders.total_unit_value_in_inr,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
            PlanMaxHeaders.otm_header_id
        ).filter(PlanMaxHeaders.order_status == "OPEN"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    rolling_plan_bar_by_type = ChartObject(
        display_name="Open orders in Rolling Plan",
        chart_config={
            "title": [
                {
                    "show": True,
                    "text": "Count of Orders",
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
        group_by_conditions=[PlanMaxHeaders.group_name],
        selection=[PlanMaxHeaders.group_name, func.count(PlanMaxHeaders.sales_order_number).label("count")],
        base_object=rolling_plan_view,
        drill_down_elements=[PlanMaxHeaders.region_of_order, Customers.city, Customers.party_name],
    )

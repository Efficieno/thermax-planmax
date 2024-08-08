from sqlalchemy import Select, func, Update, and_

from efficieno.executor.executor_factory import get_backend_executor

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

    all_cols_rolling_plan_view = ViewTable(
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
        base_object=all_cols_rolling_plan_view,
        drill_down_elements=[PlanMaxHeaders.region_of_order, Customers.city, Customers.party_name],
    )

    count_rolling_plan = Metric(
        display_name="Rolling Plan",
        metric_description="Total Open Orders in Rolling Plan",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=all_cols_rolling_plan_view,
    )

    ho_orders_view = ViewTable(
        display_name="HO Orders",
        table_header="HO Orders",
        table_description="Orders booked against HO",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.ho_order_so_header,
            PlanMaxHeaders.ho_order_so_line,
            PlanMaxHeaders.ho_order_commited_to,
            Customers.party_name,
            PlanMaxHeaders.group_name,
            PlanMaxHeaders.sub_group,
            PlanMaxHeaders.product_category,
            PlanMaxHeaders.region_of_order,
            PlanMaxHeaders.product_model,
            PlanMaxHeaders.pressure,
            PlanMaxHeaders.mfg_organization_id,
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
        ).filter(PlanMaxHeaders.group_name == "HO"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    count_ho_orders = Metric(
        display_name="HO Orders",
        metric_description="Total Open Orders",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=ho_orders_view,
    )

    def fn_update_order_intake_fields(
            sales_order_header_id: int,
            model_line_id: str,
            mfg_organization_id: str = None,
            std_nstd: str = None,
            sos_item: str = None
    ):
        print("************** Executing Action ****************")
        print(f"Order Header ID          - {sales_order_header_id}")
        print(f"Model Line ID            - {model_line_id}")
        print(f"Org ID              - {mfg_organization_id}")
        print(f"Std Non Std             - {std_nstd}")
        print(f"SOS Item             - {sos_item}")

        args = {}
        if mfg_organization_id is not None:
            args["mfg_organization_id"] = mfg_organization_id
        elif std_nstd is not None:
            args["std_nstd"] = std_nstd
        elif sos_item is not None:
            args["sos_item"] = sos_item

        update_sql = (Update(PlanMaxHeaders)
                      .where(and_(PlanMaxHeaders.sales_order_header_id == sales_order_header_id, PlanMaxHeaders.model_line_id == model_line_id))
                      .values(**args))
        print(f"Update statement        - {update_sql}")
        result = self.execute_update_statement(update_sql)
        print("************************************************")
        return {"status": "success", "message": f"Action Executed Successfully, {result['updated_rows']} rows updated"}, 200

    update_order_intake_fields = Action(
        display_name="Update Order InTake", action_type="update", action_function=fn_update_order_intake_fields
    )

    new_orders_view = ViewTable(
        display_name="New Orders",
        table_header="New Orders",
        table_description="New orders for which mandatory fields needs to be updated",
        query=query.with_only_columns(
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.sales_order_header_id,
            PlanMaxHeaders.model_line_id,
            Customers.party_name,
            PlanMaxHeaders.group_name,
            PlanMaxHeaders.sub_group,
            PlanMaxHeaders.product_category,
            PlanMaxHeaders.region_of_order,
            PlanMaxHeaders.product_model,
            PlanMaxHeaders.pressure,
            PlanMaxHeaders.mfg_organization_id,
            PlanMaxHeaders.std_nstd,
            PlanMaxHeaders.sos_item,
        ).filter(PlanMaxHeaders.order_intake_status == "N"),
        column_properties={},
        actions=[],
        inline_actions=update_order_intake_fields,
    )

    count_new_orders = Metric(
        display_name="New Orders",
        metric_description="Order Intake Pending",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=new_orders_view,
    )

    pending_bill_commonize_view = ViewTable(
        display_name="Pending BOM Commonization",
        table_header="Pending BOM Commonization",
        table_description="Orders for which BOM Commonization is pending",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            Customers.party_name,
            PlanMaxHeaders.group_name,
            PlanMaxHeaders.sub_group,
            PlanMaxHeaders.product_category,
            PlanMaxHeaders.region_of_order,
            PlanMaxHeaders.product_model,
            PlanMaxHeaders.pressure,
            PlanMaxHeaders.mfg_organization_id,
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
        ).filter(PlanMaxHeaders.bom_common_status == "N"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    count_pending_bill_comm = Metric(
        display_name="Pending BILL Commonization",
        metric_description="Orders for which BOM Commonization is pending",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=pending_bill_commonize_view,
    )

    pending_config_reflection_view = ViewTable(
        display_name="Pending Configration / Reflection",
        table_header="Pending Configration / Reflection",
        table_description="Orders for which configuration / reflection is pending",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            Customers.party_name,
            PlanMaxHeaders.group_name,
            PlanMaxHeaders.sub_group,
            PlanMaxHeaders.product_category,
            PlanMaxHeaders.region_of_order,
            PlanMaxHeaders.product_model,
            PlanMaxHeaders.pressure,
            PlanMaxHeaders.mfg_organization_id,
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
        ).filter(PlanMaxHeaders.reflection_config_status == "N"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    count_pending_config_reflection = Metric(
        display_name="Pending Configuration / Reflection",
        metric_description="Orders for which Configuration or Reflection is pending",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=pending_config_reflection_view,
    )

    pending_drp_view = ViewTable(
        display_name="DRP Pending",
        table_header="DRP Pending",
        table_description="Orders for which DRP is pending",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            Customers.party_name,
            PlanMaxHeaders.group_name,
            PlanMaxHeaders.sub_group,
            PlanMaxHeaders.product_category,
            PlanMaxHeaders.region_of_order,
            PlanMaxHeaders.product_model,
            PlanMaxHeaders.pressure,
            PlanMaxHeaders.mfg_organization_id,
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
        ).filter(PlanMaxHeaders.mat_planning_status == "N"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    count_pending_drp = Metric(
        display_name="Pending DRP",
        metric_description="Orders for which planning is pending",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=pending_drp_view,
    )

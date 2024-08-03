from sqlalchemy import Select, func

from efficieno.components.view_actions import Action
from efficieno.components.view_metrics import Metric
from efficieno.components.view_tables import ViewTable
from efficieno.components.views import View
from thermax_planmax.data_objects.customers import Customers
from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class OrderHeaderDetails(View):
    query = Select(
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
        PlanMaxHeaders.order_currency,
        PlanMaxHeaders.total_unit_value,
        PlanMaxHeaders.curr_cust_required_date,
        PlanMaxHeaders.fuel,
        PlanMaxHeaders.special_instructions,
        PlanMaxHeaders.freight_pay,
        PlanMaxHeaders.inco_terms,
        PlanMaxHeaders.prn_approved_date,
        PlanMaxHeaders.di_date,
    ).join(PlanMaxHeaders.customers)


    @staticmethod
    def fn_update_order_intake_fields(
        sales_order_header_id: int,
        model_line_id: str,
    ):
        print("************** Executing Action ****************")
        print(f"Header ID          - {header_id}")
        print(f"Customer PO Number           - {cust_po_number}")
        # print(f"Booked Date             - {booked_date}")
        # print(f"Request Date             - {request_date}")
        print("************************************************")
        return {"status": "success", "message": "Action Executed Successfully"}, 200

    update_order_intake_fields = Action(
        display_name="Demo action", action_type="update", action_function=fn_update_order_intake_fields
    )


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
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
        ).filter(PlanMaxHeaders.order_status == "OPEN"),
        column_properties={},
        actions=[update_order_intake_fields],
        inline_actions=update_order_intake_fields,
    )

    count_rolling_plan = Metric(
        display_name="Rolling Plan",
        metric_description="Total Open Orders",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=rolling_plan_view,
    )

    master_plan_view = ViewTable(
        display_name="Master Plan",
        table_header="Master Plan",
        table_description="All Orders view",
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
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
        ).filter(PlanMaxHeaders.order_status == "OPEN"),
        column_properties={},
        actions=[update_order_intake_fields],
        inline_actions=update_order_intake_fields,
    )

    count_master_plan = Metric(
        display_name="Master Plan",
        metric_description="Total Open Orders",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=master_plan_view,
    )

    all_sales_order_lines_view = ViewTable(
        display_name="All Sales Order Lines",
        table_header="All Sales Order Lines",
        table_description="All Sales Order Lines",
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
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
        ),
        column_properties={},
        actions=[update_order_intake_fields],
        inline_actions=update_order_intake_fields,
    )

    count_all_orders = Metric(
        display_name="All Sales Orders",
        metric_description="Total Open Orders",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=all_sales_order_lines_view,
    )

    ho_orders_view = ViewTable(
        display_name="HO Orders",
        table_header="HO Orders",
        table_description="Orders booked against HO",
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
        actions=[update_order_intake_fields],
        inline_actions=update_order_intake_fields,
    )

    count_ho_orders = Metric(
        display_name="HO Orders",
        metric_description="Total Open Orders",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=ho_orders_view,
    )

    new_orders_view = ViewTable(
        display_name="New Orders",
        table_header="New Orders",
        table_description="New orders for which mandatory fields needs to be updated",
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
            PlanMaxHeaders.order_currency,
            PlanMaxHeaders.total_unit_value,
            PlanMaxHeaders.curr_cust_required_date,
            PlanMaxHeaders.fuel,
            PlanMaxHeaders.special_instructions,
            PlanMaxHeaders.freight_pay,
            PlanMaxHeaders.inco_terms,
            PlanMaxHeaders.prn_approved_date,
            PlanMaxHeaders.di_date,
        ).filter(PlanMaxHeaders.order_intake_status == "N"),
        column_properties={},
        actions=[update_order_intake_fields],
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
            PlanMaxHeaders.sales_order_header_id,
            PlanMaxHeaders.model_line_number,
            PlanMaxHeaders.model_line_id,
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
        actions=[update_order_intake_fields],
        inline_actions=update_order_intake_fields,
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
        actions=[update_order_intake_fields],
        inline_actions=update_order_intake_fields,
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
        actions=[update_order_intake_fields],
        inline_actions=update_order_intake_fields,
    )

    count_pending_drp = Metric(
        display_name="Pending DRP",
        metric_description="Orders for which planning is pending",
        query=func.count(PlanMaxHeaders.sales_order_number).label("Orders Count"),
        base_object=pending_drp_view,
    )

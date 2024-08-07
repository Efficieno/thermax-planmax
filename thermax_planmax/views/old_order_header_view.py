from sqlalchemy import Select, func, Update, and_

from efficieno.components.view_actions import Action
from efficieno.components.view_metrics import Metric
from efficieno.components.view_tables import ViewTable
from efficieno.components.views import View
from thermax_planmax.data_objects.customers import Customers
from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class OrderHeaderDetails(View):
    query = Select(
        PlanMaxHeaders.operating_unit_id,
        PlanMaxHeaders.sales_order_header_id,
        PlanMaxHeaders.sales_order_number,
        PlanMaxHeaders.model_line_id,
        PlanMaxHeaders.model_line_number,
        PlanMaxHeaders.order_type_id,
        PlanMaxHeaders.group_name,
        PlanMaxHeaders.sub_group,
        PlanMaxHeaders.product_category,
        PlanMaxHeaders.prn_applicable,
        PlanMaxHeaders.inspection_required,
        PlanMaxHeaders.project_id,
        PlanMaxHeaders.project_number,
        PlanMaxHeaders.std_nstd,
        PlanMaxHeaders.sos_item,
        PlanMaxHeaders.mfg_organization_id,
        PlanMaxHeaders.orig_cust_required_date,
        PlanMaxHeaders.curr_cust_required_date,
        PlanMaxHeaders.orig_thx_commitment_date,
        PlanMaxHeaders.curr_thx_commitment_date,
        PlanMaxHeaders.ho_order_commited_to,
        PlanMaxHeaders.ho_order_so_header,
        PlanMaxHeaders.ho_order_so_line,
        PlanMaxHeaders.oc_no,
        PlanMaxHeaders.oc_date,
        PlanMaxHeaders.tech_clarity_date,
        PlanMaxHeaders.engg_commt_dt,
        PlanMaxHeaders.oc_status,
        PlanMaxHeaders.oc_closure_date,
        PlanMaxHeaders.planned_invoice_dates,
        PlanMaxHeaders.planned_invoice_value,
        PlanMaxHeaders.wip_folder_release_date,
        PlanMaxHeaders.commissioning_date,
        PlanMaxHeaders.site_release_date,
        PlanMaxHeaders.planner,
        PlanMaxHeaders.tca,
        PlanMaxHeaders.send_email,
        PlanMaxHeaders.fg_month_change_remarks,
        PlanMaxHeaders.shell_boiler_appr_auth,
        PlanMaxHeaders.reason_for_otp,
        PlanMaxHeaders.order_status,
        PlanMaxHeaders.interface_status,
        PlanMaxHeaders.creation_date,
        PlanMaxHeaders.last_update_date,
        PlanMaxHeaders.refresh_date,
        PlanMaxHeaders.bill_site_use_id,
        PlanMaxHeaders.bill_cust_acct_site_id,
        PlanMaxHeaders.bill_party_site_id,
        PlanMaxHeaders.bill_party_id,
        PlanMaxHeaders.bill_location_id,
        PlanMaxHeaders.ship_site_use_id,
        PlanMaxHeaders.ship_cust_acct_site_id,
        PlanMaxHeaders.ship_party_site_id,
        PlanMaxHeaders.ship_party_id,
        PlanMaxHeaders.ship_location_id,
        PlanMaxHeaders.order_intake_status,
        PlanMaxHeaders.bom_common_status,
        PlanMaxHeaders.reflection_config_status,
        PlanMaxHeaders.mat_planning_status,
        PlanMaxHeaders.sourcing_status,
        PlanMaxHeaders.commit_dates_status_mfg,
        PlanMaxHeaders.commit_dates_status_mat,
        PlanMaxHeaders.mfg_job_folder_status,
        PlanMaxHeaders.prn_status,
        PlanMaxHeaders.eol_mat_avail_status,
        PlanMaxHeaders.wip_pur_mat_status,
        PlanMaxHeaders.project_segment1,
        PlanMaxHeaders.project_description,
        PlanMaxHeaders.project_task_number,
        PlanMaxHeaders.project_task_id,
        PlanMaxHeaders.project_task_description,
        PlanMaxHeaders.operating_unit_name,
        PlanMaxHeaders.region_of_order,
        PlanMaxHeaders.type_of_order,
        PlanMaxHeaders.hdr_order_type,
        PlanMaxHeaders.hdr_booked_date,
        PlanMaxHeaders.otm_tech_ocl_no,
        PlanMaxHeaders.fuel,
        PlanMaxHeaders.pressure,
        PlanMaxHeaders.special_instructions,
        PlanMaxHeaders.product_model,
        PlanMaxHeaders.ordered_date,
        PlanMaxHeaders.order_currency,
        PlanMaxHeaders.total_unit_value,
        PlanMaxHeaders.conversion_rate,
        PlanMaxHeaders.total_unit_value_in_inr,
        PlanMaxHeaders.prn_customer_dely_date,
        PlanMaxHeaders.prn_revised_dely_reqd_date,
        PlanMaxHeaders.prn_number,
        PlanMaxHeaders.prn_approved_date,
        PlanMaxHeaders.freight_pay,
        PlanMaxHeaders.inco_terms,
        PlanMaxHeaders.abp_percent,
        PlanMaxHeaders.pgb_percent,
        PlanMaxHeaders.bonus,
        PlanMaxHeaders.ld_applicable,
        PlanMaxHeaders.penalty,
        PlanMaxHeaders.insurance_by,
        PlanMaxHeaders.sales_engineer,
        PlanMaxHeaders.otm_header_id,
        PlanMaxHeaders.project_task_name,
        PlanMaxHeaders.proj_specific_llbom,
        PlanMaxHeaders.llbom_release_date,
        PlanMaxHeaders.llbom_pr,
        PlanMaxHeaders.di_number,
        PlanMaxHeaders.di_date,
        PlanMaxHeaders.di_value,
        PlanMaxHeaders.di_freight,
        PlanMaxHeaders.di_recommended_transporter,
        PlanMaxHeaders.di_transportation_scope,
        PlanMaxHeaders.last_invoice_no,
        PlanMaxHeaders.last_invoice_date,
        PlanMaxHeaders.invoiced_value,
        PlanMaxHeaders.contractual_plan_otp,
        PlanMaxHeaders.delivery_otp,
        PlanMaxHeaders.original_project_no,
        PlanMaxHeaders.rated_standard_man_hrs,
        PlanMaxHeaders.mfg_commitment_date,
        PlanMaxHeaders.plan_eol_mech_date,
        PlanMaxHeaders.plan_eol_ei_date,
        PlanMaxHeaders.folder_status,
        PlanMaxHeaders.regional_commercial,
        PlanMaxHeaders.actual_fg_date,
        PlanMaxHeaders.shop_subcontract,
        Customers.account_number,
        Customers.cust_account_id,
        Customers.party_id,
        Customers.party_number,
        Customers.party_name,
        Customers.creation_date,
        Customers.site_use_code,
        Customers.party_site_number,
        Customers.cust_acct_site_id,
        Customers.site_use_id,
        Customers.site_use_status,
        Customers.location_id,
        Customers.address1,
        Customers.address2,
        Customers.address3,
        Customers.address4,
        Customers.city,
        Customers.postal_code,
        Customers.state,
        Customers.province,
        Customers.country
    ).join(PlanMaxHeaders.customers)

    rolling_plan_view = ViewTable(
        display_name="Rolling Plan",
        table_header="Rolling Plan",
        table_description="Rolling plan details",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.model_line_number,
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
        actions=[],
        inline_actions=None,
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
        actions=[],
        inline_actions=None,
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
        actions=[],
        inline_actions=None,
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

    @staticmethod
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
        print("************************************************")
        return {"status": "success", "message": "Action Executed Successfully"}, 200

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
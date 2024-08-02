from sqlalchemy import Select, func

from efficieno.components.view_tables import ViewTable
from efficieno.components.views import View
from efficieno.components.view_actions import Action

from thermax_planmax.data_objects.headers import PlanMaxHeaders
from thermax_planmax.data_objects.order_headers import OrderHeaders
from thermax_planmax.data_objects.order_lines import OrderLines


class OrderHeaderDetails(View):
    query = (
        Select(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            # Customers.party_name,
            PlanMaxHeaders.group_name,
            PlanMaxHeaders.sub_group,
            PlanMaxHeaders.product_category,
            OrderHeaders.attribute6,
            # model,
            # pressure
            PlanMaxHeaders.mfg_organization_id,
            OrderHeaders.transactional_curr_code,
            OrderLines.unit_selling_price,
            OrderLines.ordered_quantity,
            OrderLines.cancelled_quantity,
            PlanMaxHeaders.curr_cust_required_date,
            # fuel,
            # special instructions
            OrderHeaders.freight_terms_code,
            OrderHeaders.fob_point_code,
            # prn_received_dt,
            # di_receipt_date
        )
        .join(OrderHeaders.planmax_headers)
        .join(OrderLines.planmax_headers)
    )

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
        return {"status": "success", "message": "Action Executed Successfully"}, 200

    update_order_intake_fields = Action(
        display_name="Demo action", action_type="update", action_function=fn_update_order_intake_fields
    )

    master_plan_view = ViewTable(
        display_name="Master Plan",
        table_header="Master Plan",
        table_description="All Orders view",
        query=query,
        column_properties={},
        actions=[update_order_intake_fields],
        inline_actions=update_order_intake_fields,
    )

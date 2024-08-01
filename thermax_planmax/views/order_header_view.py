from sqlalchemy import Select, func

from efficieno.components.view_tables import ViewTable
from efficieno.components.views import View
from thermax_planmax.data_objects.customers import Customers
from thermax_planmax.data_objects.headers import OrderHeaders
# from efficieno.demo.thermax_planmax.data_objects.model_xref import ModelXref
from thermax_planmax.data_objects.order_headers import OrderHeadersBase
from thermax_planmax.data_objects.order_lines import OrderLinesBase


class OrderHeaderDetails(View):
    # fuel_subq = (Select(TechOCLSpecs.otos_value_1).
    #              filter(TechOCLSpecs.otos_section == 'MAIN').
    #              filter(TechOCLSpecs.otm_header_id == ocl_h.otm_header_id))

    # model_subq = Select(ModelXref.model_number).filter(ModelXref.model_item == OrderHeaders.sos_item).subquery()

    query = (
        Select(
            OrderHeaders.curr_thx_commitment_date,
            OrderHeaders.project_number,
            OrderHeaders.sales_order_number,
            Customers.party_name,
            OrderHeaders.group_name,
            OrderHeaders.sub_group,
            OrderHeaders.product_category,
            OrderHeadersBase.attribute6,
            # model_subq,
            # pressure,
            OrderHeaders.mfg_organization_id,
            OrderHeadersBase.transactional_curr_code,
            # (
                # func.coalesce(OrderLinesBase.unit_selling_price, 0)
                # * (
                    # func.coalesce(OrderLinesBase.ordered_quantity, 0)
                    # + func.coalesce(OrderLinesBase.cancelled_quantity, 0)
                # )
            # )
            # / 100000,
            OrderHeaders.curr_cust_required_date,
            # fuel,
            # special_instructions,
            OrderHeadersBase.freight_terms_code,
            OrderHeadersBase.fob_point_code,
            # prn_received_dt,
            # di_receipt_date
        )
        .join(Customers)
        .join(OrderHeadersBase)
        .join(OrderLinesBase)
    )

    master_plan_view = ViewTable(
        display_name="Master Plan",
        table_header="Master Plan",
        table_description="All Orders view",
        query=query,
        column_properties={},
        actions=[],
        inline_actions=None,
    )

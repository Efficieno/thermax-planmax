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


class DIDetailsView(View):
    query = Select(
        PlanMaxHeaders,
        Customers,
        Calender,
        Organizations,
        DIDetails
    ).outerjoin(PlanMaxHeaders.di_details).outerjoin(PlanMaxHeaders.customers).outerjoin(PlanMaxHeaders.calender).outerjoin(PlanMaxHeaders.organizations)

    di_details_view = ViewTable(
        display_name="DI Details",
        table_header="DI Details",
        table_description="DI Details",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.model_line_number,
            Customers.party_name,
            DIDetails.plan_id,
            DIDetails.plan_name,
            DIDetails.organization_id,
            DIDetails.organization_name,
            DIDetails.collection_id,
            DIDetails.occurrence,
            DIDetails.last_update_date,
            DIDetails.last_updated_by_id,
            DIDetails.last_updated_by,
            DIDetails.creation_date,
            DIDetails.created_by_id,
            DIDetails.created_by,
            DIDetails.last_update_login,
            DIDetails.operating_unit,
            DIDetails.di_number,
            DIDetails.sales_order_no,
            DIDetails.customer_id,
            DIDetails.customer,
            DIDetails.xx_project_number,
            DIDetails.region_zone,
            DIDetails.area_country,
            DIDetails.partial_shipment_instructions,
            DIDetails.bill_to_address,
            DIDetails.bill_to_customer_person_name,
            DIDetails.ship_to_address,
            DIDetails.ship_to_customer_name,
            DIDetails.tin_no,
            DIDetails.cust_ecc_no,
            DIDetails.cst_no,
            DIDetails.epcg_licence_number_date,
            DIDetails.contact_person,
            DIDetails.contact_number,
            DIDetails.fax,
            DIDetails.email_address,
            DIDetails.receiver,
            DIDetails.payment_amount,
            DIDetails.br_cheque_number,
            DIDetails.br_cheque_date,
            DIDetails.recommended_transporter,
            DIDetails.freight,
            DIDetails.consignment_delivery_instructn,
            DIDetails.shipping_method,
            # DIDetails.mode,
            DIDetails.road_permit_status,
            DIDetails.payment_details1,
            DIDetails.amt1,
            DIDetails.payment_details2,
            DIDetails.amt2,
            DIDetails.payment_details3,
            DIDetails.amt3,
            DIDetails.payment_details4,
            DIDetails.amt4,
            DIDetails.total_amount,
            DIDetails.particulars1,
            DIDetails.qty1,
            DIDetails.amt6,
            DIDetails.particulars2,
            DIDetails.qty2,
            DIDetails.amt7,
            DIDetails.particulars3,
            DIDetails.qty3,
            DIDetails.amt8,
            DIDetails.particulars4,
            DIDetails.qty4,
            DIDetails.amt12,
            DIDetails.particulars5,
            DIDetails.qty5,
            DIDetails.amt14,
            DIDetails.particulars6,
            DIDetails.qty6,
            DIDetails.amt15,
            DIDetails.particulars7,
            DIDetails.qty7,
            DIDetails.amt16,
            DIDetails.basic_amount,
            DIDetails.packing__forwarding_amount,
            DIDetails.excisable_amount,
            DIDetails.excise__duty,
            DIDetails.amt17,
            DIDetails.cess_on_excise__duty,
            DIDetails.amt9,
            DIDetails.s_h_cess_on_excise__duty,
            DIDetails.amt10,
            DIDetails.insurance_charges,
            DIDetails.taxable_amount,
            DIDetails.cst,
            DIDetails.amt5,
            DIDetails.vat,
            DIDetails.amt13,
            DIDetails.full_taxes,
            DIDetails.amt11,
            DIDetails.freight_amount,
            DIDetails.service_tax,
            DIDetails.service_tax_amount,
            DIDetails.gross_amount,
            DIDetails.unloading_by,
            DIDetails.any_special_instruction,
            DIDetails.send_email,
            DIDetails.cgst,
            DIDetails.cgst_percentage,
            DIDetails.sgst,
            DIDetails.sgst_percentage,
        ).filter(PlanMaxHeaders.order_status == "OPEN"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

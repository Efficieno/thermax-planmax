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


class DetailPlan(View):
    query = Select(
        PlanMaxHeaders,
        PlanMaxLines,
        Customers,
        Calender,
        Organizations
    ).join(PlanMaxLines).outerjoin(PlanMaxHeaders.customers).outerjoin(PlanMaxHeaders.calender).outerjoin(PlanMaxHeaders.organizations)

    rolling_plan_details_view = ViewTable(
        display_name="Rolling Plan",
        table_header="Rolling Plan",
        table_description="Rolling plan details",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.model_line_number,
            Customers.party_name,
            PlanMaxLines.sales_order_header_id,
            PlanMaxLines.sales_order_header,
            PlanMaxLines.sales_order_line_id,
            PlanMaxLines.sales_order_line,
            PlanMaxLines.reference_line_id,
            PlanMaxLines.reference_line,
            PlanMaxLines.project_id,
            PlanMaxLines.organization_id,
            PlanMaxLines.bill_sequence_id,
            PlanMaxLines.bom_implementation_date,
            PlanMaxLines.change_notice,
            PlanMaxLines.common_bill_sequence_id,
            PlanMaxLines.common_organization_id,
            PlanMaxLines.assembly_item_id,
            PlanMaxLines.assembly_item,
            PlanMaxLines.assembly_item_type,
            PlanMaxLines.plan_level,
            PlanMaxLines.effectivity_date,
            PlanMaxLines.disable_date,
            PlanMaxLines.item_num,
            PlanMaxLines.operation_seq_num,
            PlanMaxLines.implementation_date,
            PlanMaxLines.component_code,
            PlanMaxLines.component_item_id,
            PlanMaxLines.component_item,
            PlanMaxLines.component_item_revision_war,
            PlanMaxLines.component_item_revision_en1,
            PlanMaxLines.component_item_type,
            PlanMaxLines.component_quantity,
            PlanMaxLines.engg_org_exists,
            PlanMaxLines.warehouse_org_exists,
            PlanMaxLines.extended_quantity,
            PlanMaxLines.component_shippable_item_flag,
            PlanMaxLines.planning_make_buy_code,
            PlanMaxLines.primary_unit_of_measure,
            PlanMaxLines.item_cost,
            PlanMaxLines.line_item_type,
            PlanMaxLines.line_item_sub_type,
            PlanMaxLines.project_number
        ).filter(PlanMaxHeaders.order_status == "OPEN"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

    detail_lines_view = ViewTable(
        display_name="Details View",
        table_header="Details View",
        table_description="Details View",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.model_line_number,
            Customers.party_name,
            PlanMaxLines.sales_order_header_id,
            PlanMaxLines.sales_order_header,
            PlanMaxLines.sales_order_line_id,
            PlanMaxLines.sales_order_line,
            PlanMaxLines.reference_line_id,
            PlanMaxLines.reference_line,
            PlanMaxLines.project_id,
            PlanMaxLines.organization_id,
            PlanMaxLines.bill_sequence_id,
            PlanMaxLines.bom_implementation_date,
            PlanMaxLines.change_notice,
            PlanMaxLines.common_bill_sequence_id,
            PlanMaxLines.common_organization_id,
            PlanMaxLines.assembly_item_id,
            PlanMaxLines.assembly_item,
            PlanMaxLines.assembly_item_type,
            PlanMaxLines.plan_level,
            PlanMaxLines.effectivity_date,
            PlanMaxLines.disable_date,
            PlanMaxLines.item_num,
            PlanMaxLines.operation_seq_num,
            PlanMaxLines.implementation_date,
            PlanMaxLines.component_code,
            PlanMaxLines.component_item_id,
            PlanMaxLines.component_item,
            PlanMaxLines.component_item_revision_war,
            PlanMaxLines.component_item_revision_en1,
            PlanMaxLines.component_item_type,
            PlanMaxLines.component_quantity,
            PlanMaxLines.engg_org_exists,
            PlanMaxLines.warehouse_org_exists,
            PlanMaxLines.extended_quantity,
            PlanMaxLines.component_shippable_item_flag,
            PlanMaxLines.planning_make_buy_code,
            PlanMaxLines.primary_unit_of_measure,
            PlanMaxLines.item_cost,
            PlanMaxLines.line_item_type,
            PlanMaxLines.line_item_sub_type,
            PlanMaxLines.project_number
        ).filter(PlanMaxHeaders.order_status == "OPEN"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

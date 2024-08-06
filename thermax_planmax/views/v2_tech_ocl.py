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


class TechOCLDetails(View):
    query = Select(
        PlanMaxHeaders,
        Customers,
        Calender,
        Organizations,
        TechOCLLines,
    ).outerjoin(TechOCLLines).outerjoin(PlanMaxHeaders.customers).outerjoin(PlanMaxHeaders.calender).outerjoin(PlanMaxHeaders.organizations)

    tech_ocl_details_view = ViewTable(
        display_name="Tech OCL Details",
        table_header="Tech OCL Details",
        table_description="Tech OCL Details",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.model_line_number,
            Customers.party_name,
            TechOCLLines.otos_line_id,
            TechOCLLines.otm_header_id,
            TechOCLLines.organization_id,
            TechOCLLines.otos_der_model_no,
            TechOCLLines.otos_param_id,
            TechOCLLines.otos_section,
            TechOCLLines.otos_param_name,
            TechOCLLines.otos_srl_no,
            TechOCLLines.otos_value_1,
            TechOCLLines.otos_value_2,
            TechOCLLines.otos_value_3,
            TechOCLLines.created_by,
            TechOCLLines.creation_date,
            TechOCLLines.last_updated_by,
            TechOCLLines.last_update_date,
            TechOCLLines.last_update_login,
            TechOCLLines.otos_remark,
        ).filter(PlanMaxHeaders.order_status == "OPEN"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

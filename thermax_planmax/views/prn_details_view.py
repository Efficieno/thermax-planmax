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


class PRNDetailsView(View):
    query = Select(
        PlanMaxHeaders,
        Customers,
        Calender,
        Organizations,
        PRNDetails
    ).outerjoin(PlanMaxHeaders.prn_details).outerjoin(PlanMaxHeaders.customers).outerjoin(PlanMaxHeaders.calender).outerjoin(PlanMaxHeaders.organizations)

    all_cols_prn_details_v = ViewTable(
        display_name="PRN Details",
        table_header="PRN Details",
        table_description="PRN Details",
        query=query.with_only_columns(
            PlanMaxHeaders.curr_thx_commitment_date,
            PlanMaxHeaders.project_number,
            PlanMaxHeaders.sales_order_number,
            PlanMaxHeaders.model_line_number,
            Customers.party_name,
            PRNDetails.plan_id,
            PRNDetails.plan_name,
            PRNDetails.organization_id,
            PRNDetails.organization_name,
            PRNDetails.collection_id,
            PRNDetails.occurrence,
            PRNDetails.last_update_date,
            PRNDetails.last_updated_by_id,
            PRNDetails.last_updated_by,
            PRNDetails.creation_date,
            PRNDetails.created_by_id,
            PRNDetails.created_by,
            PRNDetails.last_update_login,
            PRNDetails.so_header_id,
            PRNDetails.sales_order_number,
            PRNDetails.customer_id,
            PRNDetails.customer,
            PRNDetails.project_number_so,
            PRNDetails.region_zone,
            PRNDetails.area_country,
            PRNDetails.ch_product_type,
            PRNDetails.group_route,
            PRNDetails.customer_dely_date,
            PRNDetails.prn_number,
            PRNDetails.revised_dely_reqd_date,
            PRNDetails.prn_status,
            PRNDetails.prn_approved_date,
            PRNDetails.remarks,
            PRNDetails.reporting_employee
        ).filter(PlanMaxHeaders.order_status == "OPEN"),
        column_properties={},
        actions=[],
        inline_actions=None,
    )

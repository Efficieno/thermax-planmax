from efficieno.components.relations import Relations

# Data Views
from thermax_planmax.views.rolling_plan_view import RollingPlan
from thermax_planmax.views.master_plan_details_view import MasterPlanLines
from thermax_planmax.views.di_details_view import DIDetailsView
from thermax_planmax.views.tech_ocl_lines_view import TechOCLLinesView
from thermax_planmax.views.master_plan_headers_view import MasterPlanHeaders
from thermax_planmax.views.prn_details_view import PRNDetailsView

# Data Objects
from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders
from thermax_planmax.data_objects.planmax_lines import PlanMaxLines
from thermax_planmax.data_objects.di_details import DIDetails
from thermax_planmax.data_objects.tech_ocl_lines import TechOCLLines
from thermax_planmax.data_objects.prn_details import PRNDetails 


# Rolling plan Relations 

Relations.add_relations(
    relation_name="rolling_master_details",
    source=RollingPlan.all_cols_rolling_plan_view,
    destination=MasterPlanLines.all_cols_master_plan_lines_v,
    join_conditions=[(PlanMaxHeaders.sales_order_header_id, PlanMaxLines.sales_order_header_id),
                     (PlanMaxHeaders.model_line_id, PlanMaxLines.reference_line_id)]
    )


Relations.add_relations(
    relation_name="rolling_master_di",
    source=RollingPlan.all_cols_rolling_plan_view,
    destination=DIDetailsView.all_cols_di_details_v,
    join_conditions=[(PlanMaxHeaders.sales_order_number, DIDetails.sales_order_no),
                     (PlanMaxHeaders.project_number, DIDetails.xx_project_number)]
    )

Relations.add_relations(
    relation_name="rolling_master_tech_ocl",
    source=RollingPlan.all_cols_rolling_plan_view,
    destination=TechOCLLinesView.all_cols_tech_ocl_lines_v,
    join_conditions=[(PlanMaxHeaders.otm_header_id, TechOCLLines.otm_header_id)]
    )

Relations.add_relations(
    relation_name="rolling_master_prn",
    source=RollingPlan.all_cols_rolling_plan_view,
    destination=PRNDetailsView.all_cols_prn_details_v,
    join_conditions=[(PlanMaxHeaders.sales_order_header_id, PRNDetails.so_header_id),
                     (PlanMaxHeaders.project_number, PRNDetails.project_number_so)]
    )


# Master plan Drill Down 

Relations.add_relations(
    relation_name="rolling_master_details",
    source=MasterPlanHeaders.all_cols_master_plan_headers_v,
    destination=MasterPlanLines.all_cols_master_plan_lines_v,
    join_conditions=[(PlanMaxHeaders.sales_order_header_id, PlanMaxLines.sales_order_header_id),
                     (PlanMaxHeaders.model_line_id, PlanMaxLines.reference_line_id)]
    )


Relations.add_relations(
    relation_name="rolling_master_di",
    source=MasterPlanHeaders.all_cols_master_plan_headers_v,
    destination=DIDetailsView.all_cols_di_details_v,
    join_conditions=[(PlanMaxHeaders.sales_order_number, DIDetails.sales_order_no),
                     (PlanMaxHeaders.project_number, DIDetails.xx_project_number)]
    )

Relations.add_relations(
    relation_name="rolling_master_tech_ocl",
    source=MasterPlanHeaders.all_cols_master_plan_headers_v,
    destination=TechOCLLinesView.all_cols_tech_ocl_lines_v,
    join_conditions=[(PlanMaxHeaders.otm_header_id, TechOCLLines.otm_header_id)]
    )

Relations.add_relations(
    relation_name="rolling_master_prn_detls",
    source=MasterPlanHeaders.all_cols_master_plan_headers_v,
    destination=PRNDetailsView.all_cols_prn_details_v,
    join_conditions=[(PlanMaxHeaders.sales_order_header_id, PRNDetails.so_header_id),
                     (PlanMaxHeaders.project_number, PRNDetails.project_number_so)]
    )

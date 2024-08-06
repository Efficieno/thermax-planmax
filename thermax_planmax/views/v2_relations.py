from efficieno.components.relations import Relations

# Data Views
from thermax_planmax.views.v2_rolling_plan import RollingPlan
from thermax_planmax.views.v2_detail_plan import DetailPlan
from thermax_planmax.views.v2_di_details import DIDetailsView
from thermax_planmax.views.v2_tech_ocl import TechOCLDetails

# Data Objects
from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders
from thermax_planmax.data_objects.planmax_lines import PlanMaxLines
from thermax_planmax.data_objects.di_details import DIDetails
from thermax_planmax.data_objects.tech_ocl_lines import TechOCLLines


# Rolling plan Relations 

Relations.add_relations(
    relation_name="rolling_master_details",
    source=RollingPlan.rolling_plan_view,
    destination=DetailPlan.rolling_plan_details_view,
    join_conditions=[(PlanMaxHeaders.sales_order_header_id, PlanMaxLines.sales_order_header_id),
                     (PlanMaxHeaders.model_line_id, PlanMaxLines.reference_line_id)]
    )


Relations.add_relations(
    relation_name="rolling_master_di",
    source=RollingPlan.rolling_plan_view,
    destination=DIDetailsView.di_details_view,
    join_conditions=[(PlanMaxHeaders.sales_order_number, DIDetails.sales_order_no),
                     (PlanMaxHeaders.project_number, DIDetails.xx_project_number)]
    )

Relations.add_relations(
    relation_name="rolling_master_tech_ocl",
    source=RollingPlan.rolling_plan_view,
    destination=TechOCLDetails.tech_ocl_details_view,
    join_conditions=[(PlanMaxHeaders.otm_header_id, TechOCLLines.otm_header_id)]
    )

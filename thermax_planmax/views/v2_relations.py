from efficieno.components.relations import Relations

# Data Views
from thermax_planmax.views.v2_rolling_plan import RollingPlan
from thermax_planmax.views.v2_detail_plan import DetailPlan

# Data Objects
from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders
from thermax_planmax.data_objects.planmax_lines import PlanMaxLines


Relations.add_relations(
    relation_name="rolling_master_details",
    source=RollingPlan.rolling_plan_view,
    destination=DetailPlan.rolling_plan_details_view,
    join_conditions=[(PlanMaxHeaders.sales_order_header_id, PlanMaxLines.sales_order_header_id),
                     (PlanMaxHeaders.model_line_id, PlanMaxLines.reference_line_id)]
    )

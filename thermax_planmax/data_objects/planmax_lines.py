from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Float, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class PlanMaxLines(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "XXPLANMAX_LINE_DTLS"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    sales_order_header_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata(invisible=True)})
    sales_order_header: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Sales Order Number")})
    sales_order_line_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata(invisible=True)})
    sales_order_line: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Sales Order Line")})
    reference_line_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    reference_line: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Reference Line")})
    project_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    bill_sequence_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    bom_implementation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="BOM Implimentation Date")})
    change_notice: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="ECO Number")})
    common_bill_sequence_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    common_organization_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    assembly_item_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    assembly_item: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Parent Item")})
    assembly_item_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Assembly Item Type")})
    plan_level: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Plan level")})
    effectivity_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Effectivity Date")})
    disable_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Disable Date")})
    item_num: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Item Num")})
    operation_seq_num: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Operation Seq Num")})
    implementation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Implimentation Date")})
    component_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    component_item_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    component_item: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Component Name")})
    component_item_revision_war: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Component Revision (MFG)")})
    component_item_revision_en1: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Component Revision (EN1)")})
    component_item_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Component Item Type")})
    component_quantity: Mapped[str] = mapped_column(Float, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Component Quantity")})
    engg_org_exists: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Exists in Eng Org")})
    warehouse_org_exists: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Exists in MFG org")})
    extended_quantity: Mapped[str] = mapped_column(Float, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Extended Quantity")})
    component_shippable_item_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Comp Shippable Flag")})
    planning_make_buy_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Planning Make/Buy Code")})
    primary_unit_of_measure: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Primary UOM")})
    item_cost: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Item Cost")})
    line_item_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Line Item Type")})
    line_item_sub_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Line Item Sub Type")})
    project_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Project Number")})
    show_on_view: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    order_line_item_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Order Line Item Type")})
    shippable_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Shippable Flag")})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="planmax_lines",
                                                             primaryjoin="and_(foreign(PlanMaxHeaders.sales_order_header_id)==PlanMaxLines.sales_order_header_id,"
                                                                         "foreign(PlanMaxHeaders.model_line_id)==PlanMaxLines.reference_line_id)")


"""
sales_order_header_id
sales_order_header
sales_order_line_id
sales_order_line
reference_line_id
reference_line
project_id
organization_id
bill_sequence_id
bom_implementation_date
change_notice
common_bill_sequence_id
common_organization_id
assembly_item_id
assembly_item
assembly_item_type
plan_level
effectivity_date
disable_date
item_num
operation_seq_num
implementation_date
component_code
component_item_id
component_item
component_item_revision_war
component_item_revision_en1
component_item_type
component_quantity
engg_org_exists
warehouse_org_exists
extended_quantity
component_shippable_item_flag
planning_make_buy_code
primary_unit_of_measure
item_cost
line_item_type
line_item_sub_type
project_number
show_on_view
order_line_item_type
shippable_flag
"""

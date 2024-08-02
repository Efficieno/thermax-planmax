from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase



class PlanMaxLines(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "XXPLANMAX_LINE_DTLS"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    sales_order_header_id: Mapped[str] = mapped_column(
        ForeignKey("apps.oe_order_headers_all.header_id"),
        primary_key=False,
        info={"column_metadata": ColumnMetadata()},
    )
    sales_order_header: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    sales_order_line_id: Mapped[str] = mapped_column(
        ForeignKey("apps.oe_order_lines_all.line_id"), primary_key=True, info={"column_metadata": ColumnMetadata()}
    )
    sales_order_line: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_line_id: Mapped[str] = mapped_column(
        ForeignKey("apps.oe_order_lines_all.line_id"),
        primary_key=False,
        info={"column_metadata": ColumnMetadata()},
    )
    reference_line: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_sequence_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    bom_implementation_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    change_notice: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    common_bill_sequence_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    common_organization_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    assembly_item_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    assembly_item: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    assembly_item_type: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    plan_level: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    effectivity_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    disable_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_num: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    operation_seq_num: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    implementation_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    component_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_item_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    component_item: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_item_revision_war: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    component_item_revision_en1: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    component_item_type: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    component_quantity: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    engg_org_exists: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    warehouse_org_exists: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    extended_quantity: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    component_shippable_item_flag: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    planning_make_buy_code: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    primary_unit_of_measure: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    item_cost: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_item_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_item_sub_type: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )

    # headers: Mapped["OrderHeaders"] = relationship(back_populates="lines")

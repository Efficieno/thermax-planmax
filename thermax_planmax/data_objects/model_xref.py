from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Float, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class ModelXref(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "XXPLANMAX_MODEL_XREF"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    model_item: Mapped[str] = mapped_column(String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    model_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_planner: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    std_rsmh: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_applicable: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    full_lead_time: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_category: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="model_xref",
                                                             primaryjoin="foreign(PlanMaxHeaders.sos_item)==ModelXref.model_item")


"""
model_item
model_number
product_planner
std_rsmh
prn_applicable
full_lead_time
product_category
"""

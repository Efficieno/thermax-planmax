from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    pass


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

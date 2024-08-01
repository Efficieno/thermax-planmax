from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    pass


class ModelXref(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "XXPLANMAX_MODEL_XREF"
    __table_args__ = {"schema": "apps"}

    xref_model_item: Mapped[str] = mapped_column('model_item', String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    xref_model_number: Mapped[str] = mapped_column('model_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    xref_product_planner: Mapped[str] = mapped_column('product_planner', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    xref_std_rsmh: Mapped[str] = mapped_column('std_rsmh', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    xref_prn_applicable: Mapped[str] = mapped_column('prn_applicable', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    xref_full_lead_time: Mapped[str] = mapped_column('full_lead_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    xref_product_category: Mapped[str] = mapped_column('product_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

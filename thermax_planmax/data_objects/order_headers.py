from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.headers import PlanMaxHeaders
    from thermax_planmax.data_objects.order_lines import OrderLines


class OrderHeaders(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "oe_order_headers_all"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    header_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    attribute6: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transactional_curr_code: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    freight_terms_code: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    fob_point_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})

    order_lines: Mapped["OrderLines"] = relationship(back_populates="order_headers")
    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="order_headers")

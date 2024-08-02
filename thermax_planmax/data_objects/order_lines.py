from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.headers import PlanMaxHeaders
    from thermax_planmax.data_objects.order_headers import OrderHeaders


class OrderLines(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "oe_order_lines_all"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    header_id: Mapped[str] = mapped_column(
        ForeignKey("apps.oe_order_headers_all.header_id"), primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    line_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    unit_selling_price: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    ordered_quantity: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    cancelled_quantity: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )

    order_headers: Mapped["OrderHeaders"] = relationship(back_populates="order_lines")
    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="order_lines")

    # order_lines_base: Mapped["OrderHeadersBase"] = relationship(back_populates="order_headers_base")

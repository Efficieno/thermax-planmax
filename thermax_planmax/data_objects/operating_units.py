from typing import TYPE_CHECKING

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class OperatingUnits(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "hr_operating_units"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    business_group_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_from: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_to: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    short_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    set_of_books_id: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_legal_context_id: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    usable_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="operating_unit",
                                                             primaryjoin="foreign(PlanMaxHeaders.operating_unit_id)==OperatingUnits.organization_id")


"""
business_group_id
organization_id
name
date_from
date_to
short_code
set_of_books_id
default_legal_context_id
usable_flag
"""

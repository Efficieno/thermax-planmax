from typing import TYPE_CHECKING

from sqlalchemy.dialects.oracle.types import VARCHAR2, NUMBER, FLOAT, LONG, DATE, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class OrderTypes(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "oe_transaction_types_tl"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    transaction_type_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    language: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_lang: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="order_types",
                                                             primaryjoin="foreign(PlanMaxHeaders.order_type_id)==OrderTypes.transaction_type_id")


"""
transaction_type_id
language
source_lang
name
description
creation_date
created_by
last_update_date
last_updated_by
last_update_login
program_application_id
program_id
request_id
"""

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from efficieno.ontology.base import ObjectBase, ColumnMetadata
from thermax_planmax.data_objects.employee import Employee


class Department(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "dept"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    deptno: Mapped[str] = mapped_column(String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    dname: Mapped[str] = mapped_column(String, info={"column_metadata": ColumnMetadata()})
    loc: Mapped[str] = mapped_column(String, info={"column_metadata": ColumnMetadata()})

    employee: Mapped[list[Employee]] = relationship(back_populates="department")


    @classmethod
    def insert(cls, row: dict):
        print("Invoking insert")
        print(f"Row {row}")

    @classmethod
    def delete(cls, row: dict):
        print("Invoking Delete ")
        print(f"Row {row}")

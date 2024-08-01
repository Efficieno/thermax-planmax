from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from efficieno.ontology.base import ObjectBase, ColumnMetadata

if TYPE_CHECKING:
    from thermax_planmax.data_objects.department import Department
else:
    Department = "Department"


class Employee(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "emp"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    empno: Mapped[int] = mapped_column(primary_key=True, info={"column_metadata": ColumnMetadata()})
    ename: Mapped[str] = mapped_column(String, info={"column_metadata": ColumnMetadata()})
    job: Mapped[str] = mapped_column(String, info={"column_metadata": ColumnMetadata()})
    mgr: Mapped[str] = mapped_column(String, info={"column_metadata": ColumnMetadata()})
    hiredate: Mapped[str] = mapped_column(Date, info={"column_metadata": ColumnMetadata()})
    sal: Mapped[str] = mapped_column(Integer, info={"column_metadata": ColumnMetadata()})
    comm: Mapped[str] = mapped_column(Integer, info={"column_metadata": ColumnMetadata()})
    deptno: Mapped[str] = mapped_column(ForeignKey("apps.dept.deptno"), info={"column_metadata": ColumnMetadata()})
    department: Mapped["Department"] = relationship(
        back_populates="employee", info={"column_metadata": ColumnMetadata()}
    )


    @classmethod
    def insert(cls, row: dict):
        print("Invoking insert")
        print(f"Row {row}")

    @classmethod
    def delete(cls, row: dict):
        print("Invoking Delete ")
        print(f"Row {row}")

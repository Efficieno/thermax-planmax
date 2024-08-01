from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from efficieno.ontology.base import ColumnMetadata, ObjectBase


class OperatingUnits(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "hr_operating_units"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    business_group_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    name: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Operating Unit Name")}
    )

    @classmethod
    def insert(cls, row: dict):
        pass

    @classmethod
    def update(cls, old_row: dict, updated_columns: list):
        pass

    @classmethod
    def delete(cls, row: dict):
        pass

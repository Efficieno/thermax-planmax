from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from efficieno.ontology.base import ColumnMetadata, ObjectBase


class OrderTypes(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "oe_transaction_types_tl"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    transaction_type_id: Mapped[str] = mapped_column(
        Integer, primary_key=True, info={"column_metadata": ColumnMetadata()}
    )
    language: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    name: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Order Type")}
    )
    description: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})

    @classmethod
    def insert(cls, row: dict):
        pass

    @classmethod
    def update(cls, old_row: dict, updated_columns: list):
        pass

    @classmethod
    def delete(cls, row: dict):
        pass

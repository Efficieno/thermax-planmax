from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from efficieno.ontology.base import ColumnMetadata, ObjectBase


class InventoryItems(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "mtl_system_items"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    inventory_item_id: Mapped[str] = mapped_column(
        Integer, primary_key=True, info={"column_metadata": ColumnMetadata()}
    )
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment1: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Item Number")}
    )
    description: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    enabled_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    purchasing_item_flag: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    shippable_item_flag: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    customer_order_flag: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    inventory_item_flag: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    bom_enabled_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    build_in_wip_flag: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
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

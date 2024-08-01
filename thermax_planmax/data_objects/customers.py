from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from efficieno.demo.demo_project.data_objects.order_headers import OrderHeader


class Customers(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_customer_details"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    party_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_number: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Customer Number")}
    )
    party_name: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Customer Name")}
    )
    party_site_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_site_number: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    party_site_status: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    cust_acct_site_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    cust_account_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_use_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_use_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    primary_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    location: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Location")}
    )
    country: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Country")}
    )
    address1: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address2: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address3: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address4: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    city: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="City")}
    )
    postal_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    state: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="State")}
    )
    province: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    county: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address_key: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})

    orders: Mapped["OrderHeader"] = relationship(back_populates="customers")

    @classmethod
    def insert(cls, row: dict):
        pass

    @classmethod
    def update(cls, old_row: dict, updated_columns: list):
        pass

    @classmethod
    def delete(cls, row: dict):
        pass

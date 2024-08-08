from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Float, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class Customers(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_cust_dtls"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    account_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Account Number")})
    cust_account_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    party_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    party_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Customer Number")})
    party_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Customer Name")})
    creation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_use_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Site use Code")})
    party_site_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cust_acct_site_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    site_use_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata(invisible=True)})
    site_use_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    location_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    address1: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Address 1")})
    address2: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Address 2")})
    address3: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Address 3")})
    address4: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Address 4")})
    city: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="City")})
    postal_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Postal Code")})
    state: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="State")})
    province: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Province")})
    country: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Country")})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="customers",
                                                             primaryjoin="foreign(PlanMaxHeaders.ship_site_use_id)==Customers.site_use_id")


"""
account_number
cust_account_id
party_id
party_number
party_name
creation_date
site_use_code
party_site_number
cust_acct_site_id
site_use_id
site_use_status
location_id
address1
address2
address3
address4
city
postal_code
state
province
country
"""

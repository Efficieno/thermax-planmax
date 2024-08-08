from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Float, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class PRNDetails(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "Q_PRODUCTION_RELEASE_NOTE_ST_V"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    plan_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    plan_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    organization_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Org Name")})
    collection_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    occurrence: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    last_update_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Last Update Date")})
    last_updated_by_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    last_updated_by: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Last Updated By")})
    creation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Creation Date")})
    created_by_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    created_by: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Created By")})
    last_update_login: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    so_header_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    sales_order_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Sales Order Number")})
    customer_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    customer: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Customer Name")})
    project_number_so: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Project Number")})
    region_zone: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Region")})
    area_country: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Area")})
    ch_product_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Product Type")})
    group_route: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Group Route")})
    customer_dely_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Customer Delivery Date")})
    prn_number: Mapped[str] = mapped_column(String, primary_key=True, info={"column_metadata": ColumnMetadata(display_name="PRN Number")})
    revised_dely_reqd_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Revised Delivery Required Date")})
    prn_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="PRN Status")})
    prn_approved_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="PRN Approved Date")})
    remarks: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Remarks")})
    reporting_employee: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Reporting Employee")})

    # planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="prn_details",
    #                                                          primaryjoin="and_(foreign(PlanMaxHeaders.sales_order_header_id)==PRNDetails.so_header_id,"
    #                                                                      "foreign(PlanMaxHeaders.project_number)==PRNDetails.project_number_so)")

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="prn_details",
                                                             primaryjoin="foreign(PlanMaxHeaders.sales_order_number)==PRNDetails.sales_order_number")



"""
plan_id
plan_name
organization_id
organization_name
collection_id
occurrence
last_update_date
last_updated_by_id
last_updated_by
creation_date
created_by_id
created_by
last_update_login
so_header_id
sales_order_number
customer_id
customer
project_number_so
region_zone
area_country
ch_product_type
group_route
customer_dely_date
prn_number
revised_dely_reqd_date
prn_status
prn_approved_date
remarks
reporting_employee
"""

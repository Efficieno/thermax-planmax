from typing import TYPE_CHECKING

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    pass


class PRNDetails(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "Q_PRODUCTION_RELEASE_NOTE_ST_V"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    plan_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plan_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_name: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    collection_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    occurrence: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    last_updated_by: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    so_header_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    sales_order_number: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    customer_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_number_so: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    region_zone: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    area_country: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ch_product_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_route: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_dely_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revised_dely_reqd_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    prn_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_approved_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    remarks: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reporting_employee: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )

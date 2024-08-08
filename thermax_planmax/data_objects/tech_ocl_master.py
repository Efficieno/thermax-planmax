from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Float, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.order_lines import PlanMaxHeaders


class TechOCLMaster(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxtmx_tech_ocl_mstr_tbl"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    otm_header_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata(invisible=True)})
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otm_tech_ocl_no: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Tech OCL Number")})
    otm_tech_ocl_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Tech OCL Date")})
    otm_tech_ocl_amd_no: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Ammendment Number")})
    otm_tech_ocl_amd_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Ammendment Date")})
    otm_sales_order_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otm_sales_order_no: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Sales Order Number")})
    otm_model_family: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Model Family")})
    otm_model_no: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Model Number")})
    otm_item_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Item Code")})
    otm_item_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otm_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Status")})
    otm_authorized_by: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Authorized By")})
    otm_authorized_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Authorized Date")})
    created_by: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    creation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Creation Date")})
    last_updated_by: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    last_update_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Last Update Date")})
    last_update_login: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otm_sales_order_line_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otm_sales_order_line_num: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Sales Order Line Number")})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="tech_ocl_master",
                                                             primaryjoin="foreign(PlanMaxHeaders.otm_header_id)==TechOCLMaster.otm_header_id")


"""
otm_header_id
organization_id
otm_tech_ocl_no
otm_tech_ocl_date
otm_tech_ocl_amd_no
otm_tech_ocl_amd_date
otm_sales_order_id
otm_sales_order_no
otm_model_family
otm_model_no
otm_item_code
otm_item_id
otm_status
otm_authorized_by
otm_authorized_date
created_by
creation_date
last_updated_by
last_update_date
last_update_login
otm_sales_order_line_id
otm_sales_order_line_num
"""

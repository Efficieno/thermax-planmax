from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Float, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class TechOCLLines(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxtmx_tech_ocl_specs_tbl"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    otos_line_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata(invisible=True)})
    otm_header_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    organization_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otos_der_model_no: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Model Number")})
    otos_param_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otos_section: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Section")})
    otos_param_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Parameter Name")})
    otos_srl_no: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otos_value_1: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Value 1")})
    otos_value_2: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Value 2")})
    otos_value_3: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Value 3")})
    created_by: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    creation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    last_updated_by: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    last_update_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    last_update_login: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata(invisible=True)})
    otos_remark: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata(display_name="Remarks")})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="tech_ocl_lines",
                                                             primaryjoin="foreign(PlanMaxHeaders.otm_header_id)==TechOCLLines.otm_header_id")


"""
otos_line_id
otm_header_id
organization_id
otos_der_model_no
otos_param_id
otos_section
otos_param_name
otos_srl_no
otos_value_1
otos_value_2
otos_value_3
created_by
creation_date
last_updated_by
last_update_date
last_update_login
otos_remark
"""

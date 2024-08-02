from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.customers import Customers


class PlanMaxHeaders(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "XXPLANMAX_HEADER_DTLS"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    operating_unit_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    sales_order_header_id: Mapped[str] = mapped_column(
        Integer, primary_key=True, info={"column_metadata": ColumnMetadata()}
    )
    sales_order_number: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    model_line_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    model_line_number: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    order_type_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sub_group: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_category: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_applicable: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inspection_required: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    project_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    std_nstd: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_item: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mfg_organization_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    orig_cust_required_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    curr_cust_required_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    orig_thx_commitment_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    curr_thx_commitment_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    ho_order_commited_to: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    ho_order_so_header: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    ho_order_so_line: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_no: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tech_clarity_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    engg_commt_dt: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_closure_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planned_invoice_dates: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    planned_invoice_value: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    wip_folder_release_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    commissioning_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_release_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planner: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tca: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    send_email: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fg_month_change_remarks: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    shell_boiler_appr_auth: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    reason_for_otp: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    interface_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    refresh_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_site_use_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    bill_cust_acct_site_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    bill_party_site_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    bill_party_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_location_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    ship_site_use_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    ship_cust_acct_site_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    ship_party_site_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    ship_party_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_location_id: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    order_intake_status: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    bom_common_status: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    reflection_config_status: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    mat_planning_status: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    sourcing_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    commit_dates_status_mfg: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    commit_dates_status_mat: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    mfg_job_folder_status: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    prn_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eol_mat_avail_status: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    wip_pur_mat_status: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    project_segment1: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_description: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    project_task_number: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    project_task_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_description: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    operating_unit_name: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    region_of_order: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    type_of_order: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hdr_order_type: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hdr_booked_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_tech_ocl_no: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fuel: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pressure: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    special_instructions: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    product_model: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ordered_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_currency: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    total_unit_value: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    conversion_rate: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    total_unit_value_in_inr: Mapped[str] = mapped_column(
        Integer, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    prn_customer_dely_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    prn_revised_dely_reqd_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    prn_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_approved_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_pay: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inco_terms: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    abp_percent: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pgb_percent: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bonus: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ld_applicable: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    penalty: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    insurance_by: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_engineer: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_header_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_name: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    proj_specific_llbom: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    llbom_release_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    llbom_pr: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_value: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_freight: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_recommended_transporter: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    di_transportation_scope: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    last_invoice_no: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_invoice_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoiced_value: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contractual_plan_otp: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    delivery_otp: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    original_project_no: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    rated_standard_man_hrs: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    mfg_commitment_date: Mapped[str] = mapped_column(
        Date, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    plan_eol_mech_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plan_eol_ei_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    folder_status: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    regional_commercial: Mapped[str] = mapped_column(
        String, primary_key=False, info={"column_metadata": ColumnMetadata()}
    )
    actual_fg_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shop_subcontract: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})

    customers: Mapped["Customers"] = relationship(
        back_populates="planmax_headers",
        primaryjoin="foreign(PlanMaxHeaders.ship_site_use_id)==Customers.site_use_id",
    )

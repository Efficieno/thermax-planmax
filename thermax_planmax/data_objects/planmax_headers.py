from typing import TYPE_CHECKING

from sqlalchemy.dialects.oracle.types import VARCHAR2, NUMBER, FLOAT, LONG, DATE, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.calender import Calender
    from thermax_planmax.data_objects.customers import Customers
    from thermax_planmax.data_objects.di_details import DIDetails
    from thermax_planmax.data_objects.invoice_headers import InvoiceHeaders
    from thermax_planmax.data_objects.model_xref import ModelXref
    from thermax_planmax.data_objects.operating_units import OperatingUnits
    from thermax_planmax.data_objects.order_headers import OrderHeaders
    from thermax_planmax.data_objects.order_lines import OrderLines
    from thermax_planmax.data_objects.order_types import OrderTypes
    from thermax_planmax.data_objects.organizations import Organizations
    from thermax_planmax.data_objects.planmax_lines import PlanMaxLines
    from thermax_planmax.data_objects.prn_details import PRNDetails
    from thermax_planmax.data_objects.projects_po import ProjectPODetails
    from thermax_planmax.data_objects.tech_ocl_master import TechOCLMaster
    from thermax_planmax.data_objects.tech_ocl_lines import TechOCLLines


class PlanMaxHeaders(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "XXPLANMAX_HEADER_DTLS"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    operating_unit_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_order_header_id: Mapped[str] = mapped_column(NUMBER, primary_key=True, info={"column_metadata": ColumnMetadata()})
    sales_order_number: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    model_line_id: Mapped[str] = mapped_column(NUMBER, primary_key=True, info={"column_metadata": ColumnMetadata()})
    model_line_number: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_type_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sub_group: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_category: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_applicable: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inspection_required: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_number: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    std_nstd: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_item: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mfg_organization_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_cust_required_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    curr_cust_required_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_thx_commitment_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    curr_thx_commitment_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ho_order_commited_to: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ho_order_so_header: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ho_order_so_line: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_no: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tech_clarity_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    engg_commt_dt: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_closure_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planned_invoice_dates: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planned_invoice_value: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_folder_release_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    commissioning_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_release_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planner: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tca: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    send_email: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fg_month_change_remarks: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shell_boiler_appr_auth: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reason_for_otp: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    interface_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    refresh_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_site_use_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_cust_acct_site_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_party_site_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_party_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_location_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_site_use_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_cust_acct_site_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_party_site_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_party_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_location_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_intake_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_common_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reflection_config_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mat_planning_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sourcing_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    commit_dates_status_mfg: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    commit_dates_status_mat: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mfg_job_folder_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eol_mat_avail_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_pur_mat_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_segment1: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_description: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_number: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_description: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    operating_unit_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    region_of_order: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    type_of_order: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hdr_order_type: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hdr_booked_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_tech_ocl_no: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fuel: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pressure: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    special_instructions: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_model: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ordered_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_currency: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    total_unit_value: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_rate: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    total_unit_value_in_inr: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_customer_dely_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_revised_dely_reqd_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_number: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_approved_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_pay: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inco_terms: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    abp_percent: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pgb_percent: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bonus: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ld_applicable: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    penalty: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    insurance_by: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_engineer: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_header_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    proj_specific_llbom: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    llbom_release_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    llbom_pr: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_number: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_value: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_freight: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_recommended_transporter: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_transportation_scope: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_invoice_no: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_invoice_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoiced_value: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contractual_plan_otp: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    delivery_otp: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    original_project_no: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rated_standard_man_hrs: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mfg_commitment_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plan_eol_mech_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plan_eol_ei_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    folder_status: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    regional_commercial: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    actual_fg_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shop_subcontract: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_required: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    suggested_plan_date: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_attribute9: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_en1_revision: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_mfg_revision: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_revision_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})


    # Relations
    calender: Mapped["Calender"] = relationship(back_populates="planmax_headers",
                                                primaryjoin="foreign(func.to_date(PlanMaxHeaders.orig_cust_required_date, 'DD-MM-YY'))==func.to_date(Calender.day_id, 'DD-MM-YY')")

    customers: Mapped["Customers"] = relationship(back_populates="planmax_headers",
                                                  primaryjoin="foreign(PlanMaxHeaders.ship_site_use_id)==Customers.site_use_id")

    di_details: Mapped["DIDetails"] = relationship(back_populates="planmax_headers",
                                                   primaryjoin="and_(foreign(PlanMaxHeaders.sales_order_number)==DIDetails.sales_order_no,"
                                                               "foreign(PlanMaxHeaders.project_number)==DIDetails.xx_project_number)")

    # invoice_headers: Mapped["InvoiceHeaders"] = relationship(back_populates="planmax_headers", primaryjoin="")

    model_xref: Mapped["ModelXref"] = relationship(back_populates="planmax_headers",
                                                   primaryjoin="foreign(PlanMaxHeaders.sos_item)==ModelXref.model_item")

    operating_unit: Mapped["OperatingUnits"] = relationship(back_populates="planmax_headers",
                                                            primaryjoin="foreign(PlanMaxHeaders.operating_unit_id)==OperatingUnits.organization_id")

    order_headers: Mapped["OrderHeaders"] = relationship(back_populates="planmax_headers",
                                                         primaryjoin="foreign(PlanMaxHeaders.sales_order_header_id)==OrderHeaders.header_id")

    order_lines: Mapped["OrderLines"] = relationship(back_populates="planmax_headers",
                                                     primaryjoin="foreign(PlanMaxHeaders.model_line_id)==OrderLines.line_id")

    order_types: Mapped["OrderTypes"] = relationship(back_populates="planmax_headers",
                                                     primaryjoin="foreign(PlanMaxHeaders.order_type_id)==OrderTypes.transaction_type_id")

    organizations: Mapped["Organizations"] = relationship(back_populates="planmax_headers",
                                                          primaryjoin="foreign(PlanMaxHeaders.mfg_organization_id)==Organizations.organization_id")

    planmax_lines: Mapped["PlanMaxLines"] = relationship(back_populates="planmax_headers",
                                                         primaryjoin="and_(foreign(PlanMaxHeaders.sales_order_header_id)==PlanMaxLines.sales_order_header_id,"
                                                                     "foreign(PlanMaxHeaders.model_line_id)==PlanMaxLines.reference_line_id)")

    prn_details: Mapped["PRNDetails"] = relationship(back_populates="planmax_headers",
                                                     primaryjoin="and_(foreign(PlanMaxHeaders.sales_order_header_id)==PRNDetails.so_header_id,"
                                                                 "foreign(PlanMaxHeaders.project_number)==PRNDetails.project_number_so)")

    # project_po_details: Mapped["ProjectPODetails"] = relationship(back_populates="planmax_headers", primaryjoin="")

    tech_ocl_master: Mapped["TechOCLMaster"] = relationship(back_populates="planmax_headers",
                                                            primaryjoin="foreign(PlanMaxHeaders.otm_header_id)==TechOCLMaster.otm_header_id")

    tech_ocl_lines: Mapped["TechOCLLines"] = relationship(back_populates="planmax_headers",
                                                          primaryjoin="foreign(PlanMaxHeaders.otm_header_id)==TechOCLLines.otm_header_id")


"""
operating_unit_id
sales_order_header_id
sales_order_number
model_line_id
model_line_number
order_type_id
group_name
sub_group
product_category
prn_applicable
inspection_required
project_id
project_number
std_nstd
sos_item
mfg_organization_id
orig_cust_required_date
curr_cust_required_date
orig_thx_commitment_date
curr_thx_commitment_date
ho_order_commited_to
ho_order_so_header
ho_order_so_line
oc_no
oc_date
tech_clarity_date
engg_commt_dt
oc_status
oc_closure_date
planned_invoice_dates
planned_invoice_value
wip_folder_release_date
commissioning_date
site_release_date
planner
tca
send_email
fg_month_change_remarks
shell_boiler_appr_auth
reason_for_otp
order_status
interface_status
creation_date
last_update_date
refresh_date
bill_site_use_id
bill_cust_acct_site_id
bill_party_site_id
bill_party_id
bill_location_id
ship_site_use_id
ship_cust_acct_site_id
ship_party_site_id
ship_party_id
ship_location_id
order_intake_status
bom_common_status
reflection_config_status
mat_planning_status
sourcing_status
commit_dates_status_mfg
commit_dates_status_mat
mfg_job_folder_status
prn_status
eol_mat_avail_status
wip_pur_mat_status
project_segment1
project_description
project_task_number
project_task_id
project_task_description
operating_unit_name
region_of_order
type_of_order
hdr_order_type
hdr_booked_date
otm_tech_ocl_no
fuel
pressure
special_instructions
product_model
ordered_date
order_currency
total_unit_value
conversion_rate
total_unit_value_in_inr
prn_customer_dely_date
prn_revised_dely_reqd_date
prn_number
prn_approved_date
freight_pay
inco_terms
abp_percent
pgb_percent
bonus
ld_applicable
penalty
insurance_by
sales_engineer
otm_header_id
project_task_name
proj_specific_llbom
llbom_release_date
llbom_pr
di_number
di_date
di_value
di_freight
di_recommended_transporter
di_transportation_scope
last_invoice_no
last_invoice_date
invoiced_value
contractual_plan_otp
delivery_otp
original_project_no
rated_standard_man_hrs
mfg_commitment_date
plan_eol_mech_date
plan_eol_ei_date
folder_status
regional_commercial
actual_fg_date
shop_subcontract
oc_required
suggested_plan_date
line_attribute9
sos_en1_revision
sos_mfg_revision
sos_revision_date
"""

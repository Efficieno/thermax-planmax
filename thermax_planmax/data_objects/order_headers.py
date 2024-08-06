from typing import TYPE_CHECKING

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class OrderHeaders(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "oe_order_headers_all"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    header_id: Mapped[str] = mapped_column(Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_type_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_number: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    version_number: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expiration_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_source_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_document_type_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_sys_document_ref: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_document_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ordered_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pricing_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipment_priority_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_class_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    price_list_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_exempt_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_exempt_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_exempt_reason_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_rate: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_type_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_rate_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    partial_shipments_allowed: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_tolerance_above: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_tolerance_below: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transactional_curr_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    agreement_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_point_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cust_po_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoicing_rule_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accounting_rule_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    payment_term_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipping_method_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_carrier_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fob_point_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_terms_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_from_org_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_org_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_from_org_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_to_org_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_to_org_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_org_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_contact_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_to_contact_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_to_contact_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_contact_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    context: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute1: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute2: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute3: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute4: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute5: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute6: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute7: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute8: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute9: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute10: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute11: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute12: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute13: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute14: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute15: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute_category: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute1: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute2: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute3: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute4: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute5: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute6: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute7: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute8: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute9: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute10: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute11: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute12: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute13: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute14: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute15: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute16: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute17: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute18: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute19: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute20: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cancelled_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    open_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    booked_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    salesrep_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    return_reason_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_date_type_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    earliest_schedule_limit: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    latest_schedule_limit: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    payment_type_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    payment_amount: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    check_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_holder_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_number: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_expiration_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_approval_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_channel_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    first_ack_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    first_ack_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_ack_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_ack_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_category_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    change_sequence: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    drop_ship_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_payment_term_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipping_instructions: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    packing_instructions: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_context: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute1: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute2: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute3: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute4: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute5: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute6: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute7: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute8: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute9: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute10: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute11: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute12: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute13: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute14: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute15: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    flow_status_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    marketing_source_code_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_approval_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    upgraded_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_preference_set_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    booked_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lock_control: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    price_request_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    batch_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    xml_message_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accounting_rule_duration: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute16: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute17: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute18: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute19: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute20: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    blanket_number: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_document_type_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_phone_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fulfillment_set_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_set_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_fulfillment_set: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transaction_phase_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_document_name: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quote_number: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quote_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    user_status_code: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    draft_submitted_flag: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_document_version_number: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_site_use_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supplier_signature: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supplier_signature_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_signature: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_signature_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    minisite_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_customer_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_customer_contact_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_customer_site_use_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ib_owner: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ib_current_location: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ib_installed_at_location: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_firmed_date: Mapped[str] = mapped_column(Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inst_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    csr_user_id: Mapped[str] = mapped_column(Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cancel_unshipped_lines: Mapped[str] = mapped_column(String, primary_key=False, info={"column_metadata": ColumnMetadata()})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="order_headers",
                                                             primaryjoin="foreign(PlanMaxHeaders.sales_order_header_id)==OrderHeaders.header_id")


"""
header_id
org_id
order_type_id
order_number
version_number
expiration_date
order_source_id
source_document_type_id
orig_sys_document_ref
source_document_id
ordered_date
request_date
pricing_date
shipment_priority_code
demand_class_code
price_list_id
tax_exempt_flag
tax_exempt_number
tax_exempt_reason_code
conversion_rate
conversion_type_code
conversion_rate_date
partial_shipments_allowed
ship_tolerance_above
ship_tolerance_below
transactional_curr_code
agreement_id
tax_point_code
cust_po_number
invoicing_rule_id
accounting_rule_id
payment_term_id
shipping_method_code
freight_carrier_code
fob_point_code
freight_terms_code
sold_from_org_id
sold_to_org_id
ship_from_org_id
ship_to_org_id
invoice_to_org_id
deliver_to_org_id
sold_to_contact_id
ship_to_contact_id
invoice_to_contact_id
deliver_to_contact_id
creation_date
created_by
last_updated_by
last_update_date
last_update_login
program_application_id
program_id
program_update_date
request_id
context
attribute1
attribute2
attribute3
attribute4
attribute5
attribute6
attribute7
attribute8
attribute9
attribute10
attribute11
attribute12
attribute13
attribute14
attribute15
global_attribute_category
global_attribute1
global_attribute2
global_attribute3
global_attribute4
global_attribute5
global_attribute6
global_attribute7
global_attribute8
global_attribute9
global_attribute10
global_attribute11
global_attribute12
global_attribute13
global_attribute14
global_attribute15
global_attribute16
global_attribute17
global_attribute18
global_attribute19
global_attribute20
cancelled_flag
open_flag
booked_flag
salesrep_id
return_reason_code
order_date_type_code
earliest_schedule_limit
latest_schedule_limit
payment_type_code
payment_amount
check_number
credit_card_code
credit_card_holder_name
credit_card_number
credit_card_expiration_date
credit_card_approval_code
sales_channel_code
first_ack_code
first_ack_date
last_ack_code
last_ack_date
order_category_code
change_sequence
drop_ship_flag
customer_payment_term_id
shipping_instructions
packing_instructions
tp_context
tp_attribute1
tp_attribute2
tp_attribute3
tp_attribute4
tp_attribute5
tp_attribute6
tp_attribute7
tp_attribute8
tp_attribute9
tp_attribute10
tp_attribute11
tp_attribute12
tp_attribute13
tp_attribute14
tp_attribute15
flow_status_code
marketing_source_code_id
credit_card_approval_date
upgraded_flag
customer_preference_set_code
booked_date
lock_control
price_request_code
batch_id
xml_message_id
accounting_rule_duration
attribute16
attribute17
attribute18
attribute19
attribute20
blanket_number
sales_document_type_code
sold_to_phone_id
fulfillment_set_name
line_set_name
default_fulfillment_set
transaction_phase_code
sales_document_name
quote_number
quote_date
user_status_code
draft_submitted_flag
source_document_version_number
sold_to_site_use_id
supplier_signature
supplier_signature_date
customer_signature
customer_signature_date
minisite_id
end_customer_id
end_customer_contact_id
end_customer_site_use_id
ib_owner
ib_current_location
ib_installed_at_location
order_firmed_date
inst_id
ib_installed_at_location#1
ib_current_location#1
csr_user_id
cancel_unshipped_lines
"""

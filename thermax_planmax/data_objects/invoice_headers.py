from sqlalchemy.dialects.oracle.types import VARCHAR2, NUMBER, FLOAT, LONG, DATE, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from efficieno.ontology.base import ColumnMetadata, ObjectBase


class InvoiceHeaders(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_inv_dtls"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    trx_number: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    trx_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_currency_code: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    complete_flag: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    batch_source_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    trx_type_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    trx_type_desc: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_type: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_trx_id: Mapped[str] = mapped_column(NUMBER, primary_key=True, info={"column_metadata": ColumnMetadata()})
    invoice_amt: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_to_site_use_id: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})


"""
trx_number
trx_date
invoice_currency_code
complete_flag
batch_source_name
trx_type_name
trx_type_desc
invoice_type
gl_date
customer_trx_id
invoice_amt
bill_to_site_use_id
"""
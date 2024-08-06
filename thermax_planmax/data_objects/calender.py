from typing import TYPE_CHECKING
from sqlalchemy.dialects.oracle.types import VARCHAR2, NUMBER, FLOAT, LONG, DATE, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.ontology.base import ColumnMetadata, ObjectBase

if TYPE_CHECKING:
    from thermax_planmax.data_objects.planmax_headers import PlanMaxHeaders


class Calender(ObjectBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_calender"
    __table_args__ = {"schema": "apps", "extend_existing": True}

    day_id: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    num_days_in_day: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_end_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_num_of_week: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_num_of_month: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_number_in_year: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_number_in_month: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_number_in_week: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_id: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_time_span: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_end_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_number_in_year: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_id: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_short_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_time_span: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_end_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_number_in_year: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    year_id: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    year_name: Mapped[str] = mapped_column(VARCHAR2, primary_key=False, info={"column_metadata": ColumnMetadata()})
    num_days_in_year: Mapped[str] = mapped_column(NUMBER, primary_key=False, info={"column_metadata": ColumnMetadata()})
    year_end_date: Mapped[str] = mapped_column(DATE, primary_key=False, info={"column_metadata": ColumnMetadata()})

    planmax_headers: Mapped["PlanMaxHeaders"] = relationship(back_populates="calender",
                                                             primaryjoin="foreign(func.to_date(PlanMaxHeaders.orig_cust_required_date, 'DD-MM-YY'))==func.to_date(Calender.day_id, 'DD-MM-YY')")


"""
day_id
day_name
num_days_in_day
day_end_date
day_num_of_week
day_num_of_month
day_number_in_year
day_number_in_month
day_number_in_week
month_id
month_name
month_time_span
month_end_date
month_number_in_year
quarter_id
quarter_short_name
quarter_name
quarter_time_span
quarter_end_date
quarter_number_in_year
year_id
year_name
num_days_in_year
year_end_date
"""

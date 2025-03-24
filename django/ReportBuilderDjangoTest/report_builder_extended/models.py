from django.db import models
from report_builder.models import Report, FilterField
from ReportBuilderDjangoTest.models import BaseModel

# Create your models here.
class ReportExtendedModel(Report, BaseModel):
    """
    ReportExtendedModel for Extra columns in Report model from
    report_builder.models.
    """

    class Meta:
        """Meta information about ReportOverrideModel."""

        db_table = 'report_builder_extended_report_extended'


class FilterFieldExtendedModel(FilterField, BaseModel):
    """
    FilterFieldExtendedModel for Extra columns in FilterField model from
    report_builder.models.
    """

    class Meta:
        """Meta information about ReportOverrideModel."""

        db_table = 'report_builder_extended_filter_field_extended'
from typing import Optional, Dict
from pydantic import BaseModel, Field, ConfigDict


class Report(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: Optional[str] = None


class ReportFactory:
    def __init__(self):
        self.report_types = dict()

    def register_report_type(self, db_type):
        def decorator(fn):
            self.report_types[db_type] = fn
            return fn

        return decorator

    def create_report(self, config: Dict) -> Report:
        return Report(**config)


class EmailReportFactory(ReportFactory):
    subject: str
    to_address: str
    from_address: str


#
#
# class SlackReport(Report):
#     channel_name: str
#
#
# class ReportFactory:
#     @staticmethod
#     def create_report(report: Report) -> Report:
#         return Report()

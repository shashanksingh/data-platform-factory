from pydantic import BaseModel, Field


class Report(BaseModel):
    source: str


class EmailReport(Report):
    subject: str
    to_address: str
    from_address: str


class SlackReport(Report):
    channel_name: str


class ReportFactory:
    @staticmethod
    def create_report(report: Report) -> Report:
        return Report()

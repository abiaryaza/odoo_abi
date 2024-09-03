from odoo import api, fields, models, _


class HMSPatient(models.Model):
    _inherit = "hms.patient"
    health_description = fields.Text(string='Health Description')

    def print_report(self):
        return self.env.ref('om_hospital.report1_appointment_details').report_action(self)

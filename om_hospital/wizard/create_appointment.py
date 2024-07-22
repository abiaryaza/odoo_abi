from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CreateAppointmentWiz(models.TransientModel):
    _name = "create.appointment.wizard"
    # _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='date Appointment', required=True, tracking=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient')

    def action_create_appointment(self):
        print("Button Is Clicked")
        vals = {
            # saat memanggil model 'many to one', harus memanggil .id nya, seperti dibawah ini
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        print("appointment id: ", appointment_rec.id)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            'target': 'new'

        }

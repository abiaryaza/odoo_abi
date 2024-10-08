from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CreateAppointmentWiz(models.TransientModel):
    _name = "create.appointment.wizard"
    # _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='date Appointment', required=False, tracking=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

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
            # target=new artinya wizard tertutup dan form terbuka berbentuk pop-up
            # 'target': 'new'
        }

    def action_view_appointment(self):
        # metode 1
        # action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action
        #metode 2
        # action = self.env["ir.actions.actions"]._for_xml_id('om_hospital.action_hospital_appointment')
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action
        # metode 3
        # action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return {
            'name': 'Appointments',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'target': 'current',
        }

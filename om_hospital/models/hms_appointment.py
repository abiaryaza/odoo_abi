from odoo import api, fields, models, _


class HMSAppointments(models.Model):
    _inherit = ["hms.appointment"]
    health_desc = fields.Text(string='HealthDesc',related='patient_id.health_description', readonly=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',
                              related='patient_id.gender', tracking=True)
    street = fields.Char(string='street',related='patient_id.street', readonly=True)
    city = fields.Char(string='city', related='patient_id.city', readonly=True)
    state_id = fields.Many2one('res.country.state', string='state_id', related='patient_id.state_id', readonly=True)
    zip = fields.Char(string='zip', related='patient_id.zip', readonly=True)
    country_id = fields.Many2one('res.country', string='country_id', related='patient_id.country_id', readonly=True)
    occupation = fields.Many2one('hms.patient.occupation', string='country_id', related='patient_id.occupation', readonly=True)
    sip = fields.Char(string='sip', related='physician_id.sip', readonly=True)
    physician_phone = fields.Char(string='physician_phone', related='physician_id.phone', readonly=True)
    physician_email = fields.Char(string='physician_email', related='physician_id.email', readonly=True)
    physician_street = fields.Char(string='physician_street', related='physician_id.street', readonly=True)
    physician_city = fields.Char(string='physician_city', related='physician_id.city', readonly=True)
    physician_state_id = fields.Many2one('res.country.state', string='physician_state_id', related='physician_id.state_id', readonly=True)
    physician_zip = fields.Char(string='physician_zip', related='physician_id.zip', readonly=True)
    signature = fields.Binary(string='Tanda Tangan', related='physician_id.signature', readonly=True)
    # date_created_report = fields.Date(string="Date", related='create_date', readonly=True)



    def print_report(self):
        return self.env.ref('om_hospital.report1_appointment_details').report_action(self)
    # READONLY_STATES = {'cancel': [('readonly', True)], 'done': [('readonly', True)]}
    # patient_id = fields.Many2one('hms.patient', ondelete='restrict', string='Pasien',
    #                              required=True, index=True, help='Patient Name', states=READONLY_STATES, tracking=True)

    def suratsakit(self):
        print('res....................................')
        return self.env.ref('om_hospital.action_create_surat_sakit_form')

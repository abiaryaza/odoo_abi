from odoo import api, fields, models, _

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"

    name = fields.Char(string="Order Reference", default=lambda self: _('New'), required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    # di variabel age ada 'related' buat ngambil data secara otomatis dari variabel di model lain
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',
                              tracking=True, related='patient_id.gender')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status")
    note = fields.Text(string="Notes", tracking=True)
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up")

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        return super(HospitalAppointment, self).create(vals)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.notes:
                self.note = self.patient_id.notes

        else:
            self.gender = ''
            self.note = ''

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'
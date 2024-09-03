from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Patient Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string='Is child?', tracking=True)
    notes = fields.Text(string="Notes", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',
                              tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
    ref = fields.Char(string="reference", default=lambda self: _('New'))
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    tag_ids = fields.Many2many('res.partner.category', 'hospital_patient_tag_rel', 'patient_id', 'tag_id',
                               string='Tags')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status")
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    image = fields.Binary(string="Patient Image")

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = rec.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    @api.constrains('is_child', 'age')
    def check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded!"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    # membuat 'default' pada sebuah model diluar atribut modelnya. Bisa melakukan override
    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        print('res....................................', res)
        res['age'] = 50
        res['notes'] = 'test default get method'
        return res

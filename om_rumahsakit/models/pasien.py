from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPasien(models.Model):
    _name = "hospital.pasien"
    _inherit = ["hospital.patient"]
    _description = "Rekaman Pasien"

    tag_ids = fields.Many2many('res.partner.category', 'hospital_pasien_tag_rel', 'pasien_id', 'tag_id',
                               string='Tags')

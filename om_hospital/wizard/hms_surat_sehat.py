from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CreateSuratSehatWiz(models.TransientModel):
    _name = "create.suratsehat.wizard"
    # _inherit = ["hms.appointment"]
    _description = "Create SuratSehat Wizard"

    patient_id = fields.Many2one('hms.patient', ondelete="restrict", string='Pasien', required=True, tracking=True)
    name = fields.Char(string='Jenis Kunjungan', required=True, translate=True)
    # sick_day = fields.Integer(string='Lama Sehat', tracking=True, required=True)
    needed = fields.Char(string='Keperluan', required=True, tracking=True)

    @api.model
    def default_get(self, fields):
        # self.state = 'confirm'
        result = super(CreateSuratSehatWiz, self).default_get(fields)
        patient_id = self.env['hms.appointment'].browse(self._context['active_id'])
        print(patient_id)
        result['name'] = patient_id.name
        print(result['name'])
        result['patient_id'] = patient_id.patient_id.id
        print(result['patient_id'])
        # result['active_id'] = patient_id.id
        # print(result['active_id'])
        return result

    def action_create_suratsehat(self):
        domain = []
        patient_id = self.read()[0].get('patient_id')
        print(patient_id[0])
        # domain += [('patient_id', '=', patient_id[0])]
        name = self.read()[0].get('name')
        print(name)
        domain += [('name','=',name)]
        # active_id = self.read()[0].get('active_id')
        # print(active_id)
        # domain += [('id', '=', id)]
        print("Button Is Clicked", self.read()[0])
        appointments = self.env["hms.appointment"].search_read(domain)
        print("appointments", appointments)
        data = {
            'form_data': self.read()[0],
            # 'appointments': appointments
        }
        print(data['form_data']['name'])
        return self.env.ref('om_hospital.surat_sehat_templates').report_action(self, data=data)
        # return self.env.ref('om_hospital.surat_sehat_templates').report_action(self, data=data)

class CreateSuratSehatWizReportVal(models.AbstractModel):
    _name ='report.om_hospital.surat_sehat_template'
    def _get_report_values(self, docids, data=None):
        print('resss......................')
        domain = []
        if data['form_data']['name']:
            domain += [('name', '=', data['form_data']['name'])]
        docs = self.env["hms.appointment"].search(domain)
        # name = self.env["hms.appointment"].browse(data['form_data']['id'])
        # active_id = self.env['hms.appointment'].browse(self._context['active_id'])
        # print(active_id)
        # data.update({'name': active_id})
        # print(data)
        # print(docs)
        return {
            'doc_ids': docs.ids,
            'doc_model': "hms.appointment",
            'docs': docs,
            'datas': data
        }



    # def action_view_appointment(self):
    #     # metode 1
    #     # action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
    #     # action['domain'] = [('patient_id', '=', self.patient_id.id)]
    #     # return action
    #     #metode 2
    #     # action = self.env["ir.actions.actions"]._for_xml_id('om_hospital.action_hospital_appointment')
    #     # action['domain'] = [('patient_id', '=', self.patient_id.id)]
    #     # return action
    #     # metode 3
    #     # action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
    #     # action['domain'] = [('patient_id', '=', self.patient_id.id)]
    #     return {
    #         'name': 'Appointments',
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'tree,form',
    #         'domain': [('patient_id', '=', self.patient_id.id)],
    #         'view_type': 'form',
    #         'res_model': 'hospital.appointment',
    #         'target': 'current',
    #     }

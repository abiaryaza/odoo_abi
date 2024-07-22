from odoo import models

class PatientCardXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_id_card_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        # mengiterasi setiap pasien
        for obj in patients:
            report_name = obj.name
            # Membuat satu sheet setiap pasien
            sheet = workbook.add_worksheet(report_name[:31])
            # Membuat nama menjadi bold
            bold = workbook.add_format({'bold': True})
            # Menentukan posisi penulisan nama
            sheet.write(0, 0, obj.name, bold)

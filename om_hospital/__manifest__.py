{
    'name': 'Hospital Management System',
    'author': 'Odoo Mates',
    'website': 'www.odoomates.tech',
    'summary': 'odoo 16 Development',
    'depends': ['mail', 'sale', 'report_xlsx'],
# 'assets': {
#     'web.assets_backend': [
#         'dev/om_hospital/static/src/css/appointment_style.css',
#     ]},
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'wizard/create_appointment_view.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/kid.xml',
        'views/patient_gender.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/sale.xml',
        'report/report.xml',
        'report/patient_card.xml',
        'report/patient_card_2.xml',
        'report/appointment_details.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,

}

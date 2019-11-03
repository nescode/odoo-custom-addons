# -*- coding: utf-8 -*-
{
    'name': 'Open PDF Reports and PDF Attachments in Browser',
    'version': '13.0.1.0',
    'summary': """Open PDF Reports and PDF Attachments in Browser""",
    'author': 'Ivan Sokolov, Cetmix',
    'category': 'Productivity',
    'license': 'GPL-3',
    'website': 'https://demo.cetmix.com',
    'live_test_url': 'https://demo.cetmix.com',
    'description': """
    Preview reports and pdf attachments in browser instead of downloading them.
    Open Report or PDF Attachment in new tab instead of downloading.              
""",
    'depends': ['base', 'web'],
    'images': ['static/description/banner.png'],
    'data': [
        'views/cetmix_report_preview_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

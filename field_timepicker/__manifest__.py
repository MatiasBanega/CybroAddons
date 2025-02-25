# -*- coding: utf-8 -*-
# #############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Mruthul Raj(<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Field Time Picker',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Time Picker Using Wickedpicker',
    'description': 'The Field Time Picker is a module that provides a time '
                   'picker widget designed for character fields in a web'
                   ' application. It leverages the Wickedpicker library to'
                   ' offer a user-friendly and intuitive way to select time '
                   'values.',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com/',
    'depends': ['base'],
    "assets": {
        'web.assets_backend': [
            'field_timepicker/static/wickedpicker/dist/wickedpicker.min.css',
            'field_timepicker/static/wickedpicker/dist/wickedpicker.min.js',
            'field_timepicker/static/src/js/time_widget.js',
        ],
        'web.assets_qweb': [
            'field_timepicker/static/src/xml/timepicker.xml',
        ]
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

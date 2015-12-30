# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2014-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp.osv import fields, osv


'''New class to handle sales commission configuration.'''
class cus_registration(osv.osv):
    _name = 'cus.registration'
    _columns = {
        

	'name' : fields.char("Name",size =16),
	'contno': fields.integer("Contact No"),
	'age'  : fields.integer("Age"),
	'dob': fields.date("Birthdate"),
	'Registrationdate': fields.datetime("Registration date"),
	'Registrationfee': fields.float("Registration Fee"),
	'state': fields.selection([('Draft','draft'),('Cancel','cancel'),('pending','Pending'),('registerd','Registerd')], string='status'),
	'gender' : fields.selection([('male','Male'),('female','Female')],"Gender"),
    'add':fields.many2one('res.partner','Address'),
	
    }

    _defaults={
        'active':True,
	'status':'draft',
	    }


# coding=utf-8

from ..routes import robot
from openerp.http import request

@robot.text
def input_handle(message, session):
    content = message.content.lower()
    serviceid = message.target
    openid = message.source
    
    rs = request.registry['wx.autoreply'].search([])
    for rc in rs:
        if rc.type==1:
            if content==rc.key:
                return rc.action.content
    
    if content.startswith('e'):
        return content
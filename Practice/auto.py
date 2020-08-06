'''
Created on Jun 27, 2020

@author: Sumit
'''
# def set_password(username, password):
#     from pyad import pyad
#     ads_obj = pyad.("WinNT://localhost/%s,user" % username)
#     ads_obj.Getinfo()
#     ads_obj.SetPassword(password)
# 
# 
# def verify_success(username, password):
#     from win32security import LogonUser
#     from win32con import LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT
#     try:
#         LogonUser(username, None, password, LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT)
#     except:
#         return False
#     return True
# 
# u = "Sumit"
# p = "google123456"
# set_password(u, p)
# if verify_success(u, p):
#     print ("W00t it workz")
# else:
#     print ("Continue Googling")

from pyad import *

pyad.set_defaults(ldap_server="a.b.c.d", username="Sumit", password="google@123456")

ou = pyad.adcontainer.ADContainer.from_dn("ou=All_Users, dc=LIFEALIKE, dc=LAB")
new_user = pyad.aduser.ADUser.create("Sumit", ou, password="google123456")





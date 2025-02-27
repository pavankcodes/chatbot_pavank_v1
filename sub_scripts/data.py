from mechanisms import db_access as dba
usrs= dba.get_usrs()
settings= dba.get_settings()
class login_app_data:
    uid=0
    currUser,usr_data_old ='','yes'
    data,title='','Login'
    geometry='{}x{}'.format(500,650)
    mode,theme=settings['mode'],settings['theme']
    auths,status = usrs,'out'
inst_txt=[
    'from now on i will call you neo.','when i ask who you are, respond as neo',
    'you are neo, a personal general purpose assistant, coded by Mr Pavan Kumar.',
    'Pavan Kumar made you (neo) as a cbse class 12th project in aps sp marg.',
    ]
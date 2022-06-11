import requests

#Chave API da OpenWeather
API_KEY = '8fb3a13b9320f9ee1d14bc7165c117c9'

country_code = 'ISO 3166-2:CV' # Codigo de país de Cabo Verde no padrão ISO 3166

#Informação das cidades
# Ribeira Grande -> 17.183333, -25.066667
lat_rg = 17.183333
lon_rg = -25.066667

rg = {'lat': 17.183333,'lon': -25.066667}

# Ponta do Sol -> 17.2, -25.083333
lat_ps = 17.2
lon_ps = -25.083333

# Porto Novo -> 17.016667, -25.066667
lat_pn = 17.016667
lon_pn = -25.066667

# Paul -> 17.133333, -25.016667
lat_pa = 17.148696
lon_pa = -25.015448

# Mindelo -> 16.883333, -24.983333
lat_min = 16.883333
lon_min = -24.983333

# Santa Luzia -> 16.749831, -24.717861
lat_slu = 16.749831
lon_slu = -24.717861

# Ribeira Brava São Nicolau -> 16.616672, -24.292025
lat_rb = 16.616672
lon_rb = -24.292025

# Tarrafal São Nicolau -> 16.563508, -24.356690
lat_tsn = 16.563508
lon_tsn = -24.356690

# Espargos -> 16.755341, -22.940869
lat_esp = 16.755341
lon_esp = -22.940869

# Sta Maria -> 16.601914, -22.907083
lat_sm = 16.601914
lon_sm = -22.907083

# Sal Rei -> 16.178487, -22.915784
lat_sr = 16.178487
lon_sr = -22.915784

# Ilha do Maio 15.138741, -23.205187
lat_mai = 15.138741
lon_mai = -23.205187

#Praia -> 14.915721, -23.506532
lat_pr = 14.915721
lon_pr = -23.506532

#São Domingos -> 15.027653, -23560699
lat_sd = 15.027653
lon_sd = -23.560699

#Sta Catarina de Santiago -> 15.100212, -23.670124
lat_scst = 15.100212
lon_scst = -23.670124

#São Salvador do Mundo -> 15.093484, -23.636444
lat_ssm = 15.093484
lon_ssm = -23.636444

#Sta Cruz -> 15.134690, -23.534462
lat_scr = 15.134690
lon_scr = -23.534462

#São Lourenço dos Órgãos -> 15.068217, -23.580960
lat_slo = 15.068217
lon_slo = -23.580960

#Ribeira Grande de Santiago -> 14.917396, -23.607687
lat_rgst = 14.917396
lon_rgst = -23.607687

#São Miguel -> 15.194564, -23.644760
lat_smi = 15.194564
lon_smi = -23.644760

#Tarrafal de Santiago -> 15.277276, -23.749527
lat_tst = 15.277276
lon_tst = -23.749527

#São Filipe -> 14.897820, -24.494328
lat_sf = 14.897820
lon_sf = -24.494328

#Santa Catarina -> 14.925914, -24.318882
lat_scfg = 14.925914
lon_scfg = -24.318882

#Mosteiros -> 15.035340, -24.326414
lat_mo = 15.035340
lon_mo = -24.326414

# Brava 14.870705, -24.696822
lat_br = 14.870705
lon_br = -24.696822

#FUNÇÃO QUE RETORNA O CLIMA DE CADA CIDADE

def ribeira_grande():
    link_rg = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_rg}&lon={lon_rg}&appid={API_KEY}&lang=pt&'
    requisicao_rg = requests.get(link_rg)
    requisicao_dic_rg = requisicao_rg.json()
    descricao_rg = requisicao_dic_rg['weather'][0]['description']
    temperatura_rg = requisicao_dic_rg['main']['temp'] - 272.15
    RIBEIRA_GRANDE = (f'Clima em Ribeira Grande: {descricao_rg}, Temperatura em Ribeira Grande: {"%.0f" % temperatura_rg}ºC')
    return RIBEIRA_GRANDE

def ponta_do_sol():
    link_ps = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_ps}&lon={lon_ps}&appid={API_KEY}&lang=pt&'
    requisicao_ps = requests.get(link_ps)
    requisicao_dic_ps = requisicao_ps.json()
    descricao_ps = requisicao_dic_ps['weather'][0]['description']
    temperatura_ps = requisicao_dic_ps['main']['temp'] - 272.15
    PONTA_DO_SOL = f'Clima em Ponta do Sol: {descricao_ps}, Temperatura em Ponta do Sol: {"%.0f" % temperatura_ps}ºC'
    return PONTA_DO_SOL

def porto_novo():
    link_pn = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_pn}&lon={lon_pn}&appid={API_KEY}&lang=pt&'
    requisicao_pn = requests.get(link_pn)
    requisicao_dic_pn = requisicao_pn.json()
    descricao_pn = requisicao_dic_pn['weather'][0]['description']
    temperatura_pn = requisicao_dic_pn['main']['temp'] - 272.15
    PORTO_NOVO = f'Clima em Porto Novo: {descricao_pn}, Temperatura em Porto Novo: {"%.0f" % temperatura_pn}ºC'
    return PORTO_NOVO

def paul():
    link_pa = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_pa}&lon={lon_pa}&appid={API_KEY}&lang=pt&'
    requisicao_pa = requests.get(link_pa)
    requisicao_dic_pa = requisicao_pa.json()
    descricao_pa = requisicao_dic_pa['weather'][0]['description']
    temperatura_pa = requisicao_dic_pa['main']['temp'] - 272.15
    PAUL = f'Clima em Paúl: {descricao_pa}, Temperatura em Paúl: {"%.0f" % temperatura_pa}ºC'
    return PAUL

def mindelo():
    link_min = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_min}&lon={lon_min}&appid={API_KEY}&lang=pt&'
    requisicao_min = requests.get(link_min)
    requisicao_dic_min = requisicao_min.json()
    descricao_min = requisicao_dic_min['weather'][0]['description']
    temperatura_min = requisicao_dic_min['main']['temp'] - 272.15
    MINDELO = f'Clima em Mindelo: {descricao_min}, Temperatura em Mindelo: {"%.0f" % temperatura_min}ºC'
    return MINDELO

def santa_luzia():
    link_slu = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_slu}&lon={lon_slu}&appid={API_KEY}&lang=pt&'
    requisicao_slu = requests.get(link_slu)
    requisicao_dic_slu = requisicao_slu.json()
    descricao_slu = requisicao_dic_slu['weather'][0]['description']
    temperatura_slu = requisicao_dic_slu['main']['temp'] - 272.15
    SANTA_LUZIA = f'Clima em Santa Luzia: {descricao_slu}, Temperatura em Santa Luzia: {"%.0f" % temperatura_slu}ºC'
    return SANTA_LUZIA

def ribeira_brava():
    link_rb = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_rb}&lon={lon_rb}&appid={API_KEY}&lang=pt&'
    requisicao_rb = requests.get(link_rb)
    requisicao_dic_rb = requisicao_rb.json()
    descricao_rb = requisicao_dic_rb['weather'][0]['description']
    temperatura_rb = requisicao_dic_rb['main']['temp'] - 272.15
    RIBEIRA_BRAVA = f'Clima em Ribeira Brava de São Nicolau: {descricao_rb}, Temperatura em Ribeira Brava de São Nicolau: {"%.0f" % temperatura_rb}ºC'
    return RIBEIRA_BRAVA

def tarrafal_sao_nicolau():
    link_tsn = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_tsn}&lon={lon_tsn}&appid={API_KEY}&lang=pt&'
    requisicao_tsn = requests.get(link_tsn)
    requisicao_dic_tsn = requisicao_tsn.json()
    descricao_tsn = requisicao_dic_tsn['weather'][0]['description']
    temperatura_tsn = requisicao_dic_tsn['main']['temp'] - 272.15
    TARRAFAL_SAO_NICOLAU = f'Clima em Tarrafal de São Nicolau: {descricao_tsn}, Temperatura em Tarrafal de São Nicolau: {"%.0f" % temperatura_tsn}ºC'
    return TARRAFAL_SAO_NICOLAU

def espargos():
    link_esp = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_esp}&lon={lon_esp}&appid={API_KEY}&lang=pt&'
    requisicao_esp = requests.get(link_esp)
    requisicao_dic_esp = requisicao_esp.json()
    descricao_esp = requisicao_dic_esp['weather'][0]['description']
    temperatura_esp = requisicao_dic_esp['main']['temp'] - 272.15
    ESPARGOS = f'Clima em Espargos: {descricao_esp}, Temperatura em Espargos: {"%.0f" % temperatura_esp}ºC'
    return ESPARGOS

def santa_maria():
    link_sm = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_sm}&lon={lon_sm}&appid={API_KEY}&lang=pt&'
    requisicao_sm = requests.get(link_sm)
    requisicao_dic_sm = requisicao_sm.json()
    descricao_sm = requisicao_dic_sm['weather'][0]['description']
    temperatura_sm = requisicao_dic_sm['main']['temp'] - 272.15
    SANTA_MARIA = f'Clima em Santa Maria: {descricao_sm}, Temperatura em Santa Maria: {"%.0f" % temperatura_sm}ºC'
    return SANTA_MARIA

def sal_rei():
    link_sr = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_sr}&lon={lon_sr}&appid={API_KEY}&lang=pt&'
    requisicao_sr = requests.get(link_sr)
    requisicao_dic_sr = requisicao_sr.json()
    descricao_sr = requisicao_dic_sr['weather'][0]['description']
    temperatura_sr = requisicao_dic_sr['main']['temp'] - 272.15
    SAL_REI = f'Clima em Sal Rei: {descricao_sr}, Temperatura em Sal Rei: {"%.0f" % temperatura_sr}ºC'
    return SAL_REI

def maio():
    link_mai = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_mai}&lon={lon_mai}&appid={API_KEY}&lang=pt&'
    requisicao_mai = requests.get(link_mai)
    requisicao_dic_mai = requisicao_mai.json()
    descricao_mai = requisicao_dic_mai['weather'][0]['description']
    temperatura_mai = requisicao_dic_mai['main']['temp'] - 272.15
    MAIO = f'Clima em Maio: {descricao_mai}, Temperatura em Maio: {"%.0f" % temperatura_mai}ºC'
    return MAIO

def praia():
    link_pr = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_pr}&lon={lon_pr}&appid={API_KEY}&lang=pt&'
    requisicao_pr = requests.get(link_pr)
    requisicao_dic_pr = requisicao_pr.json()
    descricao_pr = requisicao_dic_pr['weather'][0]['description']
    temperatura_pr = requisicao_dic_pr['main']['temp'] - 272.15
    PRAIA = f'Clima em Praia: {descricao_pr}, Temperatura em Praia: {"%.0f" % temperatura_pr}ºC'
    return PRAIA

def sao_domingos():
    link_sd = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_sd}&lon={lon_sd}&appid={API_KEY}&lang=pt&'
    requisicao_sd = requests.get(link_sd)
    requisicao_dic_sd = requisicao_sd.json()
    descricao_sd = requisicao_dic_sd['weather'][0]['description']
    temperatura_sd = requisicao_dic_sd['main']['temp'] - 272.15
    SAO_DOMINGOS = f'Clima em São Domingos: {descricao_sd}, Temperatura em São Domingos: {"%.0f" % temperatura_sd}ºC'
    return SAO_DOMINGOS

def santa_catarina_st():
    link_scst = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_scst}&lon={lon_scst}&appid={API_KEY}&lang=pt&'
    requisicao_scst = requests.get(link_scst)
    requisicao_dic_scst = requisicao_scst.json()
    descricao_scst = requisicao_dic_scst['weather'][0]['description']
    temperatura_scst = requisicao_dic_scst['main']['temp'] - 272.15
    SANTA_CATARINA_ST = f'Clima em Santa Catarina de Santiago: {descricao_scst}, Temperatura em Santa Catarina de Santiago: {"%.0f" % temperatura_scst}ºC'
    return SANTA_CATARINA_ST

def sao_salvador():
    link_ssm = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_ssm}&lon={lon_ssm}&appid={API_KEY}&lang=pt&'
    requisicao_ssm = requests.get(link_ssm)
    requisicao_dic_ssm = requisicao_ssm.json()
    descricao_ssm = requisicao_dic_ssm['weather'][0]['description']
    temperatura_ssm = requisicao_dic_ssm['main']['temp'] - 272.15
    SAO_SALVADOR_DO_MUNDO = f'Clima em São Salvador do Mundo: {descricao_ssm}, Temperatura em São Salvador do Mundo: {"%.0f" % temperatura_ssm}ºC'
    return SAO_SALVADOR_DO_MUNDO

def santa_cruz():
    link_scr = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_scr}&lon={lon_scr}&appid={API_KEY}&lang=pt&'
    requisicao_scr = requests.get(link_scr)
    requisicao_dic_scr = requisicao_scr.json()
    descricao_scr = requisicao_dic_scr['weather'][0]['description']
    temperatura_scr = requisicao_dic_scr['main']['temp'] - 272.15
    SANTA_CRUZ = f'Clima em Santa Cruz: {descricao_scr}, Temperatura em Santa Cruz: {"%.0f" % temperatura_scr}ºC'
    return SANTA_CRUZ

def sao_lourenço():
    link_slo = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_slo}&lon={lon_slo}&appid={API_KEY}&lang=pt&'
    requisicao_slo = requests.get(link_slo)
    requisicao_dic_slo = requisicao_slo.json()
    descricao_slo = requisicao_dic_slo['weather'][0]['description']
    temperatura_slo = requisicao_dic_slo['main']['temp'] - 272.15
    SAO_LOURENCO = f'Clima em São Lourenço: {descricao_slo}, Temperatura em São Lourenço: {"%.0f" % temperatura_slo}ºC'
    return SAO_LOURENCO

def ribeira_grande_st():
    link_rgst = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_rgst}&lon={lon_rgst}&appid={API_KEY}&lang=pt&'
    requisicao_rgst = requests.get(link_rgst)
    requisicao_dic_rgst = requisicao_rgst.json()
    descricao_rgst = requisicao_dic_rgst['weather'][0]['description']
    temperatura_rgst = requisicao_dic_rgst['main']['temp'] - 272.15
    RIBEIRA_GRANDE_ST = f'Clima em Ribeira Grande de Santiago: {descricao_rgst}, Temperatura em Ribeira Grande de Santiago: {"%.0f" % temperatura_rgst}ºC'
    return RIBEIRA_GRANDE_ST

def sao_miguel():
    link_smi = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_smi}&lon={lon_smi}&appid={API_KEY}&lang=pt&'
    requisicao_smi = requests.get(link_smi)
    requisicao_dic_smi = requisicao_smi.json()
    descricao_smi = requisicao_dic_smi['weather'][0]['description']
    temperatura_smi = requisicao_dic_smi['main']['temp'] - 272.15
    SAO_MIGUEL = f'Clima em São Miguel: {descricao_smi}, Temperatura em São Miguel: {"%.0f" % temperatura_smi}ºC'
    return SAO_MIGUEL

def tarrafal_st():
    link_tst = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_tst}&lon={lon_tst}&appid={API_KEY}&lang=pt&'
    requisicao_tst = requests.get(link_tst)
    requisicao_dic_tst = requisicao_tst.json()
    descricao_tst = requisicao_dic_tst['weather'][0]['description']
    temperatura_tst = requisicao_dic_tst['main']['temp'] - 272.15
    TARRAFAL_ST = f'Clima em Tarrafal de Santiago: {descricao_tst}, Temperatura em Tarrafal de Santiago: {"%.0f" % temperatura_tst}ºC'
    return TARRAFAL_ST

def sao_filipe():
    link_sf = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_sf}&lon={lon_sf}&appid={API_KEY}&lang=pt&'
    requisicao_sf = requests.get(link_sf)
    requisicao_dic_sf = requisicao_sf.json()
    descricao_sf = requisicao_dic_sf['weather'][0]['description']
    temperatura_sf = requisicao_dic_sf['main']['temp'] - 272.15
    SAO_FILIPE = f'Clima em São Filipe: {descricao_sf}, Temperatura em São Filipe: {"%.0f" % temperatura_sf}ºC'
    return SAO_FILIPE

def santa_catarina_fg():
    link_scfg = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_scfg}&lon={lon_scfg}&appid={API_KEY}&lang=pt&'
    requisicao_scfg = requests.get(link_scfg)
    requisicao_dic_scfg = requisicao_scfg.json()
    descricao_scfg = requisicao_dic_scfg['weather'][0]['description']
    temperatura_scfg = requisicao_dic_scfg['main']['temp'] - 272.15
    SANTA_CATARINA_FG = f'Clima em Santa Catarina do Fogo: {descricao_scfg}, Temperatura em Santa Catarina do Fogo: {"%.0f" % temperatura_scfg}ºC'
    return SANTA_CATARINA_FG

def mosteiros():
    link_mo = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_mo}&lon={lon_mo}&appid={API_KEY}&lang=pt&'
    requisicao_mo = requests.get(link_mo)
    requisicao_dic_mo = requisicao_mo.json()
    descricao_mo = requisicao_dic_mo['weather'][0]['description']
    temperatura_mo = requisicao_dic_mo['main']['temp'] - 272.15
    MOSTEIROS = f'Clima em Mosteiros: {descricao_mo}, Temperatura em Mosteiros: {"%.0f" % temperatura_mo}ºC'
    return MOSTEIROS

def brava():
    link_br = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_br}&lon={lon_br}&appid={API_KEY}&lang=pt&'
    requisicao_br = requests.get(link_br)
    requisicao_dic_br = requisicao_br.json()
    descricao_br = requisicao_dic_br['weather'][0]['description']
    temperatura_br = requisicao_dic_br['main']['temp'] - 272.15
    BRAVA = f'Clima em Brava: {descricao_br}, Temperatura em Brava: {"%.0f" % temperatura_br}ºC'
    return BRAVA


import streamlit as st
from bs4 import BeautifulSoup
import requests
import clima
import re

url = "https://cvcifra.blogspot.com/"
link_info_rg = 'https://www.google.com/search?q=ribeira+grande+de+santo+ant%C3%A3o&rlz=1C1GCEU_pt-BRCV920CV920&oq=ribeira+grande+de+santo+ant%C3%A3o&aqs=chrome..69i57j0i22i30l3j69i60.6861j0j7&sourceid=chrome&ie=UTF-8'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}

info = requests.get(url, headers=headers)
tags = BeautifulSoup(info.text, "html.parser")
a = tags.find_all(class_='widget-content list-label-widget-content') # class_='widget-content list-label-widget-content'
#print(a[0])

info_rg = requests.get(link_info_rg, headers=headers)
tags_rg = BeautifulSoup(info_rg.text, "html.parser")
desc_rg = tags_rg.find_all('span')
print(desc_rg[0])

# LISTA COM AS CIDADES
cidades = ['Ribeira Grande', 'Ponta do Sol', 'Paul', 'Porto Novo', 'Mindelo', 'Santa Luzia', 'Ribeira Brava',
           'Tarrafal de São Nicolau', 'Espargos', 'Santa Maria', 'Sal Rei', 'Maio', 'Praia', 'São Domingos', 'Santa Catarina de Santiago',
           'São Salvador do Mundo', 'Santa Cruz', 'São Lourenço dos Órgãos', 'Ribeira Grande ST', 'São Miguel', 'Tarrafal',
           'São Filipe', 'Santa Catarina', 'Mosteiros', 'Brava']

#Titulo
st.sidebar.title("CABO INFO")
st.title("CABO INFO")

#Descrição
st.write("CABO INFO - Onde você encontra tudo o que precisa saber sobre Cabo Verde")

#Escolha no SideBar. Depois deve ser feita em formato de pagina
pagina = st.sidebar.selectbox("Escolha o que quer ver:", ['Governo', 'Ilhas', 'Cidades', 'Politica', 'Cultura'])

if pagina == 'Clima':
   cidade = st.sidebar.selectbox('Escolha a cidade:', cidades)
   if cidade == 'Ribeira Grande':
       # Fazer um Web Scraping com informações relevantes da cidade
       st.header("RIBEIRA GRANDE")
       st.write('O Concelho da Ribeira Grande é um concelho/município da ilha de Santo Antão no grupo de Barlavento, em'
                'Cabo Verde. A área desse concelho mais a do concelho de Paul estende-se por apenas 1/3 da área da ilha,'
                'mas têm juntos cerca de 2/3 de sua população.')
       st.image('C:/PycharmProjects/cvcifras/CMRGPontaSol.png')
       st.sidebar.write(clima.ribeira_grande())
   if cidade == 'Ponta do Sol':
       st.sidebar.write(clima.ponta_do_sol())
   if cidade == 'Porto Novo':
       st.sidebar.write(clima.porto_novo())
   if cidade == 'Paul':
       st.sidebar.write(clima.paul())
   if cidade == 'Mindelo':
       st.sidebar.write(clima.mindelo())
   if cidade == 'Santa Luzia':
       st.sidebar.write(clima.santa_luzia())
   if cidade == 'Ribeira Brava':
       st.sidebar.write(clima.ribeira_brava())
   if cidade == 'Tarrafal de São Nicolau':
       st.sidebar.write(clima.tarrafal_sao_nicolau())
   if cidade == 'Espargos':
       st.sidebar.write(clima.espargos())
   if cidade == 'Santa Maria':
       st.sidebar.write(clima.santa_maria())
   if cidade == 'Sal Rei':
       st.sidebar.write(clima.sal_rei())
   if cidade == 'Maio':
       st.sidebar.write(clima.maio())
   if cidade == 'Praia':
       st.sidebar.write(clima.praia())
   if cidade == 'São Domingos':
       st.sidebar.write(clima.sao_domingos())
   if cidade == 'Santa Catarina de Santiago':
       st.sidebar.write(clima.santa_catarina_st())

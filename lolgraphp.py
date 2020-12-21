import tkinter
import sys
import os
import PIL
import datoslolgraphp
from tkinter import *
from functools import partial
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import os.path
import urllib.request
import io
from io import BytesIO
import base64
import requests
import json
import collections
import pandas as pd
from random import random
import threading
import time
import chart_studio.plotly as py
import cufflinks as cf
import numpy as np
import plotly.graph_objs as go
from plotly import tools
from plotly import __version__
import plotly.offline as pyo
from plotly.tools import FigureFactory as FF
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#init_notebook_mode(connected=True)
import plotly.offline
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

#-----------------------------
#FUNCIONES

	#reinicia programa
def reinciar():
	if 'asesinatos'or'asesinatos_2'or'asesinatos_3'or'asesinatos_4'or'asesinatos_5'or'mounstros'or'mounstros_2'or'mounstros_3'or'mounstros_4'or'mounstros_5' in globals():
		try:
			del asesinatos,asesinatos_2,asesinatos_3,asesinatos_4,asesinatos_5,mounstros,mounstros_2,mounstros_3,mounstros_4,mounstros_5
		except UnboundLocalError:
			pass
	if 'asesinatos_6'or'asesinatos_7'or'asesinatos_8'or'asesinatos_9'or'asesinatos_10'or'mounstros_6'or'mounstros_7'or'mounstros_8'or'mounstros_9'or'mounstros_10' in globals():
		try:
			del asesinatos_6,asesinatos_7,asesinatos_8,asesinatos_9,asesinatos_10,mounstros_6,mounstros_7,mounstros_8,mounstros_9,mounstros_10
		except UnboundLocalError:
			pass
	if 'archivo'or'matchsID'or'j1'or'j2'or'j3'or'j4'or'j5'or'j6'or'j7'or'j8'or'j9'or'j10'or'df_building' in globals():
		try:
			del archivo,matchID,j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,df_building
		except UnboundLocalError:
			pass
	if 'edificios_100'or'edificios_200' in globals():
		try:
			del edificios_100,edificios_200
		except UnboundLocalError:
			pass
	if 'items_comprados'or'levels'or'wards_puestos'or'items_destruidos'or'asesinatos'or'wards_destruidos'or'mounstros'or'items_vendidos'or'items_deshecho' in globals():
		try:
			del items_comprados, levels, wards_puestos, items_destruidos, asesinatos, wards_destruidos, mounstros, items_vendidos, items_deshecho
		except UnboundLocalError:
			pass
	if 'items_comprados_2'or'levels_2'or'wards_puestos_2'or'items_destruidos_2'or'asesinatos_2'or'wards_destruidos_2'or'mounstros_2'or'items_vendidos_2'or'items_deshecho_2' in globals():
		try:
			del items_comprados_2, levels_2, wards_puestos_2, items_destruidos_2, asesinatos_2, wards_destruidos_2, mounstros_2, items_vendidos_2, items_deshecho_2
		except UnboundLocalError:
			pass
	if 'items_comprados_3'or'levels_3'or'wards_puestos_3'or'items_destruidos_3'or'asesinatos_3'or'wards_destruidos_3'or'mounstros_3'or'items_vendidos_3'or'items_deshecho_3' in globals():
		try:
			del items_comprados_3, levels_3, wards_puestos_3, items_destruidos_3, asesinatos_3, wards_destruidos_3, mounstros_3, items_vendidos_3, items_deshecho_3
		except UnboundLocalError:
			pass
	if 'items_comprados_4'or'levels_4'or'wards_puestos_4'or'items_destruidos_4'or'asesinatos_4'or'wards_destruidos_4'or'mounstros_4'or'items_vendidos_4'or'items_deshecho_4' in globals():
		try:
			del items_comprados_4, levels_4, wards_puestos_4, items_destruidos_4, asesinatos_4, wards_destruidos_4, mounstros_4, items_vendidos_4, items_deshecho_4
		except UnboundLocalError:
			pass
	if 'items_comprados_5'or'levels_5'or'wards_puestos_5'or'items_destruidos_5'or'asesinatos_5'or'wards_destruidos_5'or'mounstros_5'or'items_vendidos_5'or'items_deshecho_5' in globals():
		try:
			del items_comprados_5, levels_5, wards_puestos_5, items_destruidos_5, asesinatos_5, wards_destruidos_5, mounstros_5, items_vendidos_5, items_deshecho_5
		except UnboundLocalError:
			pass
	if 'items_comprados_6'or'levels_6'or'wards_puestos_6'or'items_destruidos_6'or'asesinatos_6'or'wards_destruidos_6'or'mounstros_6'or'items_vendidos_6'or'items_deshecho_6' in globals():
		try:
			del items_comprados_6, levels_6, wards_puestos_6, items_destruidos_6, asesinatos_6, wards_destruidos_6, mounstros_6, items_vendidos_6, items_deshecho_6
		except UnboundLocalError:
			pass
	if 'items_comprados_7'or'levels_7'or'wards_puestos_7'or'items_destruidos_7'or'asesinatos_7'or'wards_destruidos_7'or'mounstros_7'or'items_vendidos_7'or'items_deshecho_7' in globals():
		try:
			del items_comprados_7, levels_7, wards_puestos_7, items_destruidos_7, asesinatos_7, wards_destruidos_7, mounstros_7, items_vendidos_7, items_deshecho_7
		except UnboundLocalError:
			pass
	if 'items_comprados_8'or'levels_8'or'wards_puestos_8'or'items_destruidos_8'or'asesinatos_8'or'wards_destruidos_8'or'mounstros_8'or'items_vendidos_8'or'items_deshecho_8' in globals():
		try:
			del items_comprados_8, levels_8, wards_puestos_8, items_destruidos_8, asesinatos_8, wards_destruidos_8, mounstros_8, items_vendidos_8, items_deshecho_8
		except UnboundLocalError:
			pass
	if 'items_comprados_9'or'levels_9'or'wards_puestos_9'or'items_destruidos_9'or'asesinatos_9'or'wards_destruidos_9'or'mounstros_9'or'items_vendidos_9'or'items_deshecho_9' in globals():
		try:
			del items_comprados_9, levels_9, wards_puestos_9, items_destruidos_9, asesinatos_9, wards_destruidos_9, mounstros_9, items_vendidos_9, items_deshecho_9
		except UnboundLocalError:
			pass
	if 'items_comprados_10'or'levels_10'or'wards_puestos_10'or'items_destruidos_10'or'asesinatos_10'or'wards_destruidos_10'or'mounstros_10'or'items_vendidos_10'or'items_deshecho_10' in globals():
		try:
			del items_comprados_10, levels_10, wards_puestos_10, items_destruidos_10, asesinatos_10, wards_destruidos_10, mounstros_10, items_vendidos_10, items_deshecho_10
		except UnboundLocalError:
			pass
	if 'killb'or'monsb'or'killr'or'monsr'or'MatchID'or'c1'or'c2'or'c3'or'c4'or'c5'or'c6'or'c7'or'c8'or'c9'or'c10' in globals():
		try:
			del killb,monsb,killr,monsr,MatchID,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10
		except UnboundLocalError:
			pass
	if 'butc1'or'imagec1'or'imagec11'or'butc2'or'imagec2'or'imagec21'or'butc3'or'imagec3'or'imagec31'or'butc4'or'imagec4'or'imagec41'or'butc5'or'imagec5'or'imagec51'or'butc6'or'imagec6'or'imagec61'or'butc7'or'imagec7'or'imagec71'or'butc8'or'imagec8'or'imagec81'or'butc9'or'imagec9'or'imagec91'or'butc10'or'imagec10'or'imagec101'in globals():
		try:
			del butc1,imagec1,imagec11,butc2,imagec2,imagec21,butc3,imagec3,imagec31,butc4,imagec4,imagec41,butc5,imagec5,imagec51,butc6,imagec6,imagec61,butc7,imagec7,imagec71,butc8,imagec8,imagec81,butc9,imagec9,imagec91,butc10,imagec10,imagec101
		except UnboundLocalError:
			pass
	if 'Summoner1'or'Summoner2'or'Summoner3'or'Summoner4'or'Summoner5'or'Summoner6'or'Summoner7'or'Summoner8'or'Summoner9'or'Summoner10'or'ID1'or'ID2'or'ID3'or'ID4'or'ID5'or'ID6'or'ID7'or'ID8'or'ID9'or'ID10' in globals():
		try:
			del Summoner1,Summoner2,Summoner3,Summoner4,Summoner5,Summoner6,Summoner7,Summoner8,Summoner9,Summoner10,ID1,ID2,ID3,ID4,ID5,ID6,ID7,ID8,ID9,ID10
		except UnboundLocalError:
			pass
	if 'campeon1'or'campeon2'or'campeon3'or'campeon4'or'campeon5'or'campeon6'or'campeon7'or'campeon8'or'campeon9'or'campeon10' in globals():
		try:
			del campeon1,campeon2,campeon3,campeon4,campeon5,campeon6,campeon7,campeon8,campeon9,campeon10
		except UnboundLocalError:
			pass
	if 'kb'or'kr'or'mb'or'mr'or'torreb'or'torrer' in globals():
		try:
			del kb,kr,mb,mr,torreb,torrer
			kb=[]
			kr=[]
			mb=[]
			mr=[]
			torreb=[]
			torrer=[]
		except UnboundLocalError:
			pass
	if 'label_msg1'and'label_msg2'and'label_msg3'and'label_msg4'and'label_msg5'and'label_msg6'and'label_msg7'and'label_msg8'and'label_msg9'and'label_msg10' in globals():
		try:
			cv1.delete(label_msg1)
			cv1.delete(label_msg2)
			cv1.delete(label_msg3)
			cv1.delete(label_msg4)
			cv1.delete(label_msg5)
			cv1.delete(label_msg6)
			cv1.delete(label_msg7)
			cv1.delete(label_msg8)
			cv1.delete(label_msg9)
			cv1.delete(label_msg10)
		except UnboundLocalError:
			pass



    #nombre de los campeones
def requestChampID():
	camp = "http://ddragon.leagueoflegends.com/cdn/10.4.1/data/en_US/champion.json"
	responses = requests.get(camp)
	return responses.json()

    #busca partida
def requestMatchID(matchID, APIKey):
	URL2 = "https://la2.api.riotgames.com/lol/match/v4/matches/" + str(matchID) + "?api_key=" + APIKey
	response1 = requests.get(URL2)
	return response1.json()

def getMatchData(APIKey):
    # Devuelve un .json con la data de la partida
    URL = "https://la2.api.riotgames.com/lol/match/v4/timelines/by-match/" + str(matchID) + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()


def cargajson():
	global archivo
	global matchID
	matchID = ID_text.get()
	getMatchData(APIKey)
	archivo = getMatchData(APIKey)

#BUSCAR DATOS
def buscar():
	reinciar()
	cargajson()
	global j1
	global j2
	global j3
	global j4
	global j5
	global j6
	global j7
	global j8
	global j9
	global j10
	global edificios_100
	global edificios_200
	global items_comprados, levels, wards_puestos, items_destruidos, asesinatos, wards_destruidos, mounstros, items_vendidos, items_deshecho
	global items_comprados_2, levels_2, wards_puestos_2, items_destruidos_2, asesinatos_2, wards_destruidos_2, mounstros_2, items_vendidos_2, items_deshechos_2
	global items_comprados_3, levels_3, wards_puestos_3, items_destruidos_3, asesinatos_3, wards_destruidos_3, mounstros_3, items_vendidos_3, items_deshechos_3
	global items_comprados_4, levels_4, wards_puestos_4, items_destruidos_4, asesinatos_4, wards_destruidos_4, mounstros_4, items_vendidos_4, items_deshechos_4
	global items_comprados_5, levels_5, wards_puestos_5, items_destruidos_5, asesinatos_5, wards_destruidos_5, mounstros_5, items_vendidos_5, items_deshechos_5
	global items_comprados_6, levels_6, wards_puestos_6, items_destruidos_6, asesinatos_6, wards_destruidos_6, mounstros_6, items_vendidos_6, items_deshechos_6
	global items_comprados_7, levels_7, wards_puestos_7, items_destruidos_7, asesinatos_7, wards_destruidos_7, mounstros_7, items_vendidos_7, items_deshechos_7
	global items_comprados_8, levels_8, wards_puestos_8, items_destruidos_8, asesinatos_8, wards_destruidos_8, mounstros_8, items_vendidos_8, items_deshechos_8
	global items_comprados_9, levels_9, wards_puestos_9, items_destruidos_9, asesinatos_9, wards_destruidos_9, mounstros_9, items_vendidos_9, items_deshechos_9
	global items_comprados_10, levels_10, wards_puestos_10, items_destruidos_10, asesinatos_10, wards_destruidos_10, mounstros_10, items_vendidos_10, items_deshechos_10
	global killb
	global monsb
	global killr
	global monsr
	j1 = get_participant_frames(archivo,1)
	j2 = get_participant_frames(archivo,2)
	j3 = get_participant_frames(archivo,3)
	j4 = get_participant_frames(archivo,4)
	j5 = get_participant_frames(archivo,5)
	j6 = get_participant_frames(archivo,6)
	j7 = get_participant_frames(archivo,7)
	j8 = get_participant_frames(archivo,8)
	j9 = get_participant_frames(archivo,9)
	j10 = get_participant_frames(archivo,10)
	click()
	champs()
	etiquetas()
	imagechamps()
	baneochamps()
	baneochampsimg()
	Summo()
	edificios_100 = get_building_info(100)
	edificios_200 = get_building_info(200)
	items_comprados, levels, wards_puestos, items_destruidos, asesinatos, wards_destruidos, mounstros, items_vendidos, items_deshecho  = items_p(1)
	tems_comprados_2, levels_2, wards_puestos_2, items_destruidos_2, asesinatos_2, wards_destruidos_2, mounstros_2, items_vendidos_2, items_deshechos_2 = items_p(2)
	items_comprados_3, levels_3, wards_puestos_3, items_destruidos_3, asesinatos_3, wards_destruidos_3, mounstros_3, items_vendidos_3, items_deshechos_3 = items_p(3)
	items_comprados_4, levels_4, wards_puestos_4, items_destruidos_4, asesinatos_4, wards_destruidos_4, mounstros_4, items_vendidos_4, items_deshechos_4 = items_p(4)
	items_comprados_5, levels_5, wards_puestos_5, items_destruidos_5, asesinatos_5, wards_destruidos_5, mounstros_5, items_vendidos_5, items_deshechos_5 = items_p(5)
	items_comprados_6, levels_6, wards_puestos_6, items_destruidos_6, asesinatos_6, wards_destruidos_6, mounstros_6, items_vendidos_6, items_deshechos_6 = items_p(6)
	items_comprados_7, levels_7, wards_puestos_7, items_destruidos_7, asesinatos_7, wards_destruidos_7, mounstros_7, items_vendidos_7, items_deshechos_7 = items_p(7)
	items_comprados_8, levels_8, wards_puestos_8, items_destruidos_8, asesinatos_8, wards_destruidos_8, mounstros_8, items_vendidos_8, items_deshechos_8 = items_p(8)
	items_comprados_9, levels_9, wards_puestos_9, items_destruidos_9, asesinatos_9, wards_destruidos_9, mounstros_9, items_vendidos_9, items_deshechos_9 = items_p(9)
	items_comprados_10, levels_10, wards_puestos_10, items_destruidos_10, asesinatos_10, wards_destruidos_10, mounstros_10, items_vendidos_10, items_deshechos_10 = items_p(10)
	killb = pd.concat([asesinatos,asesinatos_2,asesinatos_3,asesinatos_4,asesinatos_5])
	monsb = pd.concat([mounstros,mounstros_2,mounstros_3,mounstros_4,mounstros_5])
	killr = pd.concat([asesinatos_6,asesinatos_7,asesinatos_8,asesinatos_9,asesinatos_10])
	monsr = pd.concat([mounstros_6,mounstros_7,mounstros_8,mounstros_9,mounstros_10])
	killb = killb.sort_values("Tiempo")
	monsb = monsb.sort_values("Tiempo")
	killr = killr.sort_values("Tiempo")
	monsr = monsr.sort_values("Tiempo")
	killb = killb.reset_index(drop=True)
	killr = killr.reset_index(drop=True)
	monsr = monsr.reset_index(drop=True)
	monsb = monsb.reset_index(drop=True)
	listasesinosb()
	listasesinosr()
	listatorr()
	listatorb()
	listamonstr()
	listamonstb()
	add_command()

#EL ERROR SUCEDE CUANDO EN LA PARTIDA UN EQUIPO NO TIRO NINGUNA TORRE
#Torres

def get_building_info(numero):
	towersnone = {'Tipo': [[]],
	'Tiempo': [[]],'PosicionX': [[]],'PosicionY': [[]],'ID Asesino': [0],'ID Asistentes': [[]],'ID Equipo': [[]],'Tipo de Edificio': [[]],
	'Linea': [[]],'Tipo de Torre': [[]]}
	nonetowers = pd.DataFrame(towersnone, columns = ['Tipo', 'Tiempo','PosicionX','PosicionY','ID Asesino','ID Asistentes',
	                                                'ID Equipo','Tipo de Edificio','Linea','Tipo de Torre'])
	i=0
	lis = []
	try:
		for g in archivo['frames']:
			for e in range(0, len(archivo['frames'][i]['events'])):
				if (archivo['frames'][i]['events'][e]['type'] == "BUILDING_KILL") and (archivo['frames'][i]['events'][e]['teamId'] == numero):
					typ = archivo['frames'][i]['events'][e]['type']
					time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
					posicionx = archivo['frames'][i]['events'][e]['position']['x']
					posiciony = archivo['frames'][i]['events'][e]['position']['y']
					killerId = archivo['frames'][i]['events'][e]['killerId']
					asistentesIds = archivo['frames'][i]['events'][e]['assistingParticipantIds']
					teamId = archivo['frames'][i]['events'][e]['teamId']
					tipoDeEdificio = archivo['frames'][i]['events'][e]['buildingType']
					linea = archivo['frames'][i]['events'][e]['laneType']
					tipoDeTorre = archivo['frames'][i]['events'][e]['towerType']

					lis.append([typ, time, posicionx, posiciony, killerId, asistentesIds, teamId, tipoDeEdificio, linea, tipoDeTorre])

					df_building = pd.DataFrame(lis, columns = ('Tipo', 'Tiempo', 'PosicionX', 'PosicionY', 'ID Asesino', 'IDs Asistentes', 'ID Equipo', 'Tipo de Edificio', 'Linea', 'Tipo de Torre'))
			i+=1
		return df_building
	except UnboundLocalError:
		return nonetowers



#Items/asesinatos/monstruos
def items_p(player):
    i=0
    l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11 = [], [], [], [], [], [], [], [], [], [], []

    for g in archivo['frames']:
        for e in range(0, len(archivo['frames'][i]['events'])):

            #1
            if (archivo['frames'][i]['events'][e]['type'] == "ITEM_PURCHASED") and (archivo['frames'][i]['events'][e]['participantId'] == player):
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                typ = archivo['frames'][i]['events'][e]['type']
                parId = archivo['frames'][i]['events'][e]['participantId']
                itemId =archivo['frames'][i]['events'][e]['itemId']

                l1.append([typ, time, parId, itemId])#("Tipo", "Tiempo", "ID Invocador", "ID item")

            #2
            if (archivo['frames'][i]['events'][e]['type'] == "SKILL_LEVEL_UP") and (archivo['frames'][i]['events'][e]['participantId'] == player):
                typ = archivo['frames'][i]['events'][e]['type']
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                parId = archivo['frames'][i]['events'][e]['participantId']
                skillSlot = archivo['frames'][i]['events'][e]['skillSlot']
                lvlType = archivo['frames'][i]['events'][e]['levelUpType']

                l2.append([typ, time, parId, skillSlot, lvlType])#("Tipo", "Tiempo", "ID Invocador", "Skill Slot", "Tipo de Nivel")

            #3
            if (archivo['frames'][i]['events'][e]['type'] == "WARD_PLACED") and (archivo['frames'][i]['events'][e]['creatorId'] == player):
                typ = archivo['frames'][i]['events'][e]['type']
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                wardType = archivo['frames'][i]['events'][e]['wardType']
                creatorId = archivo['frames'][i]['events'][e]['creatorId']

                l3.append([typ, time, wardType, creatorId])#('Tipo', 'Tiempo', 'Tipo de Ward', 'ID creador')

            # 4
            if (archivo['frames'][i]['events'][e]['type'] == "ITEM_DESTROYED") and (archivo['frames'][i]['events'][e]['participantId'] == player):
                typ = archivo['frames'][i]['events'][e]['type']
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                parId = archivo['frames'][i]['events'][e]['participantId']
                itemId = archivo['frames'][i]['events'][e]['itemId']

                l4.append([typ, time, parId, itemId])#('Tipo', 'Tiempo', 'Id Invocador', 'Id Item')

            #5
            if (archivo['frames'][i]['events'][e]['type'] == "CHAMPION_KILL") and (archivo['frames'][i]['events'][e]['killerId'] == player):
                typ = archivo['frames'][i]['events'][e]['type']
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                posicionx = archivo['frames'][i]['events'][e]['position']['x']
                posiciony = archivo['frames'][i]['events'][e]['position']['y']
                invocadorAsesino = archivo['frames'][i]['events'][e]['killerId']
                invocadorVictima = archivo['frames'][i]['events'][e]['victimId']
                asistentesIds = archivo['frames'][i]['events'][e]['assistingParticipantIds']

                l5.append([typ, time, posicionx, posiciony, invocadorAsesino, invocadorVictima, asistentesIds])#('Tipo', 'Tiempo', 'Posicion', 'Asesino ID', 'Victima ID', 'Asistentes ID')

            #6
            if (archivo['frames'][i]['events'][e]['type'] == "WARD_KILL") and (archivo['frames'][i]['events'][e]['killerId'] == player):
                typ = archivo['frames'][i]['events'][e]['type']
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                wardType = archivo['frames'][i]['events'][e]['wardType']
                killerId = archivo['frames'][i]['events'][e]['killerId']

                l6.append([typ, time, wardType, killerId])#('Tipo', 'Tiempo', 'Tipo de Ward', 'ID Destructor')

            #7
            if (archivo['frames'][i]['events'][e]['type'] == "ELITE_MONSTER_KILL") and (archivo['frames'][i]['events'][e]['killerId'] == player):

                typ = archivo['frames'][i]['events'][e]['type']
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                posicionx = archivo['frames'][i]['events'][e]['position']['x']
                posiciony = archivo['frames'][i]['events'][e]['position']['y']
                killerId = archivo['frames'][i]['events'][e]['killerId']
                tipoDeMounstro = archivo['frames'][i]['events'][e]['monsterType']

                try:
                    subtipoDeMounstro = archivo['frames'][i]['events'][e]['monsterSubType']

                except:
                    subtipoDeMounstro = ' '

                l7.append([typ, time, posicionx, posiciony, killerId, tipoDeMounstro, subtipoDeMounstro])

            #8
            if (archivo['frames'][i]['events'][e]['type'] == "ITEM_SOLD") and (archivo['frames'][i]['events'][e]['participantId'] == player):
                typ = archivo['frames'][i]['events'][e]['type']
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                parId = archivo['frames'][i]['events'][e]['participantId']
                itemId = archivo['frames'][i]['events'][e]['itemId']

                l8.append([typ, time, parId, itemId])#('Tipo', 'Tiempo', 'Id Invocador', 'Id Item')

            #9
            if (archivo['frames'][i]['events'][e]['type'] == "ITEM_UNDO") and (archivo['frames'][i]['events'][e]['participantId'] == player):
                typ = archivo['frames'][i]['events'][e]['type']
                time = int(convertMinS(archivo['frames'][i]['events'][e]['timestamp']))
                parId = archivo['frames'][i]['events'][e]['participantId']
                afterId = archivo['frames'][i]['events'][e]['afterId']
                beforeId = archivo['frames'][i]['events'][e]['beforeId']

                l9.append([typ, time, parId, afterId, beforeId])#('Tipo', 'Tiempo', 'Id Invocador', 'Id Antes', 'ID Despues')



        i+=1
    df1 = pd.DataFrame(l1,columns = ("Tipo", "Tiempo", "ID Invocador", "ID item"))
    df2 = pd.DataFrame(l2,columns = ("Tipo", "Tiempo", "ID Invocador", "Skill Slot", "Tipo de Nivel"))
    df3 = pd.DataFrame(l3, columns = ('Tipo', 'Tiempo', 'Tipo de Ward', 'ID creador'))
    df4 = pd.DataFrame(l4, columns = ('Tipo', 'Tiempo', 'Id Invocador', 'Id Item'))
    df5 = pd.DataFrame(l5, columns = ('Tipo', 'Tiempo', 'PosicionX', 'PosicionY', 'Asesino ID', 'Victima ID', 'Asistentes ID'))
    df6 = pd.DataFrame(l6, columns = ('Tipo', 'Tiempo', 'Tipo de Ward', 'ID Destructor'))
    df7 = pd.DataFrame(l7, columns = ('Tipo', 'Tiempo', 'PosicionX','PosicionY', 'Asesino', 'Tipo de Mounstro', 'Subtipo de Mounstro'))
    df8 = pd.DataFrame(l8, columns = ('Tipo', 'Tiempo', 'Id Invocador', 'Id Item'))
    df9 = pd.DataFrame(l9, columns = ('Tipo', 'Tiempo', 'Id Invocador', 'Id Antes', 'ID Despues'))

    return  df1, df2, df3, df4, df5, df6, df7, df8, df9

#Torres monstruos
def listasesinosb():
    for i in range(0, len(killb)):
        killblu = (eval("Summoner"+(str(killb['Asesino ID'][i]))))
        deathblu= (eval("Summoner"+(str(killb['Victima ID'][i]))))
        tiem= str(killb['Tiempo'][i])
        kb.append("min:"+tiem+" || "+k+killblu+"  ||  "+m+deathblu)
    killblue = pd.DataFrame(kb)
    return killblue

def listasesinosr():
    for i in range(0, len(killr)):
        killred = (eval("Summoner"+(str(killr['Asesino ID'][i]))))
        deathred= (eval("Summoner"+(str(killr['Victima ID'][i]))))
        tiem= str(killr['Tiempo'][i])
        kr.append("min:"+tiem+" || "+k+killred+"  ||  "+m+deathred)
    killreds = pd.DataFrame(kr)
    return killreds

def listamonstb():
    for i in range(0, len(monsb)):
        killblu = (eval("Summoner"+(str(monsb['Asesino'][i]))))
        deathblu= (str(monsb['Tipo de Mounstro'][i]))
        tipblu= (str(monsb['Subtipo de Mounstro'][i]))
        tiem= str(monsb['Tiempo'][i])
        mb.append("min:"+tiem+" || "+k+killblu+"  ||  "+m+deathblu+":"+tipblu)
    monsblue = pd.DataFrame(mb)
    return monsblue

def listamonstr():
    for i in range(0, len(monsr)):
        killblu = (eval("Summoner"+(str(monsr['Asesino'][i]))))
        deathblu= (str(monsr['Tipo de Mounstro'][i]))
        tipblu= (str(monsr['Subtipo de Mounstro'][i]))
        tiem= str(monsr['Tiempo'][i])
        mr.append("min:"+tiem+" || "+k+killblu+"  ||  "+m+deathblu+":"+tipblu)
    monsred = pd.DataFrame(mr)
    return monsred

def listatorb():
    for i in range(0, len(edificios_100)):
        killre = (eval("Summoner"+(str(edificios_100['ID Asesino'][i]))))
        deathre= (str(edificios_100['Tipo de Edificio'][i]))
        tipre= (str(edificios_100['Linea'][i]))
        titorr=(str(edificios_100['Tipo de Torre'][i]))
        tiem= str(edificios_100['Tiempo'][i])
        torreb.append("min:"+tiem+" || "+k+killre+"  ||  "+m+deathre+":"+tipre+"-"+titorr)
    torrebl = pd.DataFrame(torreb)
    return torrebl

def listatorr():
    for i in range(0, len(edificios_200)):
        killre = (eval("Summoner"+(str(edificios_200['ID Asesino'][i]))))
        deathre= (str(edificios_200['Tipo de Edificio'][i]))
        tipre= (str(edificios_200['Linea'][i]))
        titorr=(str(edificios_200['Tipo de Torre'][i]))
        tiem= str(edificios_200['Tiempo'][i])
        torrer.append("min:"+tiem+" || "+k+killre+"  ||  "+m+deathre+":"+tipre+"-"+titorr)
    torrere = pd.DataFrame(torrer)
    return torrere




#GRAFICOS
def graficochamp():
	layoutt = go.Layout(title = "Datos Partida", xaxis = {'title': 'Tiempo'},yaxis = {'title': 'Total'})
	fig = go.Figure(layout=layoutt)
	#jugador1
	fig.add_trace(go.Scatter(x=j1["Tiempo"],y=j1["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j1["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j1["Tiempo"],y=j1["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j1["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j1["Tiempo"],y=j1["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j1["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j1["Tiempo"],y=j1["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j1["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j1["Tiempo"],y=j1["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j1["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j1["Tiempo"],y=j1["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j1["ID Invocador"][0]))+"[0]['name']"))))
	#jugador2
	fig.add_trace(go.Scatter(x=j2["Tiempo"],y=j2["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j2["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j2["Tiempo"],y=j2["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j2["ID Invocador"][0]))+"[0]['name']")) ))
	fig.add_trace(go.Scatter(x=j2["Tiempo"],y=j2["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j2["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j2["Tiempo"],y=j2["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j2["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j2["Tiempo"],y=j2["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j2["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j2["Tiempo"],y=j2["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j2["ID Invocador"][0]))+"[0]['name']"))))
	#jugador3
	fig.add_trace(go.Scatter(x=j3["Tiempo"],y=j3["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j3["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j3["Tiempo"],y=j3["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j3["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j3["Tiempo"],y=j3["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j3["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j3["Tiempo"],y=j3["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j3["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j3["Tiempo"],y=j3["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j3["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j3["Tiempo"],y=j3["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j3["ID Invocador"][0]))+"[0]['name']"))))
	#jugador4
	fig.add_trace(go.Scatter(x=j4["Tiempo"],y=j4["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j4["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j4["Tiempo"],y=j4["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j4["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j4["Tiempo"],y=j4["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j4["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j4["Tiempo"],y=j4["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j4["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j4["Tiempo"],y=j4["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j4["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j4["Tiempo"],y=j4["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j4["ID Invocador"][0]))+"[0]['name']"))))
	#jugador5
	fig.add_trace(go.Scatter(x=j5["Tiempo"],y=j5["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j5["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j5["Tiempo"],y=j5["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j5["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j5["Tiempo"],y=j5["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j5["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j5["Tiempo"],y=j5["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j5["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j5["Tiempo"],y=j5["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j5["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j5["Tiempo"],y=j5["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j5["ID Invocador"][0]))+"[0]['name']"))))
	#jugador6
	fig.add_trace(go.Scatter(x=j6["Tiempo"],y=j6["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j6["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j6["Tiempo"],y=j6["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j6["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j6["Tiempo"],y=j6["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j6["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j6["Tiempo"],y=j6["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j6["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j6["Tiempo"],y=j6["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j6["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j6["Tiempo"],y=j6["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j6["ID Invocador"][0]))+"[0]['name']"))))
	#jugador7
	fig.add_trace(go.Scatter(x=j7["Tiempo"],y=j7["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j7["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j7["Tiempo"],y=j7["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j7["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j7["Tiempo"],y=j7["Oro"],mode="lines",name='Oro :'  + (eval("campeon"+(str(j7["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j7["Tiempo"],y=j7["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j7["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j7["Tiempo"],y=j7["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j7["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j7["Tiempo"],y=j7["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j7["ID Invocador"][0]))+"[0]['name']"))))
	#jugador8
	fig.add_trace(go.Scatter(x=j8["Tiempo"],y=j8["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j8["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j8["Tiempo"],y=j8["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j8["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j8["Tiempo"],y=j8["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j8["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j8["Tiempo"],y=j8["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j8["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j8["Tiempo"],y=j8["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j8["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j8["Tiempo"],y=j8["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j8["ID Invocador"][0]))+"[0]['name']"))))
	#jugador9
	fig.add_trace(go.Scatter(x=j9["Tiempo"],y=j9["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j9["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j9["Tiempo"],y=j9["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j9["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j9["Tiempo"],y=j9["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j9["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j9["Tiempo"],y=j9["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j9["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j9["Tiempo"],y=j9["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j9["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j9["Tiempo"],y=j9["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j9["ID Invocador"][0]))+"[0]['name']"))))
	#jugador10
	fig.add_trace(go.Scatter(x=j10["Tiempo"],y=j10["CsMinions"],mode="lines",name='Cs Minions : ' + (eval("campeon"+(str(j10["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j10["Tiempo"],y=j10["CsJg"],mode="lines",name='Cs Jungla : ' + (eval("campeon"+(str(j10["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j10["Tiempo"],y=j10["Oro"],mode="lines",name='Oro : ' + (eval("campeon"+(str(j10["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j10["Tiempo"],y=j10["Oro Total"],mode="lines",name='Oro Total : ' + (eval("campeon"+(str(j10["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j10["Tiempo"],y=j10["Nivel"],mode="lines",name='Nivel : ' + (eval("campeon"+(str(j10["ID Invocador"][0]))+"[0]['name']"))))
	fig.add_trace(go.Scatter(x=j10["Tiempo"],y=j10["Exp"],mode="lines",name='Experiencia : ' + (eval("campeon"+(str(j10["ID Invocador"][0]))+"[0]['name']"))))

	fig.update_layout(updatemenus=[dict(active=0,buttons=list([dict(label=(eval('Summoner'+(str(j1["ID Invocador"][0])))),method="update",args=[{"visible": [True,True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j1["ID Invocador"][0])))),"annotations": []}]),
	dict(label=(eval('Summoner'+(str(j2["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,True,True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j2["ID Invocador"][0])))),"annotations": []}]),
    dict(label=(eval('Summoner'+(str(j3["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,True, True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j3["ID Invocador"][0])))),"annotations": []}]),
    dict(label=(eval('Summoner'+(str(j4["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j4["ID Invocador"][0])))),"annotations": []}]),
    dict(label=(eval('Summoner'+(str(j5["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j5["ID Invocador"][0])))),"annotations": []}]),
    dict(label=(eval('Summoner'+(str(j6["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j6["ID Invocador"][0])))),"annotations": []}]),
    dict(label=(eval('Summoner'+(str(j7["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j7["ID Invocador"][0])))),"annotations": []}]),
    dict(label=(eval('Summoner'+(str(j8["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j8["ID Invocador"][0])))),"annotations": []}]),
    dict(label=(eval('Summoner'+(str(j9["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True, True, True, True, True,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j9["ID Invocador"][0])))),"annotations": []}]),
    dict(label=(eval('Summoner'+(str(j10["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True, True, True, True, True]},{"title": (eval('Summoner'+(str(j10["ID Invocador"][0])))),"annotations": []}]),
    #Equipo azul
    dict(label="Equipo Azul : " + str(EA_text.get()),method="update",args=[{"visible": [True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},{"title": "Equipo Azul : " + str(EA_text.get()),"annotations": []}]),
    #Equipo rojo
    dict(label="Equipo Rojo : " + str(ER_text.get()),method="update",args=[{"visible": [False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True]},{"title": "Equipo Rojo : " + str(ER_text.get()),"annotations": []}]),
    #Todos
    dict(label="Todos",method="update",args=[{"visible": [True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True,True, True, True, True, True, True, True]},{"title": "Todos" ,"annotations": []}]),
	]))])

	pyo.plot(fig, filename='sample_plot.html')

def graficomons():
	mons1 = go.Scatter(x=monsb['Tiempo'],mode= 'lines+markers',hoverinfo = 'text',name="Blue Monstruos",text=mb,marker_color='rgba(0,30,255,1)')
	mons2 = go.Scatter(x=monsr['Tiempo'],mode= 'lines+markers',hoverinfo = 'text',name="Red Monstruos",text=mr,marker_color='rgba(253,0,15,1)')
	datamons = [mons1,mons2]
	layout2 = go.Layout(title='Grieta del invocador: Monstruos Elite',xaxis = dict(tick0 = 1,dtick = 1),xaxis_title='Minutos',yaxis_title='Cantidad')
	fig2 = go.Figure(data=datamons, layout=layout2)
	pyo.plot(fig2, filename='sample_plot.html')

def graficomap():
	layoutmap = go.Layout(title = "Grieta del Invocador")
	fig3 = go.Figure(layout=layoutmap)
	#POSICIONES
	fig3.add_trace(go.Scatter(x=j1['PosicionX'], y=j1['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j1["ID Invocador"][0])))),text=j1['Tiempo'],marker=dict(color='rgba(0,30,253,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j2['PosicionX'], y=j2['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j2["ID Invocador"][0])))),text=j2['Tiempo'],marker=dict(color='rgba(0,13,107,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j3['PosicionX'], y=j3['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j3["ID Invocador"][0])))),text=j3['Tiempo'],marker=dict(color='rgba(0,223,255,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j4['PosicionX'], y=j4['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j4["ID Invocador"][0])))),text=j4['Tiempo'],marker=dict(color='rgba(0,255,56,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j5['PosicionX'], y=j5['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j5["ID Invocador"][0])))),text=j5['Tiempo'],marker=dict(color='rgba(132,3,223,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j6['PosicionX'], y=j6['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j6["ID Invocador"][0])))),text=j6['Tiempo'],marker=dict(color='rgba(255,172,172,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j7['PosicionX'], y=j7['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j7["ID Invocador"][0])))),text=j7['Tiempo'],marker=dict(color='rgba(249,238,0,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j8['PosicionX'], y=j8['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j8["ID Invocador"][0])))),text=j8['Tiempo'],marker=dict(color='rgba(133,40,0,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j9['PosicionX'], y=j9['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j9["ID Invocador"][0])))),text=j9['Tiempo'],marker=dict(color='rgba(255,141,0,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	fig3.add_trace(go.Scatter(x=j10['PosicionX'], y=j10['PosicionY'],mode= 'lines+markers',hoverinfo = 'text',name=(eval('Summoner'+(str(j10["ID Invocador"][0])))),text=j10['Tiempo'],marker=dict(color='rgba(253,0,13,1)',size=8,opacity=0.8,line=dict(color='black',width=1)),line=dict(width=0.5)))
	#ASESINATOS
	fig3.add_trace(go.Scatter(x=killb['PosicionX'], y=killb['PosicionY'],mode= 'markers',hoverinfo = 'text',name="Blue Kills",text=kb,marker_color='rgba(0,30,253,1)',marker=dict(size=8,opacity=0.8,line=dict(width=2),color="blue",symbol=104)))
	fig3.add_trace(go.Scatter(x=killr['PosicionX'], y=killr['PosicionY'],mode= 'markers',hoverinfo = 'text',name="Red Kills",text=kr,marker_color='rgba(253,0,13,1)',marker=dict(size=8,opacity=0.8,line=dict(width=2),color="red",symbol=104)))
	#TORRES
	fig3.add_trace(go.Scatter(x=edificios_100['PosicionX'], y=edificios_100['PosicionY'],mode= 'markers',hoverinfo = 'text',name="Red T Kills",text=torreb,marker_color='rgba(253,0,13,1)',marker=dict(size=8,opacity=0.8,line=dict(color='black',width=1),color="red",symbol='star')))
	fig3.add_trace(go.Scatter(x=edificios_200['PosicionX'], y=edificios_200['PosicionY'],mode= 'markers',hoverinfo = 'text',name="Blue T Kills",text=torrer,marker_color='rgba(0,30,253,1)',marker=dict(size=8,opacity=0.8,line=dict(color='black',width=1),color="blue",symbol='star')))

	fig3.update_layout(updatemenus=[dict(active=0,buttons=list([
	#Equipo azul
	dict(label="Equipo Azul",method="update",args=[{"visible": [True,True,True,True,True,False,False,False,False,False,True,False,False,True]},{"title": "Equipo Azul","annotations": []}]),
	#Equipo rojo
	dict(label="Equipo Rojo",method="update",args=[{"visible": [False,False,False,False,False,True,True,True,True,True,False,True,True,False]},{"title": "Equipo Rojo","annotations": []}]),
	#Todos
	dict(label="Todos",method="update",args=[{"visible": [True,True,True,True,True,True,True,True,True,True,True,True,True,True]},{"title": "Todos","annotations": []}])
	]))])

	fig3.update_xaxes(range=[0, 15000],showgrid=False)
	fig3.update_yaxes(range=[0, 15000],showgrid=False)
	fig3['layout']['title'] = 'Grieta del Invocador'
	fig3['layout']['images'] = [dict(source="https://cdn.statically.io/gist/serenomoon/604d40d26cedd6abb0b0c7872b134c07/raw/54b318c411df1c86173263edee54d0c83040b83d/Mapl.svg",x=0.5, y=0.5,sizex=1, sizey=1,xanchor="center",yanchor="middle",sizing="stretch",layer="below")]
	fig3['layout']['autosize'] =False
	fig3['layout']['width'] =1200
	fig3['layout']['height'] =1000
	pyo.plot(fig3, filename='sample_plot.html')

def graficoheat():
	layoutmap = go.Layout(title = "Grieta del Invocador")
	fig4 = go.Figure(layout=layoutmap)
	#POSICIONES
	fig4.add_trace(go.Histogram2dContour(x=j1['PosicionX'], y=j1['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j1["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j2['PosicionX'], y=j2['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j2["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j3['PosicionX'], y=j3['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j3["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j4['PosicionX'], y=j4['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j4["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j5['PosicionX'], y=j5['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j5["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j6['PosicionX'], y=j6['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j6["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j7['PosicionX'], y=j7['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j7["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j8['PosicionX'], y=j8['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j8["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j9['PosicionX'], y=j9['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j9["ID Invocador"][0]))))))
	fig4.add_trace(go.Histogram2dContour(x=j10['PosicionX'], y=j10['PosicionY'],hoverinfo = 'text',opacity=0.7,name=(eval('Summoner'+(str(j10["ID Invocador"][0]))))))

	fig4.update_layout(updatemenus=[dict(active=0,buttons=list([
	#J1
	dict(label=(eval('Summoner'+(str(j1["ID Invocador"][0])))),method="update",args=[{"visible": [True,False,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j1["ID Invocador"][0])))),"annotations": []}]),
	#J2
	dict(label=(eval('Summoner'+(str(j2["ID Invocador"][0])))),method="update",args=[{"visible": [False,True,False,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j2["ID Invocador"][0])))),"annotations": []}]),
	#J3
	dict(label=(eval('Summoner'+(str(j3["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,True,False,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j3["ID Invocador"][0])))),"annotations": []}]),
	#J4
	dict(label=(eval('Summoner'+(str(j4["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,True,False,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j4["ID Invocador"][0])))),"annotations": []}]),
	#J5
	dict(label=(eval('Summoner'+(str(j5["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,True,False,False,False,False,False]},{"title": (eval('Summoner'+(str(j5["ID Invocador"][0])))),"annotations": []}]),
	#J6
	dict(label=(eval('Summoner'+(str(j6["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,True,False,False,False,False]},{"title": (eval('Summoner'+(str(j6["ID Invocador"][0])))),"annotations": []}]),
	#J7
	dict(label=(eval('Summoner'+(str(j7["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,True,False,False,False]},{"title": (eval('Summoner'+(str(j7["ID Invocador"][0])))),"annotations": []}]),
	#J8
	dict(label=(eval('Summoner'+(str(j8["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,True,False,False]},{"title": (eval('Summoner'+(str(j8["ID Invocador"][0])))),"annotations": []}]),
	#J9
	dict(label=(eval('Summoner'+(str(j9["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,True,False]},{"title": (eval('Summoner'+(str(j9["ID Invocador"][0])))),"annotations": []}]),
	#J10
	dict(label=(eval('Summoner'+(str(j10["ID Invocador"][0])))),method="update",args=[{"visible": [False,False,False,False,False,False,False,False,False,True]},{"title": (eval('Summoner'+(str(j10["ID Invocador"][0])))),"annotations": []}]),
	#Equipo azul
	dict(label="Equipo Azul",method="update",args=[{"visible": [True,True,True,True,True,False,False,False,False,False]},{"title": "Equipo Azul","annotations": []}]),
	#Equipo rojo
	dict(label="Equipo Rojo",method="update",args=[{"visible": [False,False,False,False,False,True,True,True,True,True]},{"title": "Equipo Rojo","annotations": []}]),
	#Todos
	dict(label="Todos",method="update",args=[{"visible": [True,True,True,True,True,True,True,True,True,True]},{"title": "Todos","annotations": []}])
	]))])

	fig4.update_xaxes(range=[0, 15000],showgrid=False)
	fig4.update_yaxes(range=[0, 15000],showgrid=False)
	fig4['layout']['title'] = 'Grieta del Invocador'
	fig4['layout']['images'] = [dict(source="https://cdn.statically.io/gist/serenomoon/604d40d26cedd6abb0b0c7872b134c07/raw/54b318c411df1c86173263edee54d0c83040b83d/Mapl.svg",x=0.5, y=0.5,sizex=1, sizey=1,xanchor="center",yanchor="middle",sizing="stretch",layer="below")]
	fig4['layout']['autosize'] =False
	fig4['layout']['width'] =1200
	fig4['layout']['height'] =1000
	pyo.plot(fig4, filename='sample_plot.html')



#VARIABLES CONFIRMADAS
Summoner0 = "Súbditos"
kb=[]
kr=[]
mb=[]
mr=[]
torreb=[]
torrer=[]
k="K: "
m="M: "


ChampID = requestChampID()

APIKey = "RGAPI-a5a0ad8f-492b-48ed-b388-a2402d558f45"

def click():
	global MatchID
	MatchID = requestMatchID(matchID, APIKey)
	global c1
	global c2
	global c3
	global c4
	global c5
	global c6
	global c7
	global c8
	global c9
	global c10
	global ba1
	global ba2
	global ba3
	global ba4
	global ba5
	global ba6
	global ba7
	global ba8
	global ba9
	global ba10
	c1 = MatchID["participants"][0]["championId"]
	c2 = MatchID["participants"][1]["championId"]
	c3 = MatchID["participants"][2]["championId"]
	c4 = MatchID["participants"][3]["championId"]
	c5 = MatchID["participants"][4]["championId"]
	c6 = MatchID["participants"][5]["championId"]
	c7 = MatchID["participants"][6]["championId"]
	c8 = MatchID["participants"][7]["championId"]
	c9 = MatchID["participants"][8]["championId"]
	c10 = MatchID["participants"][9]["championId"]
	ba1 = MatchID['teams'][0]['bans'][0]['championId']
	ba2 = MatchID['teams'][0]['bans'][1]['championId']
	ba3 = MatchID['teams'][0]['bans'][2]['championId']
	ba4 = MatchID['teams'][0]['bans'][3]['championId']
	ba5 = MatchID['teams'][0]['bans'][4]['championId']
	ba6 = MatchID['teams'][1]['bans'][0]['championId']
	ba7 = MatchID['teams'][1]['bans'][1]['championId']
	ba8 = MatchID['teams'][1]['bans'][2]['championId']
	ba9 = MatchID['teams'][1]['bans'][3]['championId']
	ba10 = MatchID['teams'][1]['bans'][4]['championId']

def imagechamps():
	global butc1
	global imagec1
	global imagec11
	global butc2
	global imagec2
	global imagec21
	global butc3
	global imagec3
	global imagec31
	global butc4
	global imagec4
	global imagec41
	global butc5
	global imagec5
	global imagec51
	global butc6
	global imagec6
	global imagec61
	global butc7
	global imagec7
	global imagec71
	global butc8
	global imagec8
	global imagec81
	global butc9
	global imagec9
	global imagec91
	global butc10
	global imagec10
	global imagec101
	#campeon1
	imagec1 = Image.open("champion\\" + (str(campeon1[0]['name'])) + ".png")
	imagec1 = imagec1.resize((30, 30), Image.ANTIALIAS)
	imagec11 = ImageTk.PhotoImage(imagec1)
	butc1=Button(win)
	butc1.config(image=imagec11,width="30",height="30",borderwidth=0)
	butc1.place(x=180,y=309)
	#campeon2
	imagec2 = Image.open("champion\\" + (str(campeon2[0]['name'])) + ".png")
	imagec2 = imagec2.resize((30, 30), Image.ANTIALIAS)
	imagec21 = ImageTk.PhotoImage(imagec2)
	butc2=Button(win)
	butc2.config(image=imagec21,width="30",height="30",borderwidth=0)
	butc2.place(x=180,y=344)
	#campeon3
	imagec3 = Image.open("champion\\" + (str(campeon3[0]['name'])) + ".png")
	imagec3 = imagec3.resize((30, 30), Image.ANTIALIAS)
	imagec31 = ImageTk.PhotoImage(imagec3)
	butc3=Button(win)
	butc3.config(image=imagec31,width="30",height="30",borderwidth=0)
	butc3.place(x=180,y=379)
	#campeon4
	imagec4 = Image.open("champion\\" + (str(campeon4[0]['name'])) + ".png")
	imagec4 = imagec4.resize((30, 30), Image.ANTIALIAS)
	imagec41 = ImageTk.PhotoImage(imagec4)
	butc4=Button(win)
	butc4.config(image=imagec41,width="30",height="30",borderwidth=0)
	butc4.place(x=180,y=414)
	#campeon5
	imagec5 = Image.open("champion\\" + (str(campeon5[0]['name'])) + ".png")
	imagec5 = imagec5.resize((30, 30), Image.ANTIALIAS)
	imagec51 = ImageTk.PhotoImage(imagec5)
	butc5=Button(win)
	butc5.config(image=imagec51,width="30",height="30",borderwidth=0)
	butc5.place(x=180,y=449)

	#campeon6
	imagec6 = Image.open("champion\\" + (str(campeon6[0]['name'])) + ".png")
	imagec6 = imagec6.resize((30, 30), Image.ANTIALIAS)
	imagec61 = ImageTk.PhotoImage(imagec6)
	butc6=Button(win)
	butc6.config(image=imagec61,width="30",height="30",borderwidth=0)
	butc6.place(x=594,y=309)
	#campeon7
	imagec7 = Image.open("champion\\" + (str(campeon7[0]['name'])) + ".png")
	imagec7 = imagec7.resize((30, 30), Image.ANTIALIAS)
	imagec71 = ImageTk.PhotoImage(imagec7)
	butc7=Button(win)
	butc7.config(image=imagec71,width="30",height="30",borderwidth=0)
	butc7.place(x=594,y=344)
	#campeon8
	imagec8 = Image.open("champion\\" + (str(campeon8[0]['name'])) + ".png")
	imagec8 = imagec8.resize((30, 30), Image.ANTIALIAS)
	imagec81 = ImageTk.PhotoImage(imagec8)
	butc8=Button(win)
	butc8.config(image=imagec81,width="30",height="30",borderwidth=0)
	butc8.place(x=594,y=379)
	#campeon9
	imagec9 = Image.open("champion\\" + (str(campeon9[0]['name'])) + ".png")
	imagec9 = imagec9.resize((30, 30), Image.ANTIALIAS)
	imagec91 = ImageTk.PhotoImage(imagec9)
	butc9=Button(win)
	butc9.config(image=imagec91,width="30",height="30",borderwidth=0)
	butc9.place(x=594,y=414)
	#campeon5
	imagec10 = Image.open("champion\\" + (str(campeon10[0]['name'])) + ".png")
	imagec10 = imagec10.resize((30, 30), Image.ANTIALIAS)
	imagec101 = ImageTk.PhotoImage(imagec10)
	butc10=Button(win)
	butc10.config(image=imagec101,width="30",height="30",borderwidth=0)
	butc10.place(x=594,y=449)

#########################################
#########################################
#########################################
#########################################
#Champions bans
def baneochamps():
	global ban1
	global ban2
	global ban3
	global ban4
	global ban5
	global ban6
	global ban7
	global ban8
	global ban9
	global ban10
	ban1 = []
	ban2 = []
	ban3 = []
	ban4 = []
	ban5 = []
	ban6 = []
	ban7 = []
	ban8 = []
	ban9 = []
	ban10 = []
	for name in ChampID['data']:
		if 'key' in ChampID['data'][name]:
			for i in range(1,11):
				if ChampID['data'][name]['key'] == str(eval('ba'+(str(i)))):
					(eval('ban'+(str(i)))).append(ChampID['data'][name])

def baneochampsimg():
	global baneo1
	global baneo11
	global butb1
	global baneo2
	global baneo21
	global butb2
	global baneo3
	global baneo31
	global butb3
	global baneo4
	global baneo41
	global butb4
	global baneo5
	global baneo51
	global butb5
	global baneo6
	global baneo61
	global butb6
	global baneo7
	global baneo71
	global butb7
	global baneo8
	global baneo81
	global butb8
	global baneo9
	global baneo91
	global butb9
	global baneo10
	global baneo101
	global butb10
	global rectban1
	global rectban2

	#Rectangulos y texto
	rectban1 = Canvas(win, width=155, height=33)
	rectban1.place(x=93,y=251)
	rectban1.create_rectangle(0, 0, 240, 240, fill="#034691", width=0,outline='#034691')

	rectban2 = Canvas(win, width=155, height=33)
	rectban2.place(x=556,y=251)
	rectban2.create_rectangle(0, 0, 240, 240, fill="#C82300", width=0,outline='#C82300')

	#baneo1
	baneo1 = Image.open("champion\\" + (str(ban1[0]['name'])) + ".png")
	baneo1 = baneo1.resize((25, 25), Image.ANTIALIAS)
	baneo11 = ImageTk.PhotoImage(baneo1)
	butb1=Button(win)
	butb1.config(image=baneo11,width="25",height="25",borderwidth=0)
	butb1.place(x=100,y=256)
	#baneo2
	baneo2 = Image.open("champion\\" + (str(ban2[0]['name'])) + ".png")
	baneo2 = baneo2.resize((25, 25), Image.ANTIALIAS)
	baneo21 = ImageTk.PhotoImage(baneo2)
	butb2=Button(win)
	butb2.config(image=baneo21,width="25",height="25",borderwidth=0)
	butb2.place(x=130,y=256)
	#baneo3
	baneo3 = Image.open("champion\\" + (str(ban3[0]['name'])) + ".png")
	baneo3 = baneo3.resize((25, 25), Image.ANTIALIAS)
	baneo31 = ImageTk.PhotoImage(baneo3)
	butb3=Button(win)
	butb3.config(image=baneo31,width="25",height="25",borderwidth=0)
	butb3.place(x=160,y=256)
	#baneo4
	baneo4 = Image.open("champion\\" + (str(ban4[0]['name'])) + ".png")
	baneo4 = baneo4.resize((25, 25), Image.ANTIALIAS)
	baneo41 = ImageTk.PhotoImage(baneo4)
	butb4=Button(win)
	butb4.config(image=baneo41,width="25",height="25",borderwidth=0)
	butb4.place(x=190,y=256)
	#baneo5
	baneo5 = Image.open("champion\\" + (str(ban5[0]['name'])) + ".png")
	baneo5 = baneo5.resize((25, 25), Image.ANTIALIAS)
	baneo51 = ImageTk.PhotoImage(baneo5)
	butb5=Button(win)
	butb5.config(image=baneo51,width="25",height="25",borderwidth=0)
	butb5.place(x=220,y=256)
	#baneo6
	baneo6 = Image.open("champion\\" + (str(ban6[0]['name'])) + ".png")
	baneo6 = baneo6.resize((25, 25), Image.ANTIALIAS)
	baneo61 = ImageTk.PhotoImage(baneo6)
	butb6=Button(win)
	butb6.config(image=baneo61,width="25",height="25",borderwidth=0)
	butb6.place(x=562,y=256)
	#baneo7
	baneo7 = Image.open("champion\\" + (str(ban7[0]['name'])) + ".png")
	baneo7 = baneo7.resize((25, 25), Image.ANTIALIAS)
	baneo71 = ImageTk.PhotoImage(baneo7)
	butb7=Button(win)
	butb7.config(image=baneo71,width="25",height="25",borderwidth=0)
	butb7.place(x=592,y=256)
	#baneo8
	baneo8 = Image.open("champion\\" + (str(ban8[0]['name'])) + ".png")
	baneo8 = baneo8.resize((25, 25), Image.ANTIALIAS)
	baneo81 = ImageTk.PhotoImage(baneo8)
	butb8=Button(win)
	butb8.config(image=baneo81,width="25",height="25",borderwidth=0)
	butb8.place(x=622,y=256)
	#baneo9
	baneo9 = Image.open("champion\\" + (str(ban9[0]['name'])) + ".png")
	baneo9 = baneo9.resize((25, 25), Image.ANTIALIAS)
	baneo91 = ImageTk.PhotoImage(baneo9)
	butb9=Button(win)
	butb9.config(image=baneo91,width="25",height="25",borderwidth=0)
	butb9.place(x=652,y=256)
	#baneo10
	baneo10 = Image.open("champion\\" + (str(ban10[0]['name'])) + ".png")
	baneo10 = baneo10.resize((25, 25), Image.ANTIALIAS)
	baneo101 = ImageTk.PhotoImage(baneo10)
	butb10=Button(win)
	butb10.config(image=baneo101,width="25",height="25",borderwidth=0)
	butb10.place(x=682,y=256)


#########################################
#########################################
#########################################
#########################################

def etiquetas():
	global label_msg1
	global label_msg2
	global label_msg3
	global label_msg4
	global label_msg5
	global label_msg6
	global label_msg7
	global label_msg8
	global label_msg9
	global label_msg10
	label_msg1 = cv1.create_text((178, 315), text=(str(campeon1[0]['name'])), font="MSGothic 10 bold", fill="#000B4E",anchor=NE)
	label_msg2 = cv1.create_text((178, 350), text=(str(campeon2[0]['name'])), font="MSGothic 10 bold", fill="#000B4E",anchor=NE)
	label_msg3 = cv1.create_text((178, 385), text=(str(campeon3[0]['name'])), font="MSGothic 10 bold", fill="#000B4E",anchor=NE)
	label_msg4 = cv1.create_text((178, 420), text=(str(campeon4[0]['name'])), font="MSGothic 10 bold", fill="#000B4E",anchor=NE)
	label_msg5 = cv1.create_text((178, 455), text=(str(campeon5[0]['name'])), font="MSGothic 10 bold", fill="#000B4E",anchor=NE)
	label_msg6 = cv1.create_text((628, 315), text=(str(campeon6[0]['name'])), font="MSGothic 10 bold", fill="#BE1602",anchor=NW)
	label_msg7 = cv1.create_text((628, 350), text=(str(campeon7[0]['name'])), font="MSGothic 10 bold", fill="#BE1602",anchor=NW)
	label_msg8 = cv1.create_text((628, 385), text=(str(campeon8[0]['name'])), font="MSGothic 10 bold", fill="#BE1602",anchor=NW)
	label_msg9 = cv1.create_text((628, 420), text=(str(campeon9[0]['name'])), font="MSGothic 10 bold", fill="#BE1602",anchor=NW)
	label_msg10 = cv1.create_text((628, 455), text=(str(campeon10[0]['name'])), font="MSGothic 10 bold", fill="#BE1602",anchor=NW)


def champs():
	global campeon1
	global campeon2
	global campeon3
	global campeon4
	global campeon5
	global campeon6
	global campeon7
	global campeon8
	global campeon9
	global campeon10
	campeon1 = []
	campeon2 = []
	campeon3 = []
	campeon4 = []
	campeon5 = []
	campeon6 = []
	campeon7 = []
	campeon8 = []
	campeon9 = []
	campeon10 = []
	for name in ChampID['data']:
		if 'key' in ChampID['data'][name]:
			for i in range(1,11):
				if ChampID['data'][name]['key'] == str(eval('c'+(str(i)))):
					(eval('campeon'+(str(i)))).append(ChampID['data'][name])
					#print(str(eval('campeon'+(str(i))+"[0]['name']")))


#convierte milisegundos en segundos
def convertMinS(millis):
    return (millis/(1000*60))%60



def get_participant_frames(archivo,jugador):
    data = []

    for i in range(len(archivo['frames'])):
        pid = archivo["frames"][i]["participantFrames"][str(jugador)]["participantId"]
        try:
            posx = archivo["frames"][i]["participantFrames"][str(jugador)]["position"]["x"]
        except KeyError:
            posx = archivo["frames"][i - 1]["participantFrames"][str(jugador)]["position"]["x"]
        try:
            posy = archivo["frames"][i]["participantFrames"][str(jugador)]["position"]["y"]
        except KeyError:
            posy = archivo["frames"][i - 1]["participantFrames"][str(jugador)]["position"]["y"]
        try:
            ds = archivo["frames"][i]["participantFrames"][str(jugador)]["dominionScore"]
        except KeyError:
            ds = archivo["frames"][i - 1]["participantFrames"][str(jugador)]["dominionScore"]

        try:
            ts = archivo["frames"][i]["participantFrames"][str(jugador)]["teamScore"]
        except KeyError:
            ts = archivo["frames"][i - 1]["participantFrames"][str(jugador)]["teamScore"]

        cg = archivo["frames"][i]["participantFrames"][str(jugador)]["currentGold"]
        tg = archivo["frames"][i]["participantFrames"][str(jugador)]["totalGold"]
        lvl = archivo["frames"][i]["participantFrames"][str(jugador)]["level"]
        xp = archivo["frames"][i]["participantFrames"][str(jugador)]["xp"]
        mk = archivo["frames"][i]["participantFrames"][str(jugador)]["minionsKilled"]
        jk = archivo["frames"][i]["participantFrames"][str(jugador)]["jungleMinionsKilled"]

        tiem = int(convertMinS(archivo["frames"][i]["timestamp"]))

        data.append([tiem, pid, posx, posy, cg, tg, lvl, xp, mk, jk, ds, ts])

    df = pd.DataFrame(data, columns=("Tiempo", "ID Invocador", "PosicionX", "PosicionY" , "Oro", "Oro Total", "Nivel", "Exp", "CsMinions", "CsJg", "DS", "TS"))

    return df

#-----------------------------
#Summoners

def Summo():
	global Summoner1
	global Summoner2
	global Summoner3
	global Summoner4
	global Summoner5
	global Summoner6
	global Summoner7
	global Summoner8
	global Summoner9
	global Summoner10
	global ID1
	global ID2
	global ID3
	global ID4
	global ID5
	global ID6
	global ID7
	global ID8
	global ID9
	global ID10
	Summoner1 = str(ja1_text.get()) + " : " + (str(campeon1[0]['name']))
	ID1 = MatchID ["participantIdentities"][0]["participantId"]
	Summoner2 = str(ja2_text.get()) + " : " + (str(campeon2[0]['name']))
	ID2 = MatchID ["participantIdentities"][1]["participantId"]
	Summoner3 = str(ja3_text.get()) + " : " + (str(campeon3[0]['name']))
	ID3 = MatchID ["participantIdentities"][2]["participantId"]
	Summoner4 = str(ja4_text.get()) + " : " + (str(campeon4[0]['name']))
	ID4 = MatchID ["participantIdentities"][3]["participantId"]
	Summoner5 = str(ja5_text.get()) + " : " + (str(campeon5[0]['name']))
	ID5 = MatchID ["participantIdentities"][4]["participantId"]
	Summoner6 = str(jr1_text.get()) + " : " + (str(campeon6[0]['name']))
	ID6 = MatchID ["participantIdentities"][5]["participantId"]
	Summoner7 = str(jr2_text.get()) + " : " + (str(campeon7[0]['name']))
	ID7 = MatchID ["participantIdentities"][6]["participantId"]
	Summoner8 = str(jr3_text.get()) + " : " + (str(campeon8[0]['name']))
	ID8 = MatchID ["participantIdentities"][7]["participantId"]
	Summoner9 = str(jr4_text.get()) + " : " + (str(campeon9[0]['name']))
	ID9 = MatchID ["participantIdentities"][8]["participantId"]
	Summoner10 = str(jr5_text.get()) + " : " + (str(campeon10[0]['name']))
	ID10 = MatchID ["participantIdentities"][9]["participantId"]



#-----------------------------
#Carga de DATOS
def add_command():
    datoslolgraphp.insert(ID_text.get(),EA_text.get(),ER_text.get(), ja1_text.get(),ja2_text.get(),ja3_text.get(),ja4_text.get(), ja5_text.get(),jr1_text.get(),jr2_text.get(),jr3_text.get(),jr4_text.get(),jr5_text.get())

    #list.delete(0,END)
    #list.insert(END,(ID_text.get(),EA_text.get(),ER_text.get(), ja1_text.get(), ja1_text.get(),ja2_text.get(),ja3_text.get(),ja4_text.get(), ja5_text.get(),jr1_text.get(),jr2_text.get(),jr3_text.get(),jr4_text.get(),jr5_text.get()))



#-----------------------------
#VENTANA

win = Tk()
win.title('LoLGraph')
win.geometry("800x600")

#------------------------------

#CANVAS

cv1 = Canvas(win,width=800,height=600)
#Fondo
image=ImageTk.PhotoImage(Image.open("background\\lolgraphfondoapp.png"))
cv1.create_image(0,0,anchor=NW,image=image)
cv1.pack()

#LABELS
label_msg = cv1.create_text((400, 180), text="Ingresa el ID de la partida", font="MSGothic 15 bold", fill="#000B4E")
label_msg = cv1.create_text((400, 240), text="Ingresa el nombre de los equipos", font="MSGothic 15 bold", fill="#000B4E")
label_msg = cv1.create_text((405, 270), text="VS", font="MSGothic 15 bold", fill="#000B4E")

#----------------------------
#Listbox
def get_selected_row(event):
	global selected_row
	index = lista.curselection()[0]
	selected_row = lista.get(index)
	en1.delete(0,END)
	en1.insert(END,selected_row[0])
	en2.delete(0,END)
	en2.insert(END,selected_row[1])
	en3.delete(0,END)
	en3.insert(END,selected_row[2])
	ja1.delete(0,END)
	ja1.insert(END,selected_row[3])
	ja2.delete(0,END)
	ja2.insert(END,selected_row[4])
	ja3.delete(0,END)
	ja3.insert(END,selected_row[5])
	ja4.delete(0,END)
	ja4.insert(END,selected_row[6])
	ja5.delete(0,END)
	ja5.insert(END,selected_row[7])
	jr1.delete(0,END)
	jr1.insert(END,selected_row[8])
	jr2.delete(0,END)
	jr2.insert(END,selected_row[9])
	jr3.delete(0,END)
	jr3.insert(END,selected_row[10])
	jr4.delete(0,END)
	jr4.insert(END,selected_row[11])
	jr5.delete(0,END)
	jr5.insert(END,selected_row[12])

#Buscar por palabra clave
def busca_coincidencia():
	search1_term = search1.get()
	lista.delete(0,END)
	try:
		for i in datoslolgraphp.view():
			if search1_term in i:
				lista.insert(END,i)
	except TypeError:
		pass

search1 = StringVar()
searchbox = Entry(win, textvariable=search1,width=15)
searchbox.place(x=240,y=570)

#Ver todas las partidas guardadas
def view_command():
    lista.delete(0,END)
    for row in datoslolgraphp.view():
        lista.insert(END,row)

#Eliminar partida seleccionada
def delete_command():
    datoslolgraphp.delete(selected_row[0])


sb = Scrollbar(win,orient=VERTICAL)

lista = Listbox(win,height=5,width=50,yscrollcommand=sb.set)
lista.place(x=400,y=500)

sb.config(command=lista.yview)
sb.place(x=710,y=500)


lista.bind('<<ListboxSelect>>',get_selected_row)




#----------------------------

#ENTRYS
ID_text = StringVar()
en1 = Entry(win,textvariable=ID_text)
en1.place(x=400,y=205,anchor='center')
en1.config(highlightbackground='#BE1602', highlightcolor='#BE1602')


#color fondo
rect1 = Canvas(win, width=130, height=23)
rect1.place(x=425,y=256)
rect1.create_rectangle(0, 0, 140, 140, fill="red", width=0,outline='red')

rect2 = Canvas(win, width=130, height=23)
rect2.place(x=250,y=256)
rect2.create_rectangle(0, 0, 140, 140, fill="blue", width=0,outline='blue')

EA_text = StringVar()
en2 = Entry(win,textvariable=EA_text)
en2.place(x=255,y=260)

ER_text = StringVar()
en3 = Entry(win,textvariable=ER_text)
en3.place(x=430,y=260)

#equipo azul
ja1_text = StringVar()
ja1 = Entry(win,textvariable=ja1_text)
ja1.place(x=220,y=315)

ja2_text = StringVar()
ja2 = Entry(win,textvariable=ja2_text)
ja2.place(x=220,y=350)

ja3_text = StringVar()
ja3 = Entry(win,textvariable=ja3_text)
ja3.place(x=220,y=385)

ja4_text = StringVar()
ja4 = Entry(win,textvariable=ja4_text)
ja4.place(x=220,y=420)

ja5_text = StringVar()
ja5 = Entry(win,textvariable=ja5_text)
ja5.place(x=220,y=455)

#equipo rojo
jr1_text = StringVar()
jr1 = Entry(win,textvariable=jr1_text)
jr1.place(x=460,y=315)

jr2_text = StringVar()
jr2 = Entry(win,textvariable=jr2_text)
jr2.place(x=460,y=350)

jr3_text = StringVar()
jr3 = Entry(win,textvariable=jr3_text)
jr3.place(x=460,y=385)

jr4_text = StringVar()
jr4 = Entry(win,textvariable=jr4_text)
jr4.place(x=460,y=420)

jr5_text = StringVar()
jr5 = Entry(win,textvariable=jr5_text)
jr5.place(x=460,y=455)

#---------------------------

#DESPLEGABLES
mbut=  Menubutton ( win, text="Region", relief=RAISED, width=8, bd=2 )
mbut.place(x=730, y=20)
mbut.menu =  Menu ( mbut, tearoff = 0 )
mbut["menu"] =  mbut.menu

LASVar = IntVar()
LANVar = IntVar()
BRVar = IntVar()
NASVar = IntVar()
mbut.menu.add_checkbutton ( label="LAS",variable=LASVar )
mbut.menu.add_checkbutton ( label="LAN",variable=LANVar )
mbut.menu.add_checkbutton ( label="BR",variable=BRVar )
mbut.menu.add_checkbutton ( label="NAS",variable=NASVar )

#--------------------------

#BOTONES
bt1= Button(win, text='Busca!', width=5, bd=2,command=buscar)
bt1.place(x=380,y=450)

btg1=Button(win)
btg1photo=PhotoImage(file="button\\lolgraphbtg1.png")
btg1.config(image=btg1photo,width="80",height="60",borderwidth=0,command=graficochamp)
btg1.place(x=10,y=500)

btg2=Button(win)
btg2photo=PhotoImage(file="button\\lolgraphbtg2.png")
btg2.config(image=btg2photo,width="80",height="60",borderwidth=0,command=graficomons)
btg2.place(x=110,y=500)

btg3=Button(win)
btg3photo=PhotoImage(file="button\\lolgraphbtg3.png")
btg3.config(image=btg3photo,width="80",height="60",borderwidth=0,command=graficomap)
btg3.place(x=210,y=500)

btg4=Button(win)
btg4photo=PhotoImage(file="button\\lolgraphbtg4.png")
btg4.config(image=btg4photo,width="80",height="60",borderwidth=0,command=graficoheat)
btg4.place(x=310,y=500)

bt4= Button(win, text='Borrar', width=5, bd=2,command=delete_command)
bt4.place(x=730,y=550)

bt5= Button(win, text='Ver',width=5, bd=2,command=view_command)
bt5.place(x=730,y=510)

bt6= Button(win,text='Lista',width=5, bd=2,command=busca_coincidencia)
bt6.place(x=338,y=568)

#Sereno ID
#id z2ZyzfKUcN41ZORNXFomcAsP2wmUbifOQ9Abf7VE5vAGcvs
#account id ZTc-buPhYBvmU2xA6vZ3o4trCIQl_MWGN4Z0BMwAdS6M5Yc8oBQmjgWC
win.mainloop()

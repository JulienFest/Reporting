import pandas as pd
import numpy as np
import os

def get_data():
    print('Copie le chemin du dossier où se trouve les fichiers...')
    path = input('> ')
    files = os.listdir(path)
    del files[0]

    df_res = pd.read_csv(path + files[0])
    df_par = pd.read_csv(path + files[1])
    df_cop = pd.read_csv(path + files[2])
    df_syn = pd.read_csv(path + files[3])

    print(f'\033[1;35;40mRésidences : {df_res.shape}\n')
    print(f'\033[1;35;40mLots : {df_par.shape}\n')
    print(f'\033[1;35;40mCopropriétaires : {df_cop.shape}\n')
    print(f'\033[1;35;40mSyndics : {df_syn.shape}\n')

    return df_cop, df_par, df_res, df_syn

def get_res_data(df_res):
    df_res['nb_res'] = 1.0
    df_res_new = df_res.groupby(by=df_res['Syndic / Client']).sum()
    return df_res_new

def get_par_data(df_par):
    liste_types_principaux = [
        'Appartement',
        'appart+cave',
        'appartement_t2',
        'appartement_t3',
        'appartement_t4',
        'appartement_t5',
        'appartement_t6',
        'appartement_t7',
        'appart+cave',
        't2',
        't2 meuble',
        't3',
        't3 meuble',
        't3/4',
        't4',
        't4 meuble',
        't5',
        't5 meuble',
        't6',
        't7',
        't8',
        'dup',
        'dupl',
        'duple',
        'duplex',
        'appar',
        'appart',
        'apparte',
        'appartem',
        'apparteme',
        'appartemen',
        'appartement',
        'Local commercial',
        'comm',
        'comme',
        'commer',
        'commerc',
        'commerce',
        'local comm',
        'local commercial',
        'local_ccial',
        'aire de vente',
        'maga',
        'magas',
        'magasi',
        'magasin',
        'Maison',
        'mais',
        'maiso',
        'maison',
        'Studio',
        'cham',
        'chamb',
        'chambr',
        'chambre',
        'stud',
        'studi',
        'studio',
        't1',
        't1 bis',
        'pie',
        'piec',
        'piece',
        'Local professionnel',
        'bure',
        'burea',
        'bureau',
        'bureaux',
        'labo',
        'labor',
        'labora',
        'laborat',
        'laboratoire',
        'café',
        'cafe',
        'lave',
        'laver',
        'laveri',
        'laverie',
        'loca',
        'local',
        'atel',
        'ateli',
        'atelie',
        'atelier',
        'bur',
        'bure',
        'burea',
        'bureau'
        'Bien rural',
        'chale',
        'chalet',
        'Terrain',
        'terr',
        'terrain',
        'Immeuble',
        'immeuble',
        'batiment',
        'bâtiment',
        'bâtimen',
        'bâtime',
        'bâtim',
        'bât',
        'bât.']
    df_par['nb_lots_principaux'] = df_par['Type de lot'].map(lambda x:1.0 if x in liste_types_principaux else 0.0)
    df_par_new = df_par.groupby(by=df_par['Client / Syndic']).sum()
    df_par_new = df_par_new.sort_index()
    return df_par_new

def get_cop_data(df_cop):
    df_cop['nb_copros'] = 1.0
    df_cop['nb_emails'] = df_cop['Email'].map(lambda x:1.0 if pd.notna(x) else 0.0)
    df_cop_new = df_cop.groupby(by=df_cop['Syndic / Client']).sum()
    return df_cop_new

def get_syn_data(df_syn):
    df_syn['clients_dometech'] = df_syn['Client Dometech'].map(lambda x:1.0 if pd.notna(x) else 0.0)
    df_syn_new = df_syn.groupby(by=df_syn['Nom']).sum()
    df_syn_new = df_syn_new.drop(columns=['Nb Résidences', 'Nb Assemblées', 'Client Dometech'])
    return df_syn_new

def get_final_df(df_cop_new, df_syn_new, df_res_new, df_par_new):
    df = df_cop_new.join(df_par_new)
    df = df.join(df_syn_new)
    df = df.join(df_res_new)
    cols = ['nb_copros','nb_res', 'Nb Lots', 'nb_lots_principaux', 'nb_emails', 'Nb Assemblées', 'clients_dometech']
    df = df[cols]
    df = df.rename(columns={'Nb Lots':'nb_lots', 'Nb Assemblées':'nb_assemblées'})

    syn_suppr = [
    '9863940 Canada Inc',
    'AJP Syndic Saint Malo',
    'AKAWAN',
    'ASL Victoria-CFH',
    'Acti Syndic',
    'Alteal',
    'BR',
    'CABINET DUCOS IMMOBILIER',
    'CHARO',
    'CIS Immobilier',
    'CS Pershing',
    'CS desaix',
    'Cabinet J. SOTTO',
    'Century 21',
    'Conseil Syndical',
    'Démo - Seine Gestion & Batim et Fils',
    'FONTENOY IMMOBILIER MARTINIQUE',
    'Folliot',
    'Gerancimo Amiens',
    'Guillemot',
    'Hôpitaux Facultés Immobilier',
    'IMMOTEP',
    'Immobilière du Chateau',
    'Imvesters',
    'Inowai',
    'Keredes Test',
    "L'Orée Verte Immobilier",
    'LES TERRASSES DE DORNACH',
    'Les allées de Balma',
    'MP INVESTISSEMENT',
    'Michaël AMADO',
    'PBBG',
    'RESIDENCES ET PATRIMOINE ',
    'ROSIER MIP',
    'Rohan Néogère',
    'Rosati',
    'SCCDP',
    'SCI KADIM',
    'SCP BLANKENBERG JOBARD',
    'SECRI GESTION',
    'SLPCVM',
    'SOGIRE',
    'SYNDIC COOPERATIF PARADISE VILLAS',
    'Sacclo',
    'SdC Havre du fleuve phase 1',
    'Seguinot Christophe',
    'Sponsorize Sàrl',
    'Syment Demo',
    'Syment Demo EN',
    'Syment Evol',
    'Syment Syndic',
    'Syndic',
    'Syndic de la mort',
    'Synergestion',
    'Twinsys',
    'VACHERAND IMMOBILIER',
    'Vacherand Immobilier',
    'Weiss Asset Management SARL',
    'Y.S. Immobilier',
    'armen',
    'cabinet cadoret immobilier',
    'guy hoquet',
    'limpide immobilier duriez',
    'parcstestephe',
    'tarzania',
    'test',
    'eguimos',
    'SEINE GESTION',
    'Immobilière Buecher ',
    'Cagim sogedim',
    'BATIM & FILS - COPROPRIÉTÉS',
    'Artesia',
    'Artésia'
]
    df = df.drop(syn_suppr)

    df['dometech'] = df['clients_dometech'].map(lambda x:'Oui' if x == 1 else 'Non')
    total = df.sum()
    total.name = 'Total'
    df = df.append(total.transpose())
    df['dometech'].values[81] = ''

    return df.to_csv('/Users/julienfestou/Desktop/Exports_BO/Reporting.csv')

if __name__ == '__main__':
    df_cop, df_par, df_res, df_syn = get_data()
    df_res_new = get_res_data(df_res)
    df_par_new = get_par_data(df_par)
    df_cop_new = get_cop_data(df_cop)
    df_syn_new = get_syn_data(df_syn)
    print("\033[1;33;40m Tous les tableaux ont été récupérés ! \n")
    df = get_final_df(df_cop_new, df_syn_new, df_res_new, df_par_new)

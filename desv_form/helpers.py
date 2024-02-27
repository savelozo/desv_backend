
from datetime import datetime

buttonsLabel = {
  'Casa': ["CH"], 'Auto': ["CA"], 'Quinchito':["CC"], 'Jubilación':[],
  'Inversión':[], 'Ahorro':[], 'Reunificación de deuda':["CC"], 'Comenzar negocio':["CC"]
}

industry_to_group = {
    "Servicios financieros y empresariales": 1,
    "Minería": 1,
    "Servicios Personales": 2,
    "Comercio, Restaurantes y Hoteles": 2,
    "Industria manufacturera": 2,
    "Servicios de vivienda e Inmobiliarios": 3,
    "Construcción": 3,
    "Administración pública": 2,
    "Transporte": 4,
    "Agropecuario": 5,
    "Electricidad, gas, agua y gestión de desechos": 6,
    "Comunicaciones y servicios de información": 7,
    "Pesca": 5
}

def calculate_age(birth_date):
    # Obten la fecha actual
    today = datetime.now()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    
    # Calcula la diferencia de años
    age = today.year - birth_date.year
    
    # Verifica si aún no ha pasado el cumpleaños de la persona este año
    if birth_date.month > today.month or (birth_date.month == today.month and birth_date.day > today.day):
        age -= 1  # Resta un año si no ha pasado el cumpleaños este año
    
    return age

def calculate_specific_value_for_age(age, product):

    weights = {"CH": 0.08,
               "CA": 0.04}
    
    if 18 <= age <= 24:
        if product in ["CH", "CA"]:
            return weights[product] * 0.5
        elif product in ["CC"] and age >= 21:
            return weights[product] * 0.5
        else:
            return 0
    elif 25 <= age <= 35:
        return weights[product] * 0.8
    elif 36 <= age <= 45:
        return weights[product]
    elif 46 <= age <= 55:
        return weights[product] * 0.8
    elif 56 <= age <= 65:
        return weights[product] * 0.2
    else:
        return 0

def get_percentage_by_education_level(education_level, product):
    # Definir un diccionario que asocie las categorías con los porcentajes

    weights = {"CH": 0.08,
             "CC": 0.08}

    percentage_by_level_CH_CC = {
        "Básica Incompleta": 0.01,
        "Básica Completa": 0.02,
        "Media Incompleta": 0.04,
        "Media Completa": 0.2,
        "Téc. Sup. Incompleta": 0.25,
        "Téc. Sup. Completa": 0.45,
        "Profesional Incompleta": 0.55,
        "Profesional Completa": 0.9,
        "Post-Grado Incompleta": 0.95,
        "Post-Grado Completa": 1,
    }

    # Buscar la categoría en el diccionario y obtener el porcentaje
    if product in ["CH","CC"]:
        return weights[product]*percentage_by_level_CH_CC[education_level]
    else:
        return 0

def calculate_specific_value_for_nationality(chilean_nationality, product):

    weights = {"CH": 0.02,
            "CA": 0.01}

    if chilean_nationality is "Sí":
        return weights[product]
    else:
        return 0

def calculate_time_of_employment_status(init_date_employ):
    current_date = datetime.now()
    init_date_employ = datetime.strptime(init_date_employ, "%Y-%m")
    difference = current_date - init_date_employ

    # Calculate the difference in years with decimals
    year_difference = difference.days / 365.25

    return round(year_difference, 2) 

def calculate_percentage_employment_relation(time_of_employment_status, employment_status, product):
    
    weights = {"CH": 0.08,
            "CA": 0.35}

    if employment_status == "Dependent":
        if time_of_employment_status <= 0.5:
            return weights[product] * 0.05
        elif 0.5 < time_of_employment_status <= 1:
            return weights[product] * 0.2
        elif 1 < time_of_employment_status <= 2:
            return weights[product] * 0.7
        elif time_of_employment_status > 2:
            return weights[product]
        else:
            return 0
    elif employment_status == "Independent":
        if time_of_employment_status <= 1:
            return weights[product] * 0.05
        elif 1 < time_of_employment_status <= 3:
            return weights[product] * 0.4
        elif time_of_employment_status > 3:
            return weights[product]
        else:
            return 0
    else:
        return 0

def calculate_percentage_by_income_range(income, product):

    weights = {"CH": 0.25,
                "CA": 0.35}

    income = int(income)
    if product in ["CH","CA","CC"]:
        if income <= 410000:
            if product == "CH" or (income >= 350000 and product in ["CA","CC"]):
                return weights[product] * 0.15
            else:
                return 0
        elif 410000 < income <= 800000:
            return weights[product] * 0.3
        elif 800000 < income <= 1200000:
            return weights[product] * 0.5
        elif 1200000 < income <= 2000000:
            return weights[product] * 0.7
        elif 2000000 < income <= 2500000:
            return weights[product] * 0.85
        else:
            return weights[product]
        

def calculate_percentage_by_industry_group(industry_sector, product):
    group_number = industry_to_group[industry_sector]
    percentages = {
        1: 1,
        2: 0.75,
        3: 0.75,
        4: 0.5,
        5: 0.5,
        6: 0.5,
        7: 0.5
    }

    weights = {"CH": 0.05}
    
    if group_number in percentages:
        return weights[product] * percentages[group_number]
    else:
        return 0

def calculate_assets_percentage(propertyValuation, 
                                vehicleValuation, 
                                savingValuation, 
                                otherAssetsValuation,
                                product):
    
    weights = {"CH": 0.2, 
               "CA": 0.08}
    
    percentage_by_levels_assets = {
        'propertyValuation': {
                              'Rango 1': 0.05,
                              'Rango 2': 0.2,
                              'Rango 3': 0.5,
                              'Rango 4': 1
                              },
        'vehicleValuation': {
                              'Rango 1': 0.05,
                              'Rango 2': 0.2,
                              'Rango 3': 0.5,
                              'Rango 4': 1
                              },
        'savingValuation': {
                              'Rango 1': 0.05,
                              'Rango 2': 0.2,
                              'Rango 3': 0.5,
                              'Rango 4': 1
                            },
        'otherAssetsValuation': {
                              'Rango 1': 0.05,
                              'Rango 2': 0.2,
                              'Rango 3': 0.5,
                              'Rango 4': 1
                            },
    }

    percentages_by_item = {
        'propertyValuation': 0.4,
        'vehicleValuation': 0.1,
        'savingValuation': 0.3,
        'otherAssetsValuation': 0.2,
    }
    
    total_valuations = (percentages_by_item['propertyValuation'] * propertyValuation + 
                        percentages_by_item['vehicleValuation'] * vehicleValuation + 
                        percentages_by_item['savingValuation'] * savingValuation + 
                        percentages_by_item['otherAssetsValuation'] * otherAssetsValuation)
    
    if product in ["CH"]:
        return weights[product] * total_valuations
    elif product in ["CA"]:
        return weights[product] * total_valuations

def calculate_liabilities_percentage(automotiveCommercialConsumptionValuation, 
                                     valuationCreditCardCreditLine,
                                     mortgageCreditValuation, 
                                     rentExpensesValuation,
                                     otherLiabilitiesValuation,
                                     product):
    
    weights = {"CH": 0.2, 
            "CA": 0.02}
    
    
    percentage_by_levels_liabilities = {
        'automotiveCommercialConsumptionValuation': {
                              'Rango 1': 1,
                              'Rango 2': 0.6,
                              'Rango 3': 0.4,
                              'Rango 4': 0.2,
                              'Rango 5': 0.05
                            },
        'valuationCreditCardCreditLine': {
                              'Rango 1': 1,
                              'Rango 2': 0.6,
                              'Rango 3': 0.4,
                              'Rango 4': 0.2,
                              'Rango 5': 0.05
                            },
        'mortgageCreditValuation': {
                              'Rango 1': 1,
                              'Rango 2': 0.6,
                              'Rango 3': 0.4,
                              'Rango 4': 0.2,
                              'Rango 5': 0.05
                            },
        'rentExpensesValuation': {
                              'Rango 1': 1,
                              'Rango 2': 0.6,
                              'Rango 3': 0.4,
                              'Rango 4': 0.2,
                              'Rango 5': 0.05
                            },
        'otherLiabilitiesValuation': {
                              'Rango 1': 1,
                              'Rango 2': 0.6,
                              'Rango 3': 0.4,
                              'Rango 4': 0.2,
                              'Rango 5': 0.05
                            },
    }

    percentages_by_item = {
        'automotiveCommercialConsumptionValuation': 0.15,
        'valuationCreditCardCreditLine': 0.25,
        'mortgageCreditValuation': 0.3,
        'rentExpensesValuation': 0.2,
        'otherLiabilitiesValuation': 0.1
    }

    total_liabilities = (percentages_by_item['automotiveCommercialConsumptionValuation'] * 
                         percentage_by_levels_liabilities['automotiveCommercialConsumptionValuation'][automotiveCommercialConsumptionValuation] + 
                         percentages_by_item['mortgageCreditValuation'] * 
                         percentage_by_levels_liabilities['mortgageCreditValuation'][mortgageCreditValuation] + 
                         percentages_by_item['valuationCreditCardCreditLine'] * 
                         percentage_by_levels_liabilities['valuationCreditCardCreditLine'][valuationCreditCardCreditLine] + 
                         percentages_by_item['rentExpensesValuation'] * 
                         percentage_by_levels_liabilities['rentExpensesValuation'][rentExpensesValuation] +
                         percentages_by_item['otherLiabilitiesValuation'] * 
                         percentage_by_levels_liabilities['otherLiabilitiesValuation'][otherLiabilitiesValuation])
    
    if product in ["CH"]:
        return weights[product] * total_liabilities
    elif product in ["CA"]:
        return weights[product] * total_liabilities

def calculate_index(data):
    #buttonStatus = data.get('buttonsStatus', '')
    name=data.get('firstName', ''),
    last_name=data.get('lastName', ''),
    email=data.get('email', ''),
    date_of_birth=data.get('birthdate', '')
    age = calculate_age(date_of_birth)
    print("Edad: {}".format(age))
    print("$ Edad: {}".format(calculate_specific_value_for_age(age, "CH")))
    nationality=data.get('nationality', ''),
    address=data.get('address', ''),
    education_level=data.get('educationLevel', '')
    print("Nivel de educacion: {}".format(education_level))
    print("% Nivel de educacion: {}".format(get_percentage_by_education_level(education_level, "CH")))
    employment_status=data.get('employmentStatus', '')
    print("Estado laboral: {}".format(employment_status))
    init_date_employ=data.get('init_date_employ', '')
    time_of_employment=calculate_time_of_employment_status(init_date_employ)
    print("Años de relación laboral: {}".format(time_of_employment))
    print("% por relación laboral: {}".format(calculate_percentage_employment_relation(time_of_employment, employment_status,"CH")))
    industry_type=data.get('industry', '')
    print("Tipo de industria: {}".format(industry_type))
    print("% por tipo de industria: {}".format(calculate_percentage_by_industry_group(industry_type,"CH")))
    income=data.get('income', '')
    print("Ingreso promedio mensual: ${}".format(income))
    print("% ingreso: {}".format(calculate_percentage_by_income_range(income,"CH")))
    propertyValuation=data.get('propertyValuation', '')
    vehicleValuation=data.get('vehicleValuation', '')
    savingValuation=data.get('savingValuation', '')
    otherAssetsValuation=data.get('otherAssetsValuation', '')
    automotiveCommercialConsumptionValuation=data.get('automotiveCommercialConsumptionValuation', '')
    valuationCreditCardCreditLine=data.get('valuationCreditCardCreditLine', '')  
    mortgageCreditValuation=data.get('mortgageCreditValuation', '') 
    rentExpensesValuation=data.get('rentExpensesValuation', '')
    otherLiabilitiesValuation=data.get('otherLiabilitiesValuation', '')
    # print("Activos: {}".format(calculate_assets_percentage(propertyValuation, 
    #                             vehicleValuation, 
    #                             savingValuation, 
    #                             otherAssetsValuation,
    #                             "CH")))
    print("Pasivos {}".format(calculate_liabilities_percentage(automotiveCommercialConsumptionValuation, 
                                     valuationCreditCardCreditLine,
                                     mortgageCreditValuation, 
                                     rentExpensesValuation,
                                     otherLiabilitiesValuation,
                                     "CH")))
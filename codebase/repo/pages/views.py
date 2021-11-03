# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Pages
from .models import PagesMonthly
import requests
import json

#Load json into array data
jsonFilePath = 'pages/demographics.json'
f = open(jsonFilePath)
#elements of json file will be in array: data#
data = json.load(f)
f.close()

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

class DeletePageView(TemplateView): 
    template_name = 'delete.html'

class InsertPageView(TemplateView):
    template_name = 'insert.html'

class AnalyticsPageView(TemplateView):
    template_name = 'analytics.html'

class Analytics2PageView(TemplateView):
    template_name = 'analytics2.html'


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context["qs"] = Pages.objects.all()
#     return context


#search method
def results(request):
    input = request.GET['search'] #retrieves the GET for search
    s2= '' #will be our return string
    for i in data:
        if input == i['demographic_value'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '--\n'
        elif input == i['administered_date'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '--\n'
        elif input == i['demographic_category'] :
            s2 = s2 + str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '--\n'
        elif input == str(i['ID']) :
            s2 = str(i['ID']) +' | '+ i['demographic_category'] +' | '+ i['demographic_value'] +' | '+ i['administered_date'] +' | '+ str(i['total_doses']) +' | '+ str(i['cumulative_total_doses']) +' | '+ str(i['pfizer_doses']) +' | '+ str(i['cumulative_pfizer_doses']) +' | '+ str(i['moderna_doses']) +' | '+ str(i['cumulative_moderna_doses']) +' | '+ str(i['jj_doses']) +' | '+ str(i['cumulative_jj_doses']) +' | '+ str(i['partially_vaccinated']) +' | '+ str(i['total_partially_vaccinated']) +' | '+ str(i['fully_vaccinated']) +' | '+ str(i['cumulative_fully_vaccinated']) +' | '+ str(i['at_least_one_dose']) +' | '+ str(i['cumulative_at_least_one_dose']) + '--\n'
            break
    if s2 == '': #basically if empty then no search found
        s2 = "No matching results...pleast try again."
    return render(request,'results.html',{'search':s2})

#delete method
def delete_record(request):
    input = request.GET['delete'] #retrieves the GET for deleting
    s3= '' #will be our return string
    for i in data:
        if input == str(i['ID']) : #this works in terms of getting it to 'delete' everytime surver runs 
            i['ID'] = None        #will not show up in GUI anymore...back end still needs to fix to update json
            i['demographic_category'] = 0
            i['demographic_value']  = 0
            i['administered_date'] = 0
            i['total_doses'] = 0
            i['cumulative_total_doses'] = 0
            i['pfizer_doses'] = 0
            i['cumulative_pfizer_doses'] = 0
            i['moderna_doses'] = 0
            i['cumulative_moderna_doses'] = 0 
            i['jj_doses'] = 0
            i['cumulative_jj_doses'] = 0 
            i['partially_vaccinated'] = 0 
            i['total_partially_vaccinated'] = 0 
            i['fully_vaccinated'] = 0 
            i['cumulative_fully_vaccinated'] = 0 
            i['at_least_one_dose'] = 0 
            i['cumulative_at_least_one_dose'] = 0
            s3 = 'Success. Entry record #' + input + ' has been deleted.'
            break
        elif input != str(i['ID']) :
            s3 = 'Record not found. Please try again.'
    return render(request,'delete.html',{'delete':s3})

#insert method

def insert_record(request):
    inputCat = request.GET['category'] #retrieves Demographic Category
    inputValue = request.GET['value'] #retrieves Demographic Value
    inputDate = request.GET['date']  #retrieves Date
    s3 = '' #return string
    maxIDNum = 0
    for i in data:
        if i['ID'] > maxIDNum:
           maxIDNum = i['ID']
           
    #bam = {"ID" : 3, "demographic_category": "Age Group"}
    newRecord = {"ID": maxIDNum + 1, 
           "demographic_category": inputCat,
           "demographic_value": inputValue,
           "administered_date": inputDate,
           "total_doses": 0,
           "cumulative_total_doses": 0,
           "pfizer_doses": 0,
           "cumulative_pfizer_doses": 0,
           "moderna_doses": 0,
           "cumulative_moderna_doses": 0,
           "jj_doses": 0,
           "cumulative_jj_doses": 0,
           "partially_vaccinated": 0,
           "total_partially_vaccinated": 0,
           "fully_vaccinated": 0,
           "cumulative_fully_vaccinated": 0,
           "at_least_one_dose": 0,
           "cumulative_at_least_one_dose": 0}
    
    data.append(newRecord)
    #jsonArray.append((words[0], words[1:]))
    s3 = 'Record has been successfully added. Thank you.'
    return render(request,'insert.html',{'insert':s3})

#modify method
def modify_record(request):
    inputID = request.GET['recordID'] #retrieves ID
    inputCat = request.GET['category'] #retrieves Demographic Category
    inputValue = request.GET['value'] #retrieves Demographic Value
    inputDate = request.GET['date']  #retrieves Date
    s4= '' #will be our return string
    for i in data:
        if inputID == str(i['ID']) :
            i['demographic_category'] = inputCat
            i['demographic_value']  = inputValue
            i['administered_date'] = inputDate
            s4 = 'Record has been successfully modified. Thank you.'
            break
        else:
            s4 = 'Sorry, record ' + inputID + ' not found. Try again.'
    return render(request,'insert.html',{'modify':s4})

def backup_record(request):
    #input = request.GET['backup']
    jsonString = json.dumps(data)
    jsonFile = open("pages/demographics.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    s5 = 'Record has been successfully backed up. Thank you.'
    return render(request,'home.html',{'backup':s5})

def monthly_vaccination_analytics(request):
    #input = request.GET['monthlyVaccs']
    sm_v_a = 'Chart is made'

    blankEntries = 0

    July20 = 0
    August20 = 0
    September20 = 0
    October20 = 0
    November20 = 0
    December20 = 0

    January21 = 0
    February21 = 0
    March21 = 0
    April21 = 0
    May21 = 0
    June21 = 0
    July21 = 0
    August21 = 0
    September21 = 0
    October21 = 0
    
    currentDate = ""
    currentMonth = ""
    currentDay = ""
    currentYear = ""

    for i in data:
        currentDate = i['administered_date']
        if len(currentDate) != "0":
            currentMonth, currentDay, currentYear = currentDate.split('/')
        else:
            currentMonth = "0"
            currentDay = "0"
            currentYear = "0"
        
        if i['demographic_category'] == 'Gender': #using gender because someone can be white, male, 65+ for example and we would count them three times. This prevents recounting
            if currentMonth == "0":
                blankEntries += i['total_doses']
            elif currentMonth == "1":
                January21 += i['total_doses']
            elif currentMonth == "2":
                February21 += i['total_doses']
            elif currentMonth == "3":
                March21 += i['total_doses']
            elif currentMonth == "4":
                April21 += i['total_doses']
            elif currentMonth == "5":
                May21 += i['total_doses']
            elif currentMonth == "6":
                June21 += i['total_doses']
            elif currentMonth == "7":
                if currentYear == "20":
                    July20 += i['total_doses']
                else:
                    July21 += i['total_doses']
            elif currentMonth == "8":
                if currentYear == "20":
                    August20 += i['total_doses']
                else:
                    August21 += i['total_doses']
            elif currentMonth == "9":
                if currentYear == "20":
                    September20 += i['total_doses']
                else:
                    September21 += i['total_doses']
            elif currentMonth == "10":
                if currentYear == "20":
                    October20 += i['total_doses']
                else:
                    October21 += i['total_doses']
            elif currentMonth == "11":
                if currentYear == "20":
                    November20 += i['total_doses']
                else:
                    November21 += i['total_doses']
            elif currentMonth == "12":
                if currentYear == "20":
                    December20 += i['total_doses']
                else:
                    December21 += i['total_doses']
            else:
                sm_v_a = 'invalid date found'
 
    return render(request, 'analytics.html', {
        'text':sm_v_a,
        'July20':July20,
        'August20':August20,
        'September20':September20,
        'October20':October20,
        'November20':November20,
        'December20':December20,
        'January21':January21,
        'February21':February21,
        'March21':March21,
        'April21':April21,
        'May21':May21,
        'June21':June21,
        'July21':July21,
        'August21':August21,
        'September21':September21,
        'October21':October21
        })

def race_vaccine_analytics(request):
    white_jj = 0
    white_moderna = 0
    white_pfizer = 0

    latino_jj = 0
    latino_moderna = 0
    latino_pfizer = 0

    asian_jj = 0
    asian_moderna = 0
    asian_pfizer = 0

    black_jj = 0
    black_moderna = 0
    black_pfizer = 0

    for i in data:
        if i['demographic_value'] == 'White':
            white_jj += i['jj_doses']
            white_moderna += i['moderna_doses']
            white_pfizer += i['pfizer_doses']
        if i['demographic_value'] == 'Latino':
            latino_jj += i['jj_doses']
            latino_moderna += i['moderna_doses']
            latino_pfizer += i['pfizer_doses']
        if i['demographic_value'] == 'Asian':
            asian_jj += i['jj_doses']
            asian_moderna += i['moderna_doses']
            asian_pfizer += i['pfizer_doses']
        if i['demographic_value'] == 'Black or African American':
            black_jj += i['jj_doses']
            black_moderna += i['moderna_doses']
            black_pfizer += i['pfizer_doses'] 

    total_jj = white_jj + latino_jj + asian_jj + black_jj
    total_moderna = white_moderna + latino_moderna + asian_moderna + black_moderna
    total_pfizer = white_pfizer + latino_pfizer + asian_pfizer + black_pfizer

    s6 = 'Chart is made'
    return render(request, 'analytics.html', {
        'race':s6,
        'white_jj':white_jj,
        'white_moderna':white_moderna,
        'white_pfizer':white_pfizer,
        'latino_jj':latino_jj,
        'latino_moderna':latino_moderna,
        'latino_pfizer':latino_pfizer,
        'asian_jj':asian_jj,
        'asian_moderna':asian_moderna,
        'asian_pfizer':asian_pfizer,
        'black_jj':black_jj,
        'black_moderna':black_moderna,
        'black_pfizer':black_pfizer,
        'total_jj':total_jj,
        'total_moderna':total_moderna,
        'total_pfizer':total_pfizer
        })

def mfpiechart(request):
    maleVacc = 0
    femVacc = 0
    otherVacc= 0
    for i in data:
        if i['demographic_value'] == 'Male': 
            maleVacc+= i['total_doses']
        elif i['demographic_value'] == 'Female': 
            femVacc+= i['total_doses']
        elif i['demographic_value'] == 'Unknown/undifferentiated': 
            otherVacc+= i['total_doses']

    return render(request, 'analytics.html', {
        'maleVacc':maleVacc,
        'femVacc':femVacc,
        'otherVacc':otherVacc
        })

def fully_vaccinated_analytics(request):
    overallFullVacc = 0
    overallPartVacc = 0

    maleFullVacc = 0
    malePartVacc = 0

    femFullVacc = 0
    femPartVacc = 0

    otherPartVacc = 0
    otherFullVacc = 0

    for i in data:
        if i['demographic_category'] == 'Gender':
            overallFullVacc += i['fully_vaccinated']
            overallPartVacc += i['at_least_one_dose'] #need to use at_least_one_dose parameter to accurately count jj doses with the others

        if i['demographic_value'] == 'Male': 
            maleFullVacc += i['fully_vaccinated']
            malePartVacc += i['at_least_one_dose']
        elif i['demographic_value'] == 'Female': 
            femFullVacc += i['fully_vaccinated']
            femPartVacc += i['at_least_one_dose']
        elif i['demographic_value'] == 'Unknown/undifferentiated': 
            otherFullVacc += i['fully_vaccinated']
            otherPartVacc += i['at_least_one_dose']

    return render(request, 'analytics.html', {
        'overallFullVacc':overallFullVacc,
        'overallPartVacc':overallPartVacc,
        'maleFullVacc':maleFullVacc,
        'malePartVacc':malePartVacc,
        'femFullVacc':femFullVacc,
        'femPartVacc':femPartVacc,
        'otherPartVacc':otherPartVacc,
        'otherFullVacc':otherFullVacc
        })

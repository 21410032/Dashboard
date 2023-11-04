from django.shortcuts import render
from .models import jsondata

# Create your views here.
def base_view(request):
    book=jsondata.objects.all()
    intensities = [i.intensity for i in book]
    Likelihood= [i.likelihood for i in book]
    Relevance= [i.relevance for i in book]
    Year= [i.end_year for i in book]
    Country= [i.country for i in book]
    Topics= [i.topic for i in book]
    Region= [i.region for i in book]
    City = [i.region for i in book]


    context = {
        'intensities': intensities,
        'Likelihood':Likelihood,
        'Relevance':Relevance,
        'Year':Year,
        'Country':Country,
        'Topics':Topics,
        'Region':Region,
        'City' :City,

    }
    context={
        'book':book
    }
    return render(request,'base.html',context=context)

from django.shortcuts import render
from collections import Counter



def dash_view(request):
    book=jsondata.objects.all()
    intensities = [i.intensity for i in book]
    Likelihood= [i.likelihood for i in book]
    Relevance= [i.relevance for i in book]
    Year= [i.end_year for i in book]
    Country= [i.country for i in book]
    Topics= [i.topic for i in book]
    Region= [i.region for i in book]
    City = [i.region for i in book]
    intensities_counts = dict(Counter(intensities))
    Likelihood_counts = dict(Counter(Likelihood))
    Relevance_counts = dict(Counter(Relevance))
    Year_counts = dict(Counter(Year))
    Country_counts = dict(Counter(Country))
    Topics_counts = dict(Counter(Topics))
    Region_counts = dict(Counter(Region))
    City_counts = dict(Counter(City))
    unique_numbers_intensities_counts                         = list(intensities_counts.keys())
    count_of_numbers_intensities_counts                       = list(intensities_counts.values())
    unique_numbers_Likelihood_counts                       = list(Likelihood_counts.keys())
    count_of_numbers_Likelihood_counts                       = list(Likelihood_counts.values())
    unique_numbers_Relevance_counts                       = list(Relevance_counts.keys())
    count_of_numbers_Relevance_counts                       = list(Relevance_counts.values())
    unique_numbers_Year_counts                       = list(Year_counts.keys())
    count_of_numbers_Year_counts                       = list(Year_counts.values())
    unique_numbers_Country_counts                       = list(Country_counts.keys())
    count_of_numbers_Country_counts                       = list(Country_counts.values())
    unique_numbers_Topics_counts                       = list(Topics_counts.keys())
    count_of_numbers_Topics_counts                      = list(Topics_counts.values())
    unique_numbers_Region_counts                       = list(Region_counts.keys())
    count_of_numbers_Region_counts                       = list(Region_counts.values())
    unique_numbers_City_counts                      = list(City_counts.keys())
    count_of_numbers_City_counts                       = list(City_counts.values())
    
    string_numbers_unique_numbers_intensities_counts =[str(num) for num in unique_numbers_intensities_counts]
    string_numbers_unique_numbers_Likelihood_counts  =[str(num) for num in unique_numbers_Likelihood_counts]
    string_numbers_unique_numbers_Relevance_counts   =[str(num) for num in unique_numbers_Relevance_counts]
    string_numbers_unique_numbers_Year_counts        =[str(num) for num in unique_numbers_Year_counts]
    string_numbers_unique_numbers_Country_counts     =[str(num) for num in unique_numbers_Country_counts]
    string_numbers_unique_numbers_Topics_counts      =[str(num) for num in unique_numbers_Topics_counts]
    string_numbers_unique_numbers_Region_counts      =[str(num) for num in unique_numbers_Region_counts]
    string_numbers_unique_numbers_City_counts        =[str(num) for num in unique_numbers_City_counts]
    
    
    context={
        'book':book
    }
    context = {
        'intensities': intensities,
        'Likelihood':Likelihood,
        'Relevance'              :Relevance,
        'Year'              :Year,
        'Country'              :Country,
        'Topics'              :Topics,
        'Region'              :Region,
        'City'               :City,
        'unique_numbers_intensities_counts  ':unique_numbers_intensities_counts  ,
        'count_of_numbers_intensities_counts':count_of_numbers_intensities_counts,
        'unique_numbers_Likelihood_counts   ':unique_numbers_Likelihood_counts   ,
        'count_of_numbers_Likelihood_counts ':count_of_numbers_Likelihood_counts ,
        'unique_numbers_Relevance_counts    ':unique_numbers_Relevance_counts    ,
        'count_of_numbers_Relevance_counts  ':count_of_numbers_Relevance_counts  ,
        'unique_numbers_Year_counts         ':unique_numbers_Year_counts         ,
        'count_of_numbers_Year_counts       ':count_of_numbers_Year_counts       ,
        'unique_numbers_Country_counts      ':unique_numbers_Country_counts      ,
        'count_of_numbers_Country_counts    ':count_of_numbers_Country_counts    ,
        'unique_numbers_Topics_counts       ':unique_numbers_Topics_counts       ,
        'count_of_numbers_Topics_counts     ':count_of_numbers_Topics_counts     ,
        'unique_numbers_Region_counts       ':unique_numbers_Region_counts       ,
        'count_of_numbers_Region_counts     ':count_of_numbers_Region_counts     ,
        'unique_numbers_City_counts         ':unique_numbers_City_counts         ,
        'count_of_numbers_City_counts       ':count_of_numbers_City_counts       ,
        'string_numbers_unique_numbers_intensities_counts':string_numbers_unique_numbers_intensities_counts,
        'string_numbers_unique_numbers_Likelihood_counts ':string_numbers_unique_numbers_Likelihood_counts ,
        'string_numbers_unique_numbers_Relevance_counts  ':string_numbers_unique_numbers_Relevance_counts  ,
        'string_numbers_unique_numbers_Year_counts       ':string_numbers_unique_numbers_Year_counts       ,
        'string_numbers_unique_numbers_Country_counts    ':string_numbers_unique_numbers_Country_counts    ,
        'string_numbers_unique_numbers_Topics_counts     ':string_numbers_unique_numbers_Topics_counts     ,
        'string_numbers_unique_numbers_Region_counts     ':string_numbers_unique_numbers_Region_counts     ,
        'string_numbers_unique_numbers_City_counts       ':string_numbers_unique_numbers_City_counts       ,


    }
    print(string_numbers_unique_numbers_Likelihood_counts)
    return render(request,'dashboard.html',context=context)

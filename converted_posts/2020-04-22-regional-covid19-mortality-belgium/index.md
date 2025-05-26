---
title: regional covid19 mortality belgium
date: 2020-04-22
created_at: 2020-04-22T10:44:22.941081
last_modified: 2020-04-22T10:44:22.941087
---
# Regional covid-19 mortality in Belgium per gender and age
> Combines the mortality number of the last 10 year with those of covid-19 this year.
- toc:true
- branch: master
- badges: true
- comments: true
- author: Lode Nachtergaele
- categories: [cast42, jupyter, covid19, Belgium, altair]


```
# Import pandas for data wrangling and Altair for plotting
import pandas as pd
import altair as alt
```


```
df_tot_sc = pd.read_excel('https://epistat.sciensano.be/Data/COVID19BE.xlsx')
```


```
df_inhab = pd.read_excel('https://statbel.fgov.be/sites/default/files/files/opendata/bevolking%20naar%20woonplaats%2C%20nationaliteit%20burgelijke%20staat%20%2C%20leeftijd%20en%20geslacht/TF_SOC_POP_STRUCT_2019.xlsx')
```


```
df_inhab
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CD_REFNIS</th>
      <th>TX_DESCR_NL</th>
      <th>TX_DESCR_FR</th>
      <th>CD_DSTR_REFNIS</th>
      <th>TX_ADM_DSTR_DESCR_NL</th>
      <th>TX_ADM_DSTR_DESCR_FR</th>
      <th>CD_PROV_REFNIS</th>
      <th>TX_PROV_DESCR_NL</th>
      <th>TX_PROV_DESCR_FR</th>
      <th>CD_RGN_REFNIS</th>
      <th>TX_RGN_DESCR_NL</th>
      <th>TX_RGN_DESCR_FR</th>
      <th>CD_SEX</th>
      <th>CD_NATLTY</th>
      <th>TX_NATLTY_NL</th>
      <th>TX_NATLTY_FR</th>
      <th>CD_CIV_STS</th>
      <th>TX_CIV_STS_NL</th>
      <th>TX_CIV_STS_FR</th>
      <th>CD_AGE</th>
      <th>MS_POPULATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>69</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>80</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>M</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>30</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>48</td>
      <td>26</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>76</td>
      <td>2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>463376</th>
      <td>93090</td>
      <td>Viroinval</td>
      <td>Viroinval</td>
      <td>93000</td>
      <td>Arrondissement Philippeville</td>
      <td>Arrondissement de Philippeville</td>
      <td>90000.0</td>
      <td>Provincie Namen</td>
      <td>Province de Namur</td>
      <td>3000</td>
      <td>Waals Gewest</td>
      <td>Région wallonne</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>3</td>
      <td>Weduwstaat</td>
      <td>Veuf</td>
      <td>73</td>
      <td>10</td>
    </tr>
    <tr>
      <th>463377</th>
      <td>93090</td>
      <td>Viroinval</td>
      <td>Viroinval</td>
      <td>93000</td>
      <td>Arrondissement Philippeville</td>
      <td>Arrondissement de Philippeville</td>
      <td>90000.0</td>
      <td>Provincie Namen</td>
      <td>Province de Namur</td>
      <td>3000</td>
      <td>Waals Gewest</td>
      <td>Région wallonne</td>
      <td>M</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>3</td>
      <td>Weduwstaat</td>
      <td>Veuf</td>
      <td>64</td>
      <td>1</td>
    </tr>
    <tr>
      <th>463378</th>
      <td>93090</td>
      <td>Viroinval</td>
      <td>Viroinval</td>
      <td>93000</td>
      <td>Arrondissement Philippeville</td>
      <td>Arrondissement de Philippeville</td>
      <td>90000.0</td>
      <td>Provincie Namen</td>
      <td>Province de Namur</td>
      <td>3000</td>
      <td>Waals Gewest</td>
      <td>Région wallonne</td>
      <td>M</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>3</td>
      <td>Weduwstaat</td>
      <td>Veuf</td>
      <td>86</td>
      <td>3</td>
    </tr>
    <tr>
      <th>463379</th>
      <td>93090</td>
      <td>Viroinval</td>
      <td>Viroinval</td>
      <td>93000</td>
      <td>Arrondissement Philippeville</td>
      <td>Arrondissement de Philippeville</td>
      <td>90000.0</td>
      <td>Provincie Namen</td>
      <td>Province de Namur</td>
      <td>3000</td>
      <td>Waals Gewest</td>
      <td>Région wallonne</td>
      <td>M</td>
      <td>ETR</td>
      <td>niet-Belgen</td>
      <td>non-Belges</td>
      <td>3</td>
      <td>Weduwstaat</td>
      <td>Veuf</td>
      <td>74</td>
      <td>1</td>
    </tr>
    <tr>
      <th>463380</th>
      <td>93090</td>
      <td>Viroinval</td>
      <td>Viroinval</td>
      <td>93000</td>
      <td>Arrondissement Philippeville</td>
      <td>Arrondissement de Philippeville</td>
      <td>90000.0</td>
      <td>Provincie Namen</td>
      <td>Province de Namur</td>
      <td>3000</td>
      <td>Waals Gewest</td>
      <td>Région wallonne</td>
      <td>M</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>3</td>
      <td>Weduwstaat</td>
      <td>Veuf</td>
      <td>52</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>463381 rows × 21 columns</p>
</div>




```
inhab_provence = df_inhab['TX_PROV_DESCR_NL'].dropna().unique()
inhab_provence
```




    array(['Provincie Antwerpen', 'Provincie Vlaams-Brabant',
           'Provincie Waals-Brabant', 'Provincie West-Vlaanderen',
           'Provincie Oost-Vlaanderen', 'Provincie Henegouwen',
           'Provincie Luik', 'Provincie Limburg', 'Provincie Luxemburg',
           'Provincie Namen'], dtype=object)




```
sc_provence = df_tot_sc['PROVINCE'].unique()
sc_provence
```




    array(['Brussels', 'Liège', 'Limburg', 'OostVlaanderen', 'VlaamsBrabant',
           'Antwerpen', 'WestVlaanderen', 'BrabantWallon', 'Hainaut', 'Namur',
           nan, 'Luxembourg'], dtype=object)




```
[p.split()[1] for p in inhab_provence]
```




    ['Antwerpen',
     'Vlaams-Brabant',
     'Waals-Brabant',
     'West-Vlaanderen',
     'Oost-Vlaanderen',
     'Henegouwen',
     'Luik',
     'Limburg',
     'Luxemburg',
     'Namen']




```
map_statbel_provence_to_sc_provence = {'Provincie Antwerpen':'Antwerpen', 'Provincie Vlaams-Brabant':'VlaamsBrabant',
       'Provincie Waals-Brabant':'BrabantWallon', 'Provincie West-Vlaanderen':'WestVlaanderen',
       'Provincie Oost-Vlaanderen':'OostVlaanderen', 'Provincie Henegouwen':'Hainaut',
       'Provincie Luik':'Liège', 'Provincie Limburg':'Limburg', 'Provincie Luxemburg':'Luxembourg',
       'Provincie Namen':'Namur'}
```


```
df_inhab['sc_provence'] = df_inhab['TX_PROV_DESCR_NL'].map(map_statbel_provence_to_sc_provence)
```


```
df_tot_sc['AGEGROUP'].unique()
```




    array(['10-19', '20-29', '30-39', '40-49', '50-59', '70-79', '60-69',
           '0-9', '90+', '80-89', nan], dtype=object)




```
df_inhab['AGEGROUP'] =pd.cut(df_inhab['CD_AGE'], bins=[0,10,20,30,40,50,60,70,80,90,200], labels=['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90+'], include_lowest=True)
```


```
df_inhab_gender_prov = df_inhab.groupby(['sc_provence', 'CD_SEX', 'AGEGROUP'])['MS_POPULATION'].sum().reset_index()
```


```
df_inhab_gender_prov_cases = pd.merge(df_inhab_gender_prov, df_tot_sc.dropna(), left_on=['sc_provence', 'AGEGROUP', 'CD_SEX'], right_on=['PROVINCE', 'AGEGROUP', 'SEX'])
```


```
df_inhab_gender_prov_cases.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sc_provence</th>
      <th>CD_SEX</th>
      <th>AGEGROUP</th>
      <th>MS_POPULATION</th>
      <th>DATE</th>
      <th>PROVINCE</th>
      <th>REGION</th>
      <th>SEX</th>
      <th>CASES</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Antwerpen</td>
      <td>F</td>
      <td>0-9</td>
      <td>113851</td>
      <td>2020-03-05</td>
      <td>Antwerpen</td>
      <td>Flanders</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Antwerpen</td>
      <td>F</td>
      <td>0-9</td>
      <td>113851</td>
      <td>2020-03-18</td>
      <td>Antwerpen</td>
      <td>Flanders</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Antwerpen</td>
      <td>F</td>
      <td>0-9</td>
      <td>113851</td>
      <td>2020-03-26</td>
      <td>Antwerpen</td>
      <td>Flanders</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Antwerpen</td>
      <td>F</td>
      <td>0-9</td>
      <td>113851</td>
      <td>2020-03-30</td>
      <td>Antwerpen</td>
      <td>Flanders</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Antwerpen</td>
      <td>F</td>
      <td>0-9</td>
      <td>113851</td>
      <td>2020-04-03</td>
      <td>Antwerpen</td>
      <td>Flanders</td>
      <td>F</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```
df_plot = df_inhab_gender_prov_cases.groupby(['SEX', 'AGEGROUP', 'PROVINCE']).agg(CASES = ('CASES', 'sum'), MS_POPULATION=('MS_POPULATION', 'first')).reset_index()
df_plot
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SEX</th>
      <th>AGEGROUP</th>
      <th>PROVINCE</th>
      <th>CASES</th>
      <th>MS_POPULATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>0-9</td>
      <td>Antwerpen</td>
      <td>9</td>
      <td>113851</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>0-9</td>
      <td>BrabantWallon</td>
      <td>3</td>
      <td>23744</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>0-9</td>
      <td>Hainaut</td>
      <td>11</td>
      <td>81075</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>0-9</td>
      <td>Limburg</td>
      <td>11</td>
      <td>48102</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>0-9</td>
      <td>Liège</td>
      <td>19</td>
      <td>67479</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>195</th>
      <td>M</td>
      <td>90+</td>
      <td>Luxembourg</td>
      <td>17</td>
      <td>469</td>
    </tr>
    <tr>
      <th>196</th>
      <td>M</td>
      <td>90+</td>
      <td>Namur</td>
      <td>27</td>
      <td>827</td>
    </tr>
    <tr>
      <th>197</th>
      <td>M</td>
      <td>90+</td>
      <td>OostVlaanderen</td>
      <td>102</td>
      <td>3105</td>
    </tr>
    <tr>
      <th>198</th>
      <td>M</td>
      <td>90+</td>
      <td>VlaamsBrabant</td>
      <td>129</td>
      <td>2611</td>
    </tr>
    <tr>
      <th>199</th>
      <td>M</td>
      <td>90+</td>
      <td>WestVlaanderen</td>
      <td>121</td>
      <td>3292</td>
    </tr>
  </tbody>
</table>
<p>200 rows × 5 columns</p>
</div>




```
df_plot['PROVINCE'].unique()
```




    array(['Antwerpen', 'BrabantWallon', 'Hainaut', 'Limburg', 'Liège',
           'Luxembourg', 'Namur', 'OostVlaanderen', 'VlaamsBrabant',
           'WestVlaanderen'], dtype=object)




```
alt.Chart(df_plot).mark_bar().encode(x='AGEGROUP:N', y='CASES', color='SEX:N', column='PROVINCE:N')
```





<div id="altair-viz-886320b6e1244ff3b5e3263d78744d40"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-886320b6e1244ff3b5e3263d78744d40") {
      outputDiv = document.getElementById("altair-viz-886320b6e1244ff3b5e3263d78744d40");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-29d222b951085bbf99de7ab1bfa9a22c"}, "mark": "bar", "encoding": {"color": {"type": "nominal", "field": "SEX"}, "column": {"type": "nominal", "field": "PROVINCE"}, "x": {"type": "nominal", "field": "AGEGROUP"}, "y": {"type": "quantitative", "field": "CASES"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-29d222b951085bbf99de7ab1bfa9a22c": [{"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 9, "MS_POPULATION": 113851}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 3, "MS_POPULATION": 23744}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 11, "MS_POPULATION": 81075}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 48102}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 19, "MS_POPULATION": 67479}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 3, "MS_POPULATION": 17834}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 4, "MS_POPULATION": 29270}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 7, "MS_POPULATION": 88120}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 9, "MS_POPULATION": 69061}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 7, "MS_POPULATION": 63579}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 26, "MS_POPULATION": 97741}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 5, "MS_POPULATION": 24368}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 18, "MS_POPULATION": 78804}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 21, "MS_POPULATION": 43943}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 22, "MS_POPULATION": 62761}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 10, "MS_POPULATION": 17617}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 5, "MS_POPULATION": 28987}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 38, "MS_POPULATION": 79353}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 22, "MS_POPULATION": 64641}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 25, "MS_POPULATION": 59104}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 299, "MS_POPULATION": 114364}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 58, "MS_POPULATION": 23892}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 257, "MS_POPULATION": 80946}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 294, "MS_POPULATION": 49202}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 339, "MS_POPULATION": 70284}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 75, "MS_POPULATION": 17671}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 106, "MS_POPULATION": 30639}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 318, "MS_POPULATION": 92829}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 230, "MS_POPULATION": 67228}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 311, "MS_POPULATION": 67252}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 342, "MS_POPULATION": 120901}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 78, "MS_POPULATION": 24455}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 401, "MS_POPULATION": 83728}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 322, "MS_POPULATION": 55322}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 465, "MS_POPULATION": 70295}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 95, "MS_POPULATION": 17849}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 116, "MS_POPULATION": 31144}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 324, "MS_POPULATION": 97907}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 246, "MS_POPULATION": 72520}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 316, "MS_POPULATION": 68094}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 348, "MS_POPULATION": 117869}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 103, "MS_POPULATION": 28346}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 457, "MS_POPULATION": 90877}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 372, "MS_POPULATION": 57203}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 453, "MS_POPULATION": 71565}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 93, "MS_POPULATION": 18961}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 152, "MS_POPULATION": 32384}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 450, "MS_POPULATION": 99714}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 362, "MS_POPULATION": 77657}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 385, "MS_POPULATION": 73584}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 419, "MS_POPULATION": 129704}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 93, "MS_POPULATION": 29056}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 413, "MS_POPULATION": 93332}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 472, "MS_POPULATION": 66159}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 440, "MS_POPULATION": 76876}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 84, "MS_POPULATION": 19137}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 128, "MS_POPULATION": 34850}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 474, "MS_POPULATION": 105453}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 387, "MS_POPULATION": 81649}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 470, "MS_POPULATION": 85817}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 227, "MS_POPULATION": 105349}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 54, "MS_POPULATION": 24653}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 212, "MS_POPULATION": 84127}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 221, "MS_POPULATION": 55216}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 243, "MS_POPULATION": 66973}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 49, "MS_POPULATION": 15653}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 47, "MS_POPULATION": 30550}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 207, "MS_POPULATION": 86777}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 177, "MS_POPULATION": 65934}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 190, "MS_POPULATION": 77019}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 303, "MS_POPULATION": 77129}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 46, "MS_POPULATION": 16999}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 273, "MS_POPULATION": 54498}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 280, "MS_POPULATION": 36984}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 298, "MS_POPULATION": 45051}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 9923}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 78, "MS_POPULATION": 19409}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 278, "MS_POPULATION": 64518}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 205, "MS_POPULATION": 47305}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 262, "MS_POPULATION": 60688}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 627, "MS_POPULATION": 49568}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 100, "MS_POPULATION": 9920}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 572, "MS_POPULATION": 34639}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 626, "MS_POPULATION": 22709}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 659, "MS_POPULATION": 28095}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 151, "MS_POPULATION": 6857}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 204, "MS_POPULATION": 12219}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 687, "MS_POPULATION": 43514}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 550, "MS_POPULATION": 31804}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 638, "MS_POPULATION": 39736}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 388, "MS_POPULATION": 9763}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 66, "MS_POPULATION": 2250}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 330, "MS_POPULATION": 8030}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 355, "MS_POPULATION": 3938}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 352, "MS_POPULATION": 5838}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 81, "MS_POPULATION": 1447}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 104, "MS_POPULATION": 2672}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 392, "MS_POPULATION": 8570}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 346, "MS_POPULATION": 6362}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 360, "MS_POPULATION": 8230}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 24, "MS_POPULATION": 119457}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 1, "MS_POPULATION": 24910}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 13, "MS_POPULATION": 85344}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 7, "MS_POPULATION": 50436}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 17, "MS_POPULATION": 70112}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 2, "MS_POPULATION": 18737}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 2, "MS_POPULATION": 30497}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 8, "MS_POPULATION": 92147}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 8, "MS_POPULATION": 72250}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 9, "MS_POPULATION": 66786}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 18, "MS_POPULATION": 102852}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 4, "MS_POPULATION": 25686}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 10, "MS_POPULATION": 82404}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 46386}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 15, "MS_POPULATION": 65391}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 5, "MS_POPULATION": 18572}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 7, "MS_POPULATION": 30126}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 6, "MS_POPULATION": 83108}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 32, "MS_POPULATION": 67462}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 15, "MS_POPULATION": 62137}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 84, "MS_POPULATION": 115579}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 30, "MS_POPULATION": 24810}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 81, "MS_POPULATION": 83150}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 103, "MS_POPULATION": 50634}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 124, "MS_POPULATION": 70573}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 32, "MS_POPULATION": 18821}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 37, "MS_POPULATION": 31562}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 105, "MS_POPULATION": 93998}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 81, "MS_POPULATION": 68028}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 105, "MS_POPULATION": 71055}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 140, "MS_POPULATION": 121528}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 35, "MS_POPULATION": 23581}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 117, "MS_POPULATION": 83704}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 97, "MS_POPULATION": 55582}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 159, "MS_POPULATION": 70086}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 54, "MS_POPULATION": 18359}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 48, "MS_POPULATION": 31373}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 144, "MS_POPULATION": 98604}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 107, "MS_POPULATION": 70303}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 107, "MS_POPULATION": 71014}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 206, "MS_POPULATION": 121067}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 26621}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 196, "MS_POPULATION": 91355}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 193, "MS_POPULATION": 58026}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 235, "MS_POPULATION": 72725}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 66, "MS_POPULATION": 19512}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 67, "MS_POPULATION": 32462}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 216, "MS_POPULATION": 102816}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 158, "MS_POPULATION": 76199}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 150, "MS_POPULATION": 76238}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 350, "MS_POPULATION": 132717}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 69, "MS_POPULATION": 27611}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 243, "MS_POPULATION": 91404}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 297, "MS_POPULATION": 68198}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 289, "MS_POPULATION": 75997}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 19737}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 83, "MS_POPULATION": 34203}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 323, "MS_POPULATION": 108042}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 262, "MS_POPULATION": 81771}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 308, "MS_POPULATION": 88775}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 370, "MS_POPULATION": 104236}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 21864}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 280, "MS_POPULATION": 75054}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 274, "MS_POPULATION": 55339}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 62795}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 64, "MS_POPULATION": 15101}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 85, "MS_POPULATION": 28668}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 251, "MS_POPULATION": 84501}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 241, "MS_POPULATION": 63019}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 236, "MS_POPULATION": 75047}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 371, "MS_POPULATION": 67535}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 13892}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 288, "MS_POPULATION": 41795}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 353, "MS_POPULATION": 33651}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 288, "MS_POPULATION": 35865}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 69, "MS_POPULATION": 8340}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 64, "MS_POPULATION": 15628}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 257, "MS_POPULATION": 55194}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 225, "MS_POPULATION": 40155}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 269, "MS_POPULATION": 52423}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 410, "MS_POPULATION": 32894}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 57, "MS_POPULATION": 6132}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 246, "MS_POPULATION": 17698}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 377, "MS_POPULATION": 15492}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 16297}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 79, "MS_POPULATION": 4041}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 109, "MS_POPULATION": 6855}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 375, "MS_POPULATION": 26794}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 310, "MS_POPULATION": 20216}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 357, "MS_POPULATION": 25926}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 142, "MS_POPULATION": 3882}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 26, "MS_POPULATION": 809}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 92, "MS_POPULATION": 2277}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 148, "MS_POPULATION": 1526}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 92, "MS_POPULATION": 1934}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 17, "MS_POPULATION": 469}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 27, "MS_POPULATION": 827}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 102, "MS_POPULATION": 3105}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 129, "MS_POPULATION": 2611}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 121, "MS_POPULATION": 3292}]}}, {"mode": "vega-lite"});
</script>




```
df_plot['percentage'] = df_plot['CASES'] / df_plot['MS_POPULATION']
```


```
alt.Chart(df_plot).mark_bar().encode(x='AGEGROUP:N', y='percentage', color='SEX:N', column='PROVINCE:N')
```





<div id="altair-viz-2366eac619714ef6a8d8402921470a5d"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-2366eac619714ef6a8d8402921470a5d") {
      outputDiv = document.getElementById("altair-viz-2366eac619714ef6a8d8402921470a5d");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-8c4256b2c33a1fca2a5d94ca31a38873"}, "mark": "bar", "encoding": {"color": {"type": "nominal", "field": "SEX"}, "column": {"type": "nominal", "field": "PROVINCE"}, "x": {"type": "nominal", "field": "AGEGROUP"}, "y": {"type": "quantitative", "field": "percentage"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-8c4256b2c33a1fca2a5d94ca31a38873": [{"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 9, "MS_POPULATION": 113851, "percentage": 7.90506890585063e-05}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 3, "MS_POPULATION": 23744, "percentage": 0.0001263477088948787}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 11, "MS_POPULATION": 81075, "percentage": 0.0001356768424298489}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 48102, "percentage": 0.00022868072013637687}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 19, "MS_POPULATION": 67479, "percentage": 0.0002815690807510485}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 3, "MS_POPULATION": 17834, "percentage": 0.000168218010541662}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 4, "MS_POPULATION": 29270, "percentage": 0.0001366586949094636}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 7, "MS_POPULATION": 88120, "percentage": 7.943713118474807e-05}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 9, "MS_POPULATION": 69061, "percentage": 0.00013031957255180203}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 7, "MS_POPULATION": 63579, "percentage": 0.00011009924660658394}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 26, "MS_POPULATION": 97741, "percentage": 0.0002660091466221954}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 5, "MS_POPULATION": 24368, "percentage": 0.00020518713066316482}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 18, "MS_POPULATION": 78804, "percentage": 0.00022841480127912289}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 21, "MS_POPULATION": 43943, "percentage": 0.000477891814395922}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 22, "MS_POPULATION": 62761, "percentage": 0.0003505361609916987}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 10, "MS_POPULATION": 17617, "percentage": 0.0005676335357892944}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 5, "MS_POPULATION": 28987, "percentage": 0.00017249111670748955}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 38, "MS_POPULATION": 79353, "percentage": 0.00047887288445301374}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 22, "MS_POPULATION": 64641, "percentage": 0.00034034126947293515}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 25, "MS_POPULATION": 59104, "percentage": 0.0004229832160259881}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 299, "MS_POPULATION": 114364, "percentage": 0.0026144590955195692}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 58, "MS_POPULATION": 23892, "percentage": 0.0024275908253808807}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 257, "MS_POPULATION": 80946, "percentage": 0.0031749561436019073}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 294, "MS_POPULATION": 49202, "percentage": 0.005975366855005894}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 339, "MS_POPULATION": 70284, "percentage": 0.004823288372887143}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 75, "MS_POPULATION": 17671, "percentage": 0.004244241978382661}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 106, "MS_POPULATION": 30639, "percentage": 0.0034596429387382093}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 318, "MS_POPULATION": 92829, "percentage": 0.0034256536211744173}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 230, "MS_POPULATION": 67228, "percentage": 0.00342119355030642}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 311, "MS_POPULATION": 67252, "percentage": 0.004624397787426396}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 342, "MS_POPULATION": 120901, "percentage": 0.002828760721582121}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 78, "MS_POPULATION": 24455, "percentage": 0.003189531793089348}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 401, "MS_POPULATION": 83728, "percentage": 0.004789317790942098}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 322, "MS_POPULATION": 55322, "percentage": 0.005820469252738512}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 465, "MS_POPULATION": 70295, "percentage": 0.006614979728287929}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 95, "MS_POPULATION": 17849, "percentage": 0.0053224270267241865}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 116, "MS_POPULATION": 31144, "percentage": 0.0037246339583868484}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 324, "MS_POPULATION": 97907, "percentage": 0.0033092628719090566}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 246, "MS_POPULATION": 72520, "percentage": 0.0033921676778819634}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 316, "MS_POPULATION": 68094, "percentage": 0.0046406438159015476}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 348, "MS_POPULATION": 117869, "percentage": 0.0029524302403515766}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 103, "MS_POPULATION": 28346, "percentage": 0.003633669653566641}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 457, "MS_POPULATION": 90877, "percentage": 0.005028775157630644}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 372, "MS_POPULATION": 57203, "percentage": 0.006503155428911071}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 453, "MS_POPULATION": 71565, "percentage": 0.006329909872144205}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 93, "MS_POPULATION": 18961, "percentage": 0.00490480459891356}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 152, "MS_POPULATION": 32384, "percentage": 0.004693675889328063}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 450, "MS_POPULATION": 99714, "percentage": 0.004512906913773392}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 362, "MS_POPULATION": 77657, "percentage": 0.004661524395740242}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 385, "MS_POPULATION": 73584, "percentage": 0.0052321156773211565}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 419, "MS_POPULATION": 129704, "percentage": 0.0032304323690865353}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 93, "MS_POPULATION": 29056, "percentage": 0.003200715859030837}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 413, "MS_POPULATION": 93332, "percentage": 0.004425063215188789}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 472, "MS_POPULATION": 66159, "percentage": 0.0071343279070118955}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 440, "MS_POPULATION": 76876, "percentage": 0.005723502783703626}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 84, "MS_POPULATION": 19137, "percentage": 0.004389402727700266}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 128, "MS_POPULATION": 34850, "percentage": 0.003672883787661406}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 474, "MS_POPULATION": 105453, "percentage": 0.004494893459645529}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 387, "MS_POPULATION": 81649, "percentage": 0.004739800854878811}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 470, "MS_POPULATION": 85817, "percentage": 0.005476770336879639}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 227, "MS_POPULATION": 105349, "percentage": 0.002154742807240695}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 54, "MS_POPULATION": 24653, "percentage": 0.0021904027907354074}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 212, "MS_POPULATION": 84127, "percentage": 0.0025199995245283914}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 221, "MS_POPULATION": 55216, "percentage": 0.0040024630541871924}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 243, "MS_POPULATION": 66973, "percentage": 0.003628327833604587}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 49, "MS_POPULATION": 15653, "percentage": 0.0031303903405098064}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 47, "MS_POPULATION": 30550, "percentage": 0.0015384615384615385}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 207, "MS_POPULATION": 86777, "percentage": 0.0023854247093123755}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 177, "MS_POPULATION": 65934, "percentage": 0.0026845026845026846}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 190, "MS_POPULATION": 77019, "percentage": 0.0024669237460886273}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 303, "MS_POPULATION": 77129, "percentage": 0.003928483449804872}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 46, "MS_POPULATION": 16999, "percentage": 0.002706041531854815}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 273, "MS_POPULATION": 54498, "percentage": 0.005009358141583178}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 280, "MS_POPULATION": 36984, "percentage": 0.007570841444949167}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 298, "MS_POPULATION": 45051, "percentage": 0.0066147255332845}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 9923, "percentage": 0.006550438375491283}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 78, "MS_POPULATION": 19409, "percentage": 0.004018754186202277}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 278, "MS_POPULATION": 64518, "percentage": 0.004308875042623764}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 205, "MS_POPULATION": 47305, "percentage": 0.004333579959835112}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 262, "MS_POPULATION": 60688, "percentage": 0.004317163195359874}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 627, "MS_POPULATION": 49568, "percentage": 0.012649289864428663}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 100, "MS_POPULATION": 9920, "percentage": 0.010080645161290322}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 572, "MS_POPULATION": 34639, "percentage": 0.01651317878691648}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 626, "MS_POPULATION": 22709, "percentage": 0.027566163195208947}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 659, "MS_POPULATION": 28095, "percentage": 0.023456130984160883}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 151, "MS_POPULATION": 6857, "percentage": 0.022021292110252298}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 204, "MS_POPULATION": 12219, "percentage": 0.016695310581880677}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 687, "MS_POPULATION": 43514, "percentage": 0.015788022245714024}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 550, "MS_POPULATION": 31804, "percentage": 0.017293422211042637}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 638, "MS_POPULATION": 39736, "percentage": 0.01605596939802698}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 388, "MS_POPULATION": 9763, "percentage": 0.03974188261804773}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 66, "MS_POPULATION": 2250, "percentage": 0.029333333333333333}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 330, "MS_POPULATION": 8030, "percentage": 0.0410958904109589}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 355, "MS_POPULATION": 3938, "percentage": 0.09014728288471305}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 352, "MS_POPULATION": 5838, "percentage": 0.06029462144570058}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 81, "MS_POPULATION": 1447, "percentage": 0.05597788527988943}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 104, "MS_POPULATION": 2672, "percentage": 0.038922155688622756}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 392, "MS_POPULATION": 8570, "percentage": 0.04574095682613769}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 346, "MS_POPULATION": 6362, "percentage": 0.05438541339201509}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 360, "MS_POPULATION": 8230, "percentage": 0.04374240583232078}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 24, "MS_POPULATION": 119457, "percentage": 0.00020090911373967202}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 1, "MS_POPULATION": 24910, "percentage": 4.014452027298274e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 13, "MS_POPULATION": 85344, "percentage": 0.0001523247094113236}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 7, "MS_POPULATION": 50436, "percentage": 0.0001387897533507812}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 17, "MS_POPULATION": 70112, "percentage": 0.00024246919214970333}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 2, "MS_POPULATION": 18737, "percentage": 0.00010674067353365}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 2, "MS_POPULATION": 30497, "percentage": 6.558022100534478e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 8, "MS_POPULATION": 92147, "percentage": 8.681780199029811e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 8, "MS_POPULATION": 72250, "percentage": 0.00011072664359861591}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 9, "MS_POPULATION": 66786, "percentage": 0.0001347587817806127}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 18, "MS_POPULATION": 102852, "percentage": 0.00017500875043752187}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 4, "MS_POPULATION": 25686, "percentage": 0.00015572685509616132}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 10, "MS_POPULATION": 82404, "percentage": 0.00012135333236250667}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 46386, "percentage": 0.00023714051653516148}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 15, "MS_POPULATION": 65391, "percentage": 0.000229389365509015}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 5, "MS_POPULATION": 18572, "percentage": 0.0002692224854619858}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 7, "MS_POPULATION": 30126, "percentage": 0.0002323574321184359}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 6, "MS_POPULATION": 83108, "percentage": 7.219521586369543e-05}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 32, "MS_POPULATION": 67462, "percentage": 0.0004743411105511251}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 15, "MS_POPULATION": 62137, "percentage": 0.00024140206318296666}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 84, "MS_POPULATION": 115579, "percentage": 0.000726775625329861}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 30, "MS_POPULATION": 24810, "percentage": 0.0012091898428053204}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 81, "MS_POPULATION": 83150, "percentage": 0.0009741431148526759}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 103, "MS_POPULATION": 50634, "percentage": 0.0020342062645653117}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 124, "MS_POPULATION": 70573, "percentage": 0.0017570458957391637}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 32, "MS_POPULATION": 18821, "percentage": 0.0017002284682004144}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 37, "MS_POPULATION": 31562, "percentage": 0.0011722957987453267}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 105, "MS_POPULATION": 93998, "percentage": 0.001117045043511564}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 81, "MS_POPULATION": 68028, "percentage": 0.0011906861880402186}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 105, "MS_POPULATION": 71055, "percentage": 0.001477728520160439}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 140, "MS_POPULATION": 121528, "percentage": 0.0011519978934895663}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 35, "MS_POPULATION": 23581, "percentage": 0.0014842457911030066}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 117, "MS_POPULATION": 83704, "percentage": 0.0013977826627162382}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 97, "MS_POPULATION": 55582, "percentage": 0.0017451692994134792}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 159, "MS_POPULATION": 70086, "percentage": 0.0022686413834431983}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 54, "MS_POPULATION": 18359, "percentage": 0.0029413366741107903}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 48, "MS_POPULATION": 31373, "percentage": 0.0015299780065661556}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 144, "MS_POPULATION": 98604, "percentage": 0.0014603870025556773}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 107, "MS_POPULATION": 70303, "percentage": 0.0015219834146480236}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 107, "MS_POPULATION": 71014, "percentage": 0.00150674514884389}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 206, "MS_POPULATION": 121067, "percentage": 0.0017015371653712407}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 26621, "percentage": 0.0019533451034897263}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 196, "MS_POPULATION": 91355, "percentage": 0.0021454764380712606}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 193, "MS_POPULATION": 58026, "percentage": 0.003326095198704029}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 235, "MS_POPULATION": 72725, "percentage": 0.003231350979718116}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 66, "MS_POPULATION": 19512, "percentage": 0.0033825338253382535}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 67, "MS_POPULATION": 32462, "percentage": 0.002063951697369232}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 216, "MS_POPULATION": 102816, "percentage": 0.0021008403361344537}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 158, "MS_POPULATION": 76199, "percentage": 0.002073518025170934}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 150, "MS_POPULATION": 76238, "percentage": 0.0019675227576798973}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 350, "MS_POPULATION": 132717, "percentage": 0.0026371904126826252}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 69, "MS_POPULATION": 27611, "percentage": 0.002499004020136902}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 243, "MS_POPULATION": 91404, "percentage": 0.00265852697912564}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 297, "MS_POPULATION": 68198, "percentage": 0.004354966421302678}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 289, "MS_POPULATION": 75997, "percentage": 0.0038027816887508717}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 19737, "percentage": 0.0032933069868774385}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 83, "MS_POPULATION": 34203, "percentage": 0.0024266877174516856}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 323, "MS_POPULATION": 108042, "percentage": 0.0029895781270246756}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 262, "MS_POPULATION": 81771, "percentage": 0.0032040699025326826}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 308, "MS_POPULATION": 88775, "percentage": 0.003469445226696705}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 370, "MS_POPULATION": 104236, "percentage": 0.0035496373613722707}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 21864, "percentage": 0.0023783388218075376}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 280, "MS_POPULATION": 75054, "percentage": 0.003730647267300877}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 274, "MS_POPULATION": 55339, "percentage": 0.004951300168055079}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 62795, "percentage": 0.004984473286089657}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 64, "MS_POPULATION": 15101, "percentage": 0.0042381299251705185}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 85, "MS_POPULATION": 28668, "percentage": 0.0029649783730989255}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 251, "MS_POPULATION": 84501, "percentage": 0.0029703790487686536}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 241, "MS_POPULATION": 63019, "percentage": 0.0038242434821244386}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 236, "MS_POPULATION": 75047, "percentage": 0.003144695990512612}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 371, "MS_POPULATION": 67535, "percentage": 0.005493447841859777}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 13892, "percentage": 0.003743161531816873}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 288, "MS_POPULATION": 41795, "percentage": 0.006890776408661323}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 353, "MS_POPULATION": 33651, "percentage": 0.010490030013966896}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 288, "MS_POPULATION": 35865, "percentage": 0.008030112923462986}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 69, "MS_POPULATION": 8340, "percentage": 0.008273381294964029}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 64, "MS_POPULATION": 15628, "percentage": 0.004095213718965958}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 257, "MS_POPULATION": 55194, "percentage": 0.004656303221364641}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 225, "MS_POPULATION": 40155, "percentage": 0.0056032872618602915}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 269, "MS_POPULATION": 52423, "percentage": 0.005131335482517215}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 410, "MS_POPULATION": 32894, "percentage": 0.012464279199854076}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 57, "MS_POPULATION": 6132, "percentage": 0.009295499021526418}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 246, "MS_POPULATION": 17698, "percentage": 0.013899875692168606}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 377, "MS_POPULATION": 15492, "percentage": 0.024335140717789826}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 16297, "percentage": 0.019205988832300423}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 79, "MS_POPULATION": 4041, "percentage": 0.019549616431576343}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 109, "MS_POPULATION": 6855, "percentage": 0.015900802334062727}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 375, "MS_POPULATION": 26794, "percentage": 0.013995670672538627}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 310, "MS_POPULATION": 20216, "percentage": 0.015334388603086665}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 357, "MS_POPULATION": 25926, "percentage": 0.013769960657255265}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 142, "MS_POPULATION": 3882, "percentage": 0.03657908294693457}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 26, "MS_POPULATION": 809, "percentage": 0.032138442521631644}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 92, "MS_POPULATION": 2277, "percentage": 0.04040404040404041}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 148, "MS_POPULATION": 1526, "percentage": 0.09698558322411534}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 92, "MS_POPULATION": 1934, "percentage": 0.047569803516028956}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 17, "MS_POPULATION": 469, "percentage": 0.03624733475479744}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 27, "MS_POPULATION": 827, "percentage": 0.032648125755743655}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 102, "MS_POPULATION": 3105, "percentage": 0.03285024154589372}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 129, "MS_POPULATION": 2611, "percentage": 0.04940635771734968}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 121, "MS_POPULATION": 3292, "percentage": 0.03675577156743621}]}}, {"mode": "vega-lite"});
</script>



Let's add a colorscale the makes the male blue and female number pink.


```
color_scale = alt.Scale(domain=['M', 'F'],
                        range=['#1f77b4', '#e377c2'])
```


```
alt.Chart(df_plot).mark_bar().encode(
    x='AGEGROUP:N', 
    y='percentage', 
    color=alt.Color('SEX:N', scale=color_scale, legend=None),
    column='PROVINCE:N')
```





<div id="altair-viz-a31b42ff7ea54ba6b534047220fe11b7"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-a31b42ff7ea54ba6b534047220fe11b7") {
      outputDiv = document.getElementById("altair-viz-a31b42ff7ea54ba6b534047220fe11b7");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-8c4256b2c33a1fca2a5d94ca31a38873"}, "mark": "bar", "encoding": {"color": {"type": "nominal", "field": "SEX", "legend": null, "scale": {"domain": ["M", "F"], "range": ["#1f77b4", "#e377c2"]}}, "column": {"type": "nominal", "field": "PROVINCE"}, "x": {"type": "nominal", "field": "AGEGROUP"}, "y": {"type": "quantitative", "field": "percentage"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-8c4256b2c33a1fca2a5d94ca31a38873": [{"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 9, "MS_POPULATION": 113851, "percentage": 7.90506890585063e-05}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 3, "MS_POPULATION": 23744, "percentage": 0.0001263477088948787}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 11, "MS_POPULATION": 81075, "percentage": 0.0001356768424298489}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 48102, "percentage": 0.00022868072013637687}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 19, "MS_POPULATION": 67479, "percentage": 0.0002815690807510485}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 3, "MS_POPULATION": 17834, "percentage": 0.000168218010541662}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 4, "MS_POPULATION": 29270, "percentage": 0.0001366586949094636}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 7, "MS_POPULATION": 88120, "percentage": 7.943713118474807e-05}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 9, "MS_POPULATION": 69061, "percentage": 0.00013031957255180203}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 7, "MS_POPULATION": 63579, "percentage": 0.00011009924660658394}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 26, "MS_POPULATION": 97741, "percentage": 0.0002660091466221954}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 5, "MS_POPULATION": 24368, "percentage": 0.00020518713066316482}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 18, "MS_POPULATION": 78804, "percentage": 0.00022841480127912289}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 21, "MS_POPULATION": 43943, "percentage": 0.000477891814395922}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 22, "MS_POPULATION": 62761, "percentage": 0.0003505361609916987}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 10, "MS_POPULATION": 17617, "percentage": 0.0005676335357892944}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 5, "MS_POPULATION": 28987, "percentage": 0.00017249111670748955}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 38, "MS_POPULATION": 79353, "percentage": 0.00047887288445301374}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 22, "MS_POPULATION": 64641, "percentage": 0.00034034126947293515}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 25, "MS_POPULATION": 59104, "percentage": 0.0004229832160259881}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 299, "MS_POPULATION": 114364, "percentage": 0.0026144590955195692}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 58, "MS_POPULATION": 23892, "percentage": 0.0024275908253808807}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 257, "MS_POPULATION": 80946, "percentage": 0.0031749561436019073}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 294, "MS_POPULATION": 49202, "percentage": 0.005975366855005894}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 339, "MS_POPULATION": 70284, "percentage": 0.004823288372887143}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 75, "MS_POPULATION": 17671, "percentage": 0.004244241978382661}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 106, "MS_POPULATION": 30639, "percentage": 0.0034596429387382093}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 318, "MS_POPULATION": 92829, "percentage": 0.0034256536211744173}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 230, "MS_POPULATION": 67228, "percentage": 0.00342119355030642}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 311, "MS_POPULATION": 67252, "percentage": 0.004624397787426396}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 342, "MS_POPULATION": 120901, "percentage": 0.002828760721582121}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 78, "MS_POPULATION": 24455, "percentage": 0.003189531793089348}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 401, "MS_POPULATION": 83728, "percentage": 0.004789317790942098}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 322, "MS_POPULATION": 55322, "percentage": 0.005820469252738512}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 465, "MS_POPULATION": 70295, "percentage": 0.006614979728287929}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 95, "MS_POPULATION": 17849, "percentage": 0.0053224270267241865}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 116, "MS_POPULATION": 31144, "percentage": 0.0037246339583868484}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 324, "MS_POPULATION": 97907, "percentage": 0.0033092628719090566}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 246, "MS_POPULATION": 72520, "percentage": 0.0033921676778819634}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 316, "MS_POPULATION": 68094, "percentage": 0.0046406438159015476}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 348, "MS_POPULATION": 117869, "percentage": 0.0029524302403515766}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 103, "MS_POPULATION": 28346, "percentage": 0.003633669653566641}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 457, "MS_POPULATION": 90877, "percentage": 0.005028775157630644}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 372, "MS_POPULATION": 57203, "percentage": 0.006503155428911071}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 453, "MS_POPULATION": 71565, "percentage": 0.006329909872144205}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 93, "MS_POPULATION": 18961, "percentage": 0.00490480459891356}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 152, "MS_POPULATION": 32384, "percentage": 0.004693675889328063}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 450, "MS_POPULATION": 99714, "percentage": 0.004512906913773392}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 362, "MS_POPULATION": 77657, "percentage": 0.004661524395740242}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 385, "MS_POPULATION": 73584, "percentage": 0.0052321156773211565}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 419, "MS_POPULATION": 129704, "percentage": 0.0032304323690865353}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 93, "MS_POPULATION": 29056, "percentage": 0.003200715859030837}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 413, "MS_POPULATION": 93332, "percentage": 0.004425063215188789}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 472, "MS_POPULATION": 66159, "percentage": 0.0071343279070118955}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 440, "MS_POPULATION": 76876, "percentage": 0.005723502783703626}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 84, "MS_POPULATION": 19137, "percentage": 0.004389402727700266}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 128, "MS_POPULATION": 34850, "percentage": 0.003672883787661406}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 474, "MS_POPULATION": 105453, "percentage": 0.004494893459645529}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 387, "MS_POPULATION": 81649, "percentage": 0.004739800854878811}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 470, "MS_POPULATION": 85817, "percentage": 0.005476770336879639}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 227, "MS_POPULATION": 105349, "percentage": 0.002154742807240695}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 54, "MS_POPULATION": 24653, "percentage": 0.0021904027907354074}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 212, "MS_POPULATION": 84127, "percentage": 0.0025199995245283914}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 221, "MS_POPULATION": 55216, "percentage": 0.0040024630541871924}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 243, "MS_POPULATION": 66973, "percentage": 0.003628327833604587}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 49, "MS_POPULATION": 15653, "percentage": 0.0031303903405098064}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 47, "MS_POPULATION": 30550, "percentage": 0.0015384615384615385}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 207, "MS_POPULATION": 86777, "percentage": 0.0023854247093123755}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 177, "MS_POPULATION": 65934, "percentage": 0.0026845026845026846}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 190, "MS_POPULATION": 77019, "percentage": 0.0024669237460886273}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 303, "MS_POPULATION": 77129, "percentage": 0.003928483449804872}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 46, "MS_POPULATION": 16999, "percentage": 0.002706041531854815}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 273, "MS_POPULATION": 54498, "percentage": 0.005009358141583178}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 280, "MS_POPULATION": 36984, "percentage": 0.007570841444949167}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 298, "MS_POPULATION": 45051, "percentage": 0.0066147255332845}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 9923, "percentage": 0.006550438375491283}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 78, "MS_POPULATION": 19409, "percentage": 0.004018754186202277}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 278, "MS_POPULATION": 64518, "percentage": 0.004308875042623764}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 205, "MS_POPULATION": 47305, "percentage": 0.004333579959835112}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 262, "MS_POPULATION": 60688, "percentage": 0.004317163195359874}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 627, "MS_POPULATION": 49568, "percentage": 0.012649289864428663}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 100, "MS_POPULATION": 9920, "percentage": 0.010080645161290322}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 572, "MS_POPULATION": 34639, "percentage": 0.01651317878691648}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 626, "MS_POPULATION": 22709, "percentage": 0.027566163195208947}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 659, "MS_POPULATION": 28095, "percentage": 0.023456130984160883}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 151, "MS_POPULATION": 6857, "percentage": 0.022021292110252298}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 204, "MS_POPULATION": 12219, "percentage": 0.016695310581880677}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 687, "MS_POPULATION": 43514, "percentage": 0.015788022245714024}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 550, "MS_POPULATION": 31804, "percentage": 0.017293422211042637}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 638, "MS_POPULATION": 39736, "percentage": 0.01605596939802698}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 388, "MS_POPULATION": 9763, "percentage": 0.03974188261804773}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 66, "MS_POPULATION": 2250, "percentage": 0.029333333333333333}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 330, "MS_POPULATION": 8030, "percentage": 0.0410958904109589}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 355, "MS_POPULATION": 3938, "percentage": 0.09014728288471305}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 352, "MS_POPULATION": 5838, "percentage": 0.06029462144570058}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 81, "MS_POPULATION": 1447, "percentage": 0.05597788527988943}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 104, "MS_POPULATION": 2672, "percentage": 0.038922155688622756}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 392, "MS_POPULATION": 8570, "percentage": 0.04574095682613769}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 346, "MS_POPULATION": 6362, "percentage": 0.05438541339201509}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 360, "MS_POPULATION": 8230, "percentage": 0.04374240583232078}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 24, "MS_POPULATION": 119457, "percentage": 0.00020090911373967202}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 1, "MS_POPULATION": 24910, "percentage": 4.014452027298274e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 13, "MS_POPULATION": 85344, "percentage": 0.0001523247094113236}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 7, "MS_POPULATION": 50436, "percentage": 0.0001387897533507812}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 17, "MS_POPULATION": 70112, "percentage": 0.00024246919214970333}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 2, "MS_POPULATION": 18737, "percentage": 0.00010674067353365}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 2, "MS_POPULATION": 30497, "percentage": 6.558022100534478e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 8, "MS_POPULATION": 92147, "percentage": 8.681780199029811e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 8, "MS_POPULATION": 72250, "percentage": 0.00011072664359861591}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 9, "MS_POPULATION": 66786, "percentage": 0.0001347587817806127}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 18, "MS_POPULATION": 102852, "percentage": 0.00017500875043752187}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 4, "MS_POPULATION": 25686, "percentage": 0.00015572685509616132}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 10, "MS_POPULATION": 82404, "percentage": 0.00012135333236250667}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 46386, "percentage": 0.00023714051653516148}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 15, "MS_POPULATION": 65391, "percentage": 0.000229389365509015}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 5, "MS_POPULATION": 18572, "percentage": 0.0002692224854619858}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 7, "MS_POPULATION": 30126, "percentage": 0.0002323574321184359}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 6, "MS_POPULATION": 83108, "percentage": 7.219521586369543e-05}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 32, "MS_POPULATION": 67462, "percentage": 0.0004743411105511251}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 15, "MS_POPULATION": 62137, "percentage": 0.00024140206318296666}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 84, "MS_POPULATION": 115579, "percentage": 0.000726775625329861}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 30, "MS_POPULATION": 24810, "percentage": 0.0012091898428053204}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 81, "MS_POPULATION": 83150, "percentage": 0.0009741431148526759}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 103, "MS_POPULATION": 50634, "percentage": 0.0020342062645653117}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 124, "MS_POPULATION": 70573, "percentage": 0.0017570458957391637}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 32, "MS_POPULATION": 18821, "percentage": 0.0017002284682004144}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 37, "MS_POPULATION": 31562, "percentage": 0.0011722957987453267}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 105, "MS_POPULATION": 93998, "percentage": 0.001117045043511564}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 81, "MS_POPULATION": 68028, "percentage": 0.0011906861880402186}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 105, "MS_POPULATION": 71055, "percentage": 0.001477728520160439}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 140, "MS_POPULATION": 121528, "percentage": 0.0011519978934895663}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 35, "MS_POPULATION": 23581, "percentage": 0.0014842457911030066}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 117, "MS_POPULATION": 83704, "percentage": 0.0013977826627162382}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 97, "MS_POPULATION": 55582, "percentage": 0.0017451692994134792}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 159, "MS_POPULATION": 70086, "percentage": 0.0022686413834431983}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 54, "MS_POPULATION": 18359, "percentage": 0.0029413366741107903}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 48, "MS_POPULATION": 31373, "percentage": 0.0015299780065661556}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 144, "MS_POPULATION": 98604, "percentage": 0.0014603870025556773}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 107, "MS_POPULATION": 70303, "percentage": 0.0015219834146480236}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 107, "MS_POPULATION": 71014, "percentage": 0.00150674514884389}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 206, "MS_POPULATION": 121067, "percentage": 0.0017015371653712407}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 26621, "percentage": 0.0019533451034897263}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 196, "MS_POPULATION": 91355, "percentage": 0.0021454764380712606}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 193, "MS_POPULATION": 58026, "percentage": 0.003326095198704029}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 235, "MS_POPULATION": 72725, "percentage": 0.003231350979718116}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 66, "MS_POPULATION": 19512, "percentage": 0.0033825338253382535}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 67, "MS_POPULATION": 32462, "percentage": 0.002063951697369232}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 216, "MS_POPULATION": 102816, "percentage": 0.0021008403361344537}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 158, "MS_POPULATION": 76199, "percentage": 0.002073518025170934}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 150, "MS_POPULATION": 76238, "percentage": 0.0019675227576798973}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 350, "MS_POPULATION": 132717, "percentage": 0.0026371904126826252}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 69, "MS_POPULATION": 27611, "percentage": 0.002499004020136902}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 243, "MS_POPULATION": 91404, "percentage": 0.00265852697912564}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 297, "MS_POPULATION": 68198, "percentage": 0.004354966421302678}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 289, "MS_POPULATION": 75997, "percentage": 0.0038027816887508717}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 19737, "percentage": 0.0032933069868774385}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 83, "MS_POPULATION": 34203, "percentage": 0.0024266877174516856}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 323, "MS_POPULATION": 108042, "percentage": 0.0029895781270246756}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 262, "MS_POPULATION": 81771, "percentage": 0.0032040699025326826}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 308, "MS_POPULATION": 88775, "percentage": 0.003469445226696705}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 370, "MS_POPULATION": 104236, "percentage": 0.0035496373613722707}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 21864, "percentage": 0.0023783388218075376}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 280, "MS_POPULATION": 75054, "percentage": 0.003730647267300877}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 274, "MS_POPULATION": 55339, "percentage": 0.004951300168055079}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 62795, "percentage": 0.004984473286089657}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 64, "MS_POPULATION": 15101, "percentage": 0.0042381299251705185}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 85, "MS_POPULATION": 28668, "percentage": 0.0029649783730989255}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 251, "MS_POPULATION": 84501, "percentage": 0.0029703790487686536}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 241, "MS_POPULATION": 63019, "percentage": 0.0038242434821244386}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 236, "MS_POPULATION": 75047, "percentage": 0.003144695990512612}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 371, "MS_POPULATION": 67535, "percentage": 0.005493447841859777}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 13892, "percentage": 0.003743161531816873}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 288, "MS_POPULATION": 41795, "percentage": 0.006890776408661323}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 353, "MS_POPULATION": 33651, "percentage": 0.010490030013966896}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 288, "MS_POPULATION": 35865, "percentage": 0.008030112923462986}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 69, "MS_POPULATION": 8340, "percentage": 0.008273381294964029}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 64, "MS_POPULATION": 15628, "percentage": 0.004095213718965958}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 257, "MS_POPULATION": 55194, "percentage": 0.004656303221364641}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 225, "MS_POPULATION": 40155, "percentage": 0.0056032872618602915}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 269, "MS_POPULATION": 52423, "percentage": 0.005131335482517215}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 410, "MS_POPULATION": 32894, "percentage": 0.012464279199854076}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 57, "MS_POPULATION": 6132, "percentage": 0.009295499021526418}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 246, "MS_POPULATION": 17698, "percentage": 0.013899875692168606}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 377, "MS_POPULATION": 15492, "percentage": 0.024335140717789826}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 16297, "percentage": 0.019205988832300423}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 79, "MS_POPULATION": 4041, "percentage": 0.019549616431576343}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 109, "MS_POPULATION": 6855, "percentage": 0.015900802334062727}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 375, "MS_POPULATION": 26794, "percentage": 0.013995670672538627}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 310, "MS_POPULATION": 20216, "percentage": 0.015334388603086665}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 357, "MS_POPULATION": 25926, "percentage": 0.013769960657255265}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 142, "MS_POPULATION": 3882, "percentage": 0.03657908294693457}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 26, "MS_POPULATION": 809, "percentage": 0.032138442521631644}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 92, "MS_POPULATION": 2277, "percentage": 0.04040404040404041}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 148, "MS_POPULATION": 1526, "percentage": 0.09698558322411534}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 92, "MS_POPULATION": 1934, "percentage": 0.047569803516028956}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 17, "MS_POPULATION": 469, "percentage": 0.03624733475479744}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 27, "MS_POPULATION": 827, "percentage": 0.032648125755743655}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 102, "MS_POPULATION": 3105, "percentage": 0.03285024154589372}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 129, "MS_POPULATION": 2611, "percentage": 0.04940635771734968}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 121, "MS_POPULATION": 3292, "percentage": 0.03675577156743621}]}}, {"mode": "vega-lite"});
</script>



The graph's get to wide. Let's use faceting to make two rows.

Inspired and based on https://altair-viz.github.io/gallery/us_population_pyramid_over_time.html


```
#slider = alt.binding_range(min=1850, max=2000, step=10)
# select_province = alt.selection_single(name='PROVINCE', fields=['PROVINCE'],
#                                    bind=slider, init={'PROVINCE': 'Antwerpen'})
color_scale = alt.Scale(domain=['Male', 'Female'],
                        range=['#1f77b4', '#e377c2'])

select_province = alt.selection_multi(fields=['PROVINCE'], bind='legend')

base = alt.Chart(df_plot).add_selection(
    select_province
).transform_filter(
    select_province
).transform_calculate(
    gender=alt.expr.if_(alt.datum.SEX == 'M', 'Male', 'Female')
).properties(
    width=250
)

left = base.transform_filter(
    alt.datum.gender == 'Female'
).encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    x=alt.X('percentage:Q', axis=alt.Axis(format='.0%'),
            title='Percentage',
            sort=alt.SortOrder('descending'),
            ),
    color=alt.Color('gender:N', scale=color_scale, legend=None),
).mark_bar().properties(title='Female')

middle = base.encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    text=alt.Text('AGEGROUP:O'),
).mark_text().properties(width=20)

right = base.transform_filter(
    alt.datum.gender == 'Male'
).encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    x=alt.X('percentage:Q', title='Percentage', axis=alt.Axis(format='.0%'),),
    color=alt.Color('gender:N', scale=color_scale, legend=None)
).mark_bar().properties(title='Male')

# legend = alt.Chart(df_plot).mark_text().encode(
#     y=alt.Y('PROVINCE:N', axis=None),
#     text=alt.Text('PROVINCE:N'),
#     color=alt.Color('PROVINCE:N', legend=alt.Legend(title="Provincie"))
# )

alt.concat(left, middle, right, spacing=5)

#legend=alt.Legend(title="Species by color")
```





<div id="altair-viz-9448ccb88b834869a56dfe88c2457a96"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-9448ccb88b834869a56dfe88c2457a96") {
      outputDiv = document.getElementById("altair-viz-9448ccb88b834869a56dfe88c2457a96");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "concat": [{"mark": "bar", "encoding": {"color": {"type": "nominal", "field": "gender", "legend": null, "scale": {"domain": ["Male", "Female"], "range": ["#1f77b4", "#e377c2"]}}, "x": {"type": "quantitative", "axis": {"format": ".0%"}, "field": "percentage", "sort": "descending", "title": "Percentage"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"selector001": {"type": "multi", "fields": ["PROVINCE"], "bind": "legend"}}, "title": "Female", "transform": [{"filter": {"selection": "selector001"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}, {"filter": "(datum.gender === 'Female')"}], "width": 250}, {"mark": "text", "encoding": {"text": {"type": "ordinal", "field": "AGEGROUP"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"selector001": {"type": "multi", "fields": ["PROVINCE"], "bind": "legend"}}, "transform": [{"filter": {"selection": "selector001"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}], "width": 20}, {"mark": "bar", "encoding": {"color": {"type": "nominal", "field": "gender", "legend": null, "scale": {"domain": ["Male", "Female"], "range": ["#1f77b4", "#e377c2"]}}, "x": {"type": "quantitative", "axis": {"format": ".0%"}, "field": "percentage", "title": "Percentage"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"selector001": {"type": "multi", "fields": ["PROVINCE"], "bind": "legend"}}, "title": "Male", "transform": [{"filter": {"selection": "selector001"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}, {"filter": "(datum.gender === 'Male')"}], "width": 250}], "data": {"name": "data-8c4256b2c33a1fca2a5d94ca31a38873"}, "spacing": 5, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-8c4256b2c33a1fca2a5d94ca31a38873": [{"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 9, "MS_POPULATION": 113851, "percentage": 7.90506890585063e-05}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 3, "MS_POPULATION": 23744, "percentage": 0.0001263477088948787}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 11, "MS_POPULATION": 81075, "percentage": 0.0001356768424298489}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 48102, "percentage": 0.00022868072013637687}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 19, "MS_POPULATION": 67479, "percentage": 0.0002815690807510485}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 3, "MS_POPULATION": 17834, "percentage": 0.000168218010541662}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 4, "MS_POPULATION": 29270, "percentage": 0.0001366586949094636}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 7, "MS_POPULATION": 88120, "percentage": 7.943713118474807e-05}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 9, "MS_POPULATION": 69061, "percentage": 0.00013031957255180203}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 7, "MS_POPULATION": 63579, "percentage": 0.00011009924660658394}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 26, "MS_POPULATION": 97741, "percentage": 0.0002660091466221954}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 5, "MS_POPULATION": 24368, "percentage": 0.00020518713066316482}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 18, "MS_POPULATION": 78804, "percentage": 0.00022841480127912289}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 21, "MS_POPULATION": 43943, "percentage": 0.000477891814395922}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 22, "MS_POPULATION": 62761, "percentage": 0.0003505361609916987}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 10, "MS_POPULATION": 17617, "percentage": 0.0005676335357892944}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 5, "MS_POPULATION": 28987, "percentage": 0.00017249111670748955}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 38, "MS_POPULATION": 79353, "percentage": 0.00047887288445301374}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 22, "MS_POPULATION": 64641, "percentage": 0.00034034126947293515}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 25, "MS_POPULATION": 59104, "percentage": 0.0004229832160259881}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 299, "MS_POPULATION": 114364, "percentage": 0.0026144590955195692}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 58, "MS_POPULATION": 23892, "percentage": 0.0024275908253808807}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 257, "MS_POPULATION": 80946, "percentage": 0.0031749561436019073}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 294, "MS_POPULATION": 49202, "percentage": 0.005975366855005894}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 339, "MS_POPULATION": 70284, "percentage": 0.004823288372887143}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 75, "MS_POPULATION": 17671, "percentage": 0.004244241978382661}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 106, "MS_POPULATION": 30639, "percentage": 0.0034596429387382093}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 318, "MS_POPULATION": 92829, "percentage": 0.0034256536211744173}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 230, "MS_POPULATION": 67228, "percentage": 0.00342119355030642}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 311, "MS_POPULATION": 67252, "percentage": 0.004624397787426396}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 342, "MS_POPULATION": 120901, "percentage": 0.002828760721582121}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 78, "MS_POPULATION": 24455, "percentage": 0.003189531793089348}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 401, "MS_POPULATION": 83728, "percentage": 0.004789317790942098}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 322, "MS_POPULATION": 55322, "percentage": 0.005820469252738512}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 465, "MS_POPULATION": 70295, "percentage": 0.006614979728287929}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 95, "MS_POPULATION": 17849, "percentage": 0.0053224270267241865}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 116, "MS_POPULATION": 31144, "percentage": 0.0037246339583868484}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 324, "MS_POPULATION": 97907, "percentage": 0.0033092628719090566}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 246, "MS_POPULATION": 72520, "percentage": 0.0033921676778819634}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 316, "MS_POPULATION": 68094, "percentage": 0.0046406438159015476}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 348, "MS_POPULATION": 117869, "percentage": 0.0029524302403515766}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 103, "MS_POPULATION": 28346, "percentage": 0.003633669653566641}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 457, "MS_POPULATION": 90877, "percentage": 0.005028775157630644}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 372, "MS_POPULATION": 57203, "percentage": 0.006503155428911071}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 453, "MS_POPULATION": 71565, "percentage": 0.006329909872144205}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 93, "MS_POPULATION": 18961, "percentage": 0.00490480459891356}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 152, "MS_POPULATION": 32384, "percentage": 0.004693675889328063}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 450, "MS_POPULATION": 99714, "percentage": 0.004512906913773392}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 362, "MS_POPULATION": 77657, "percentage": 0.004661524395740242}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 385, "MS_POPULATION": 73584, "percentage": 0.0052321156773211565}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 419, "MS_POPULATION": 129704, "percentage": 0.0032304323690865353}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 93, "MS_POPULATION": 29056, "percentage": 0.003200715859030837}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 413, "MS_POPULATION": 93332, "percentage": 0.004425063215188789}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 472, "MS_POPULATION": 66159, "percentage": 0.0071343279070118955}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 440, "MS_POPULATION": 76876, "percentage": 0.005723502783703626}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 84, "MS_POPULATION": 19137, "percentage": 0.004389402727700266}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 128, "MS_POPULATION": 34850, "percentage": 0.003672883787661406}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 474, "MS_POPULATION": 105453, "percentage": 0.004494893459645529}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 387, "MS_POPULATION": 81649, "percentage": 0.004739800854878811}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 470, "MS_POPULATION": 85817, "percentage": 0.005476770336879639}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 227, "MS_POPULATION": 105349, "percentage": 0.002154742807240695}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 54, "MS_POPULATION": 24653, "percentage": 0.0021904027907354074}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 212, "MS_POPULATION": 84127, "percentage": 0.0025199995245283914}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 221, "MS_POPULATION": 55216, "percentage": 0.0040024630541871924}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 243, "MS_POPULATION": 66973, "percentage": 0.003628327833604587}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 49, "MS_POPULATION": 15653, "percentage": 0.0031303903405098064}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 47, "MS_POPULATION": 30550, "percentage": 0.0015384615384615385}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 207, "MS_POPULATION": 86777, "percentage": 0.0023854247093123755}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 177, "MS_POPULATION": 65934, "percentage": 0.0026845026845026846}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 190, "MS_POPULATION": 77019, "percentage": 0.0024669237460886273}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 303, "MS_POPULATION": 77129, "percentage": 0.003928483449804872}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 46, "MS_POPULATION": 16999, "percentage": 0.002706041531854815}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 273, "MS_POPULATION": 54498, "percentage": 0.005009358141583178}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 280, "MS_POPULATION": 36984, "percentage": 0.007570841444949167}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 298, "MS_POPULATION": 45051, "percentage": 0.0066147255332845}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 9923, "percentage": 0.006550438375491283}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 78, "MS_POPULATION": 19409, "percentage": 0.004018754186202277}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 278, "MS_POPULATION": 64518, "percentage": 0.004308875042623764}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 205, "MS_POPULATION": 47305, "percentage": 0.004333579959835112}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 262, "MS_POPULATION": 60688, "percentage": 0.004317163195359874}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 627, "MS_POPULATION": 49568, "percentage": 0.012649289864428663}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 100, "MS_POPULATION": 9920, "percentage": 0.010080645161290322}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 572, "MS_POPULATION": 34639, "percentage": 0.01651317878691648}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 626, "MS_POPULATION": 22709, "percentage": 0.027566163195208947}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 659, "MS_POPULATION": 28095, "percentage": 0.023456130984160883}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 151, "MS_POPULATION": 6857, "percentage": 0.022021292110252298}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 204, "MS_POPULATION": 12219, "percentage": 0.016695310581880677}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 687, "MS_POPULATION": 43514, "percentage": 0.015788022245714024}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 550, "MS_POPULATION": 31804, "percentage": 0.017293422211042637}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 638, "MS_POPULATION": 39736, "percentage": 0.01605596939802698}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 388, "MS_POPULATION": 9763, "percentage": 0.03974188261804773}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 66, "MS_POPULATION": 2250, "percentage": 0.029333333333333333}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 330, "MS_POPULATION": 8030, "percentage": 0.0410958904109589}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 355, "MS_POPULATION": 3938, "percentage": 0.09014728288471305}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 352, "MS_POPULATION": 5838, "percentage": 0.06029462144570058}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 81, "MS_POPULATION": 1447, "percentage": 0.05597788527988943}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 104, "MS_POPULATION": 2672, "percentage": 0.038922155688622756}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 392, "MS_POPULATION": 8570, "percentage": 0.04574095682613769}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 346, "MS_POPULATION": 6362, "percentage": 0.05438541339201509}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 360, "MS_POPULATION": 8230, "percentage": 0.04374240583232078}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 24, "MS_POPULATION": 119457, "percentage": 0.00020090911373967202}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 1, "MS_POPULATION": 24910, "percentage": 4.014452027298274e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 13, "MS_POPULATION": 85344, "percentage": 0.0001523247094113236}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 7, "MS_POPULATION": 50436, "percentage": 0.0001387897533507812}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 17, "MS_POPULATION": 70112, "percentage": 0.00024246919214970333}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 2, "MS_POPULATION": 18737, "percentage": 0.00010674067353365}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 2, "MS_POPULATION": 30497, "percentage": 6.558022100534478e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 8, "MS_POPULATION": 92147, "percentage": 8.681780199029811e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 8, "MS_POPULATION": 72250, "percentage": 0.00011072664359861591}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 9, "MS_POPULATION": 66786, "percentage": 0.0001347587817806127}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 18, "MS_POPULATION": 102852, "percentage": 0.00017500875043752187}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 4, "MS_POPULATION": 25686, "percentage": 0.00015572685509616132}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 10, "MS_POPULATION": 82404, "percentage": 0.00012135333236250667}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 46386, "percentage": 0.00023714051653516148}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 15, "MS_POPULATION": 65391, "percentage": 0.000229389365509015}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 5, "MS_POPULATION": 18572, "percentage": 0.0002692224854619858}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 7, "MS_POPULATION": 30126, "percentage": 0.0002323574321184359}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 6, "MS_POPULATION": 83108, "percentage": 7.219521586369543e-05}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 32, "MS_POPULATION": 67462, "percentage": 0.0004743411105511251}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 15, "MS_POPULATION": 62137, "percentage": 0.00024140206318296666}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 84, "MS_POPULATION": 115579, "percentage": 0.000726775625329861}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 30, "MS_POPULATION": 24810, "percentage": 0.0012091898428053204}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 81, "MS_POPULATION": 83150, "percentage": 0.0009741431148526759}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 103, "MS_POPULATION": 50634, "percentage": 0.0020342062645653117}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 124, "MS_POPULATION": 70573, "percentage": 0.0017570458957391637}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 32, "MS_POPULATION": 18821, "percentage": 0.0017002284682004144}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 37, "MS_POPULATION": 31562, "percentage": 0.0011722957987453267}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 105, "MS_POPULATION": 93998, "percentage": 0.001117045043511564}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 81, "MS_POPULATION": 68028, "percentage": 0.0011906861880402186}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 105, "MS_POPULATION": 71055, "percentage": 0.001477728520160439}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 140, "MS_POPULATION": 121528, "percentage": 0.0011519978934895663}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 35, "MS_POPULATION": 23581, "percentage": 0.0014842457911030066}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 117, "MS_POPULATION": 83704, "percentage": 0.0013977826627162382}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 97, "MS_POPULATION": 55582, "percentage": 0.0017451692994134792}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 159, "MS_POPULATION": 70086, "percentage": 0.0022686413834431983}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 54, "MS_POPULATION": 18359, "percentage": 0.0029413366741107903}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 48, "MS_POPULATION": 31373, "percentage": 0.0015299780065661556}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 144, "MS_POPULATION": 98604, "percentage": 0.0014603870025556773}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 107, "MS_POPULATION": 70303, "percentage": 0.0015219834146480236}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 107, "MS_POPULATION": 71014, "percentage": 0.00150674514884389}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 206, "MS_POPULATION": 121067, "percentage": 0.0017015371653712407}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 26621, "percentage": 0.0019533451034897263}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 196, "MS_POPULATION": 91355, "percentage": 0.0021454764380712606}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 193, "MS_POPULATION": 58026, "percentage": 0.003326095198704029}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 235, "MS_POPULATION": 72725, "percentage": 0.003231350979718116}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 66, "MS_POPULATION": 19512, "percentage": 0.0033825338253382535}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 67, "MS_POPULATION": 32462, "percentage": 0.002063951697369232}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 216, "MS_POPULATION": 102816, "percentage": 0.0021008403361344537}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 158, "MS_POPULATION": 76199, "percentage": 0.002073518025170934}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 150, "MS_POPULATION": 76238, "percentage": 0.0019675227576798973}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 350, "MS_POPULATION": 132717, "percentage": 0.0026371904126826252}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 69, "MS_POPULATION": 27611, "percentage": 0.002499004020136902}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 243, "MS_POPULATION": 91404, "percentage": 0.00265852697912564}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 297, "MS_POPULATION": 68198, "percentage": 0.004354966421302678}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 289, "MS_POPULATION": 75997, "percentage": 0.0038027816887508717}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 19737, "percentage": 0.0032933069868774385}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 83, "MS_POPULATION": 34203, "percentage": 0.0024266877174516856}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 323, "MS_POPULATION": 108042, "percentage": 0.0029895781270246756}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 262, "MS_POPULATION": 81771, "percentage": 0.0032040699025326826}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 308, "MS_POPULATION": 88775, "percentage": 0.003469445226696705}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 370, "MS_POPULATION": 104236, "percentage": 0.0035496373613722707}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 21864, "percentage": 0.0023783388218075376}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 280, "MS_POPULATION": 75054, "percentage": 0.003730647267300877}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 274, "MS_POPULATION": 55339, "percentage": 0.004951300168055079}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 62795, "percentage": 0.004984473286089657}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 64, "MS_POPULATION": 15101, "percentage": 0.0042381299251705185}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 85, "MS_POPULATION": 28668, "percentage": 0.0029649783730989255}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 251, "MS_POPULATION": 84501, "percentage": 0.0029703790487686536}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 241, "MS_POPULATION": 63019, "percentage": 0.0038242434821244386}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 236, "MS_POPULATION": 75047, "percentage": 0.003144695990512612}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 371, "MS_POPULATION": 67535, "percentage": 0.005493447841859777}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 13892, "percentage": 0.003743161531816873}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 288, "MS_POPULATION": 41795, "percentage": 0.006890776408661323}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 353, "MS_POPULATION": 33651, "percentage": 0.010490030013966896}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 288, "MS_POPULATION": 35865, "percentage": 0.008030112923462986}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 69, "MS_POPULATION": 8340, "percentage": 0.008273381294964029}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 64, "MS_POPULATION": 15628, "percentage": 0.004095213718965958}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 257, "MS_POPULATION": 55194, "percentage": 0.004656303221364641}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 225, "MS_POPULATION": 40155, "percentage": 0.0056032872618602915}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 269, "MS_POPULATION": 52423, "percentage": 0.005131335482517215}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 410, "MS_POPULATION": 32894, "percentage": 0.012464279199854076}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 57, "MS_POPULATION": 6132, "percentage": 0.009295499021526418}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 246, "MS_POPULATION": 17698, "percentage": 0.013899875692168606}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 377, "MS_POPULATION": 15492, "percentage": 0.024335140717789826}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 16297, "percentage": 0.019205988832300423}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 79, "MS_POPULATION": 4041, "percentage": 0.019549616431576343}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 109, "MS_POPULATION": 6855, "percentage": 0.015900802334062727}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 375, "MS_POPULATION": 26794, "percentage": 0.013995670672538627}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 310, "MS_POPULATION": 20216, "percentage": 0.015334388603086665}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 357, "MS_POPULATION": 25926, "percentage": 0.013769960657255265}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 142, "MS_POPULATION": 3882, "percentage": 0.03657908294693457}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 26, "MS_POPULATION": 809, "percentage": 0.032138442521631644}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 92, "MS_POPULATION": 2277, "percentage": 0.04040404040404041}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 148, "MS_POPULATION": 1526, "percentage": 0.09698558322411534}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 92, "MS_POPULATION": 1934, "percentage": 0.047569803516028956}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 17, "MS_POPULATION": 469, "percentage": 0.03624733475479744}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 27, "MS_POPULATION": 827, "percentage": 0.032648125755743655}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 102, "MS_POPULATION": 3105, "percentage": 0.03285024154589372}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 129, "MS_POPULATION": 2611, "percentage": 0.04940635771734968}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 121, "MS_POPULATION": 3292, "percentage": 0.03675577156743621}]}}, {"mode": "vega-lite"});
</script>




```
provinces = df_plot['PROVINCE'].unique()
select_province = alt.selection_single(
    name='Select', # name the selection 'Select'
    fields=['PROVINCE'], # limit selection to the Major_Genre field
    init={'PROVINCE': 'Antwerpen'}, # use first genre entry as initial value
    bind=alt.binding_select(options=provinces) # bind to a menu of unique provence values
)


base = alt.Chart(df_plot).add_selection(
    select_province
).transform_filter(
    select_province
).transform_calculate(
    gender=alt.expr.if_(alt.datum.SEX == 'M', 'Male', 'Female')
).properties(
    width=250
)

left = base.transform_filter(
    alt.datum.gender == 'Female'
).encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    x=alt.X('percentage:Q', axis=alt.Axis(format='.0%'),
            title='Percentage',
            sort=alt.SortOrder('descending'),
            scale=alt.Scale(domain=(0.0, 0.1), clamp=True)
            ),
    color=alt.Color('gender:N', scale=color_scale, legend=None),
    tooltip=[alt.Tooltip('percentage', format='.1%')]
).mark_bar().properties(title='Female')

middle = base.encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    text=alt.Text('AGEGROUP:O'),
).mark_text().properties(width=20)

right = base.transform_filter(
    alt.datum.gender == 'Male'
).encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    x=alt.X('percentage:Q', title='Percentage', axis=alt.Axis(format='.1%'), scale=alt.Scale(domain=(0.0, 0.1), clamp=True)),
    color=alt.Color('gender:N', scale=color_scale, legend=None),
    tooltip=[alt.Tooltip('percentage', format='.1%')]
).mark_bar().properties(title='Male')

alt.concat(left, middle, right, spacing=5).properties(title='Percentage of covid-19 cases per province, gender and age grup in Belgium')
```





<div id="altair-viz-c31051fb4ca94bf1be8426805634988e"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-c31051fb4ca94bf1be8426805634988e") {
      outputDiv = document.getElementById("altair-viz-c31051fb4ca94bf1be8426805634988e");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "concat": [{"mark": "bar", "encoding": {"color": {"type": "nominal", "field": "gender", "legend": null, "scale": {"domain": ["Male", "Female"], "range": ["#1f77b4", "#e377c2"]}}, "tooltip": [{"type": "quantitative", "field": "percentage", "format": ".1%"}], "x": {"type": "quantitative", "axis": {"format": ".0%"}, "field": "percentage", "scale": {"clamp": true, "domain": [0.0, 0.1]}, "sort": "descending", "title": "Percentage"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"Select": {"type": "single", "fields": ["PROVINCE"], "init": {"PROVINCE": "Antwerpen"}, "bind": {"input": "select", "options": ["Antwerpen", "BrabantWallon", "Hainaut", "Limburg", "Li\u00e8ge", "Luxembourg", "Namur", "OostVlaanderen", "VlaamsBrabant", "WestVlaanderen"]}}}, "title": "Female", "transform": [{"filter": {"selection": "Select"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}, {"filter": "(datum.gender === 'Female')"}], "width": 250}, {"mark": "text", "encoding": {"text": {"type": "ordinal", "field": "AGEGROUP"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"Select": {"type": "single", "fields": ["PROVINCE"], "init": {"PROVINCE": "Antwerpen"}, "bind": {"input": "select", "options": ["Antwerpen", "BrabantWallon", "Hainaut", "Limburg", "Li\u00e8ge", "Luxembourg", "Namur", "OostVlaanderen", "VlaamsBrabant", "WestVlaanderen"]}}}, "transform": [{"filter": {"selection": "Select"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}], "width": 20}, {"mark": "bar", "encoding": {"color": {"type": "nominal", "field": "gender", "legend": null, "scale": {"domain": ["Male", "Female"], "range": ["#1f77b4", "#e377c2"]}}, "tooltip": [{"type": "quantitative", "field": "percentage", "format": ".1%"}], "x": {"type": "quantitative", "axis": {"format": ".1%"}, "field": "percentage", "scale": {"clamp": true, "domain": [0.0, 0.1]}, "title": "Percentage"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"Select": {"type": "single", "fields": ["PROVINCE"], "init": {"PROVINCE": "Antwerpen"}, "bind": {"input": "select", "options": ["Antwerpen", "BrabantWallon", "Hainaut", "Limburg", "Li\u00e8ge", "Luxembourg", "Namur", "OostVlaanderen", "VlaamsBrabant", "WestVlaanderen"]}}}, "title": "Male", "transform": [{"filter": {"selection": "Select"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}, {"filter": "(datum.gender === 'Male')"}], "width": 250}], "data": {"name": "data-8c4256b2c33a1fca2a5d94ca31a38873"}, "spacing": 5, "title": "Percentage of covid-19 cases per province, gender and age grup in Belgium", "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-8c4256b2c33a1fca2a5d94ca31a38873": [{"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 9, "MS_POPULATION": 113851, "percentage": 7.90506890585063e-05}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 3, "MS_POPULATION": 23744, "percentage": 0.0001263477088948787}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 11, "MS_POPULATION": 81075, "percentage": 0.0001356768424298489}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 48102, "percentage": 0.00022868072013637687}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 19, "MS_POPULATION": 67479, "percentage": 0.0002815690807510485}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 3, "MS_POPULATION": 17834, "percentage": 0.000168218010541662}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 4, "MS_POPULATION": 29270, "percentage": 0.0001366586949094636}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 7, "MS_POPULATION": 88120, "percentage": 7.943713118474807e-05}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 9, "MS_POPULATION": 69061, "percentage": 0.00013031957255180203}, {"SEX": "F", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 7, "MS_POPULATION": 63579, "percentage": 0.00011009924660658394}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 26, "MS_POPULATION": 97741, "percentage": 0.0002660091466221954}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 5, "MS_POPULATION": 24368, "percentage": 0.00020518713066316482}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 18, "MS_POPULATION": 78804, "percentage": 0.00022841480127912289}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 21, "MS_POPULATION": 43943, "percentage": 0.000477891814395922}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 22, "MS_POPULATION": 62761, "percentage": 0.0003505361609916987}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 10, "MS_POPULATION": 17617, "percentage": 0.0005676335357892944}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 5, "MS_POPULATION": 28987, "percentage": 0.00017249111670748955}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 38, "MS_POPULATION": 79353, "percentage": 0.00047887288445301374}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 22, "MS_POPULATION": 64641, "percentage": 0.00034034126947293515}, {"SEX": "F", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 25, "MS_POPULATION": 59104, "percentage": 0.0004229832160259881}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 299, "MS_POPULATION": 114364, "percentage": 0.0026144590955195692}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 58, "MS_POPULATION": 23892, "percentage": 0.0024275908253808807}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 257, "MS_POPULATION": 80946, "percentage": 0.0031749561436019073}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 294, "MS_POPULATION": 49202, "percentage": 0.005975366855005894}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 339, "MS_POPULATION": 70284, "percentage": 0.004823288372887143}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 75, "MS_POPULATION": 17671, "percentage": 0.004244241978382661}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 106, "MS_POPULATION": 30639, "percentage": 0.0034596429387382093}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 318, "MS_POPULATION": 92829, "percentage": 0.0034256536211744173}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 230, "MS_POPULATION": 67228, "percentage": 0.00342119355030642}, {"SEX": "F", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 311, "MS_POPULATION": 67252, "percentage": 0.004624397787426396}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 342, "MS_POPULATION": 120901, "percentage": 0.002828760721582121}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 78, "MS_POPULATION": 24455, "percentage": 0.003189531793089348}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 401, "MS_POPULATION": 83728, "percentage": 0.004789317790942098}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 322, "MS_POPULATION": 55322, "percentage": 0.005820469252738512}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 465, "MS_POPULATION": 70295, "percentage": 0.006614979728287929}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 95, "MS_POPULATION": 17849, "percentage": 0.0053224270267241865}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 116, "MS_POPULATION": 31144, "percentage": 0.0037246339583868484}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 324, "MS_POPULATION": 97907, "percentage": 0.0033092628719090566}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 246, "MS_POPULATION": 72520, "percentage": 0.0033921676778819634}, {"SEX": "F", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 316, "MS_POPULATION": 68094, "percentage": 0.0046406438159015476}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 348, "MS_POPULATION": 117869, "percentage": 0.0029524302403515766}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 103, "MS_POPULATION": 28346, "percentage": 0.003633669653566641}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 457, "MS_POPULATION": 90877, "percentage": 0.005028775157630644}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 372, "MS_POPULATION": 57203, "percentage": 0.006503155428911071}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 453, "MS_POPULATION": 71565, "percentage": 0.006329909872144205}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 93, "MS_POPULATION": 18961, "percentage": 0.00490480459891356}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 152, "MS_POPULATION": 32384, "percentage": 0.004693675889328063}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 450, "MS_POPULATION": 99714, "percentage": 0.004512906913773392}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 362, "MS_POPULATION": 77657, "percentage": 0.004661524395740242}, {"SEX": "F", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 385, "MS_POPULATION": 73584, "percentage": 0.0052321156773211565}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 419, "MS_POPULATION": 129704, "percentage": 0.0032304323690865353}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 93, "MS_POPULATION": 29056, "percentage": 0.003200715859030837}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 413, "MS_POPULATION": 93332, "percentage": 0.004425063215188789}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 472, "MS_POPULATION": 66159, "percentage": 0.0071343279070118955}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 440, "MS_POPULATION": 76876, "percentage": 0.005723502783703626}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 84, "MS_POPULATION": 19137, "percentage": 0.004389402727700266}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 128, "MS_POPULATION": 34850, "percentage": 0.003672883787661406}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 474, "MS_POPULATION": 105453, "percentage": 0.004494893459645529}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 387, "MS_POPULATION": 81649, "percentage": 0.004739800854878811}, {"SEX": "F", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 470, "MS_POPULATION": 85817, "percentage": 0.005476770336879639}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 227, "MS_POPULATION": 105349, "percentage": 0.002154742807240695}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 54, "MS_POPULATION": 24653, "percentage": 0.0021904027907354074}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 212, "MS_POPULATION": 84127, "percentage": 0.0025199995245283914}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 221, "MS_POPULATION": 55216, "percentage": 0.0040024630541871924}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 243, "MS_POPULATION": 66973, "percentage": 0.003628327833604587}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 49, "MS_POPULATION": 15653, "percentage": 0.0031303903405098064}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 47, "MS_POPULATION": 30550, "percentage": 0.0015384615384615385}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 207, "MS_POPULATION": 86777, "percentage": 0.0023854247093123755}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 177, "MS_POPULATION": 65934, "percentage": 0.0026845026845026846}, {"SEX": "F", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 190, "MS_POPULATION": 77019, "percentage": 0.0024669237460886273}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 303, "MS_POPULATION": 77129, "percentage": 0.003928483449804872}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 46, "MS_POPULATION": 16999, "percentage": 0.002706041531854815}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 273, "MS_POPULATION": 54498, "percentage": 0.005009358141583178}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 280, "MS_POPULATION": 36984, "percentage": 0.007570841444949167}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 298, "MS_POPULATION": 45051, "percentage": 0.0066147255332845}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 9923, "percentage": 0.006550438375491283}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 78, "MS_POPULATION": 19409, "percentage": 0.004018754186202277}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 278, "MS_POPULATION": 64518, "percentage": 0.004308875042623764}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 205, "MS_POPULATION": 47305, "percentage": 0.004333579959835112}, {"SEX": "F", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 262, "MS_POPULATION": 60688, "percentage": 0.004317163195359874}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 627, "MS_POPULATION": 49568, "percentage": 0.012649289864428663}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 100, "MS_POPULATION": 9920, "percentage": 0.010080645161290322}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 572, "MS_POPULATION": 34639, "percentage": 0.01651317878691648}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 626, "MS_POPULATION": 22709, "percentage": 0.027566163195208947}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 659, "MS_POPULATION": 28095, "percentage": 0.023456130984160883}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 151, "MS_POPULATION": 6857, "percentage": 0.022021292110252298}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 204, "MS_POPULATION": 12219, "percentage": 0.016695310581880677}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 687, "MS_POPULATION": 43514, "percentage": 0.015788022245714024}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 550, "MS_POPULATION": 31804, "percentage": 0.017293422211042637}, {"SEX": "F", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 638, "MS_POPULATION": 39736, "percentage": 0.01605596939802698}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 388, "MS_POPULATION": 9763, "percentage": 0.03974188261804773}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 66, "MS_POPULATION": 2250, "percentage": 0.029333333333333333}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 330, "MS_POPULATION": 8030, "percentage": 0.0410958904109589}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 355, "MS_POPULATION": 3938, "percentage": 0.09014728288471305}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 352, "MS_POPULATION": 5838, "percentage": 0.06029462144570058}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 81, "MS_POPULATION": 1447, "percentage": 0.05597788527988943}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 104, "MS_POPULATION": 2672, "percentage": 0.038922155688622756}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 392, "MS_POPULATION": 8570, "percentage": 0.04574095682613769}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 346, "MS_POPULATION": 6362, "percentage": 0.05438541339201509}, {"SEX": "F", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 360, "MS_POPULATION": 8230, "percentage": 0.04374240583232078}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Antwerpen", "CASES": 24, "MS_POPULATION": 119457, "percentage": 0.00020090911373967202}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "BrabantWallon", "CASES": 1, "MS_POPULATION": 24910, "percentage": 4.014452027298274e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Hainaut", "CASES": 13, "MS_POPULATION": 85344, "percentage": 0.0001523247094113236}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Limburg", "CASES": 7, "MS_POPULATION": 50436, "percentage": 0.0001387897533507812}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Li\u00e8ge", "CASES": 17, "MS_POPULATION": 70112, "percentage": 0.00024246919214970333}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Luxembourg", "CASES": 2, "MS_POPULATION": 18737, "percentage": 0.00010674067353365}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "Namur", "CASES": 2, "MS_POPULATION": 30497, "percentage": 6.558022100534478e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "OostVlaanderen", "CASES": 8, "MS_POPULATION": 92147, "percentage": 8.681780199029811e-05}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "VlaamsBrabant", "CASES": 8, "MS_POPULATION": 72250, "percentage": 0.00011072664359861591}, {"SEX": "M", "AGEGROUP": "0-9", "PROVINCE": "WestVlaanderen", "CASES": 9, "MS_POPULATION": 66786, "percentage": 0.0001347587817806127}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Antwerpen", "CASES": 18, "MS_POPULATION": 102852, "percentage": 0.00017500875043752187}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "BrabantWallon", "CASES": 4, "MS_POPULATION": 25686, "percentage": 0.00015572685509616132}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Hainaut", "CASES": 10, "MS_POPULATION": 82404, "percentage": 0.00012135333236250667}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Limburg", "CASES": 11, "MS_POPULATION": 46386, "percentage": 0.00023714051653516148}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Li\u00e8ge", "CASES": 15, "MS_POPULATION": 65391, "percentage": 0.000229389365509015}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Luxembourg", "CASES": 5, "MS_POPULATION": 18572, "percentage": 0.0002692224854619858}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "Namur", "CASES": 7, "MS_POPULATION": 30126, "percentage": 0.0002323574321184359}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "OostVlaanderen", "CASES": 6, "MS_POPULATION": 83108, "percentage": 7.219521586369543e-05}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "VlaamsBrabant", "CASES": 32, "MS_POPULATION": 67462, "percentage": 0.0004743411105511251}, {"SEX": "M", "AGEGROUP": "10-19", "PROVINCE": "WestVlaanderen", "CASES": 15, "MS_POPULATION": 62137, "percentage": 0.00024140206318296666}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Antwerpen", "CASES": 84, "MS_POPULATION": 115579, "percentage": 0.000726775625329861}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "BrabantWallon", "CASES": 30, "MS_POPULATION": 24810, "percentage": 0.0012091898428053204}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Hainaut", "CASES": 81, "MS_POPULATION": 83150, "percentage": 0.0009741431148526759}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Limburg", "CASES": 103, "MS_POPULATION": 50634, "percentage": 0.0020342062645653117}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Li\u00e8ge", "CASES": 124, "MS_POPULATION": 70573, "percentage": 0.0017570458957391637}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Luxembourg", "CASES": 32, "MS_POPULATION": 18821, "percentage": 0.0017002284682004144}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "Namur", "CASES": 37, "MS_POPULATION": 31562, "percentage": 0.0011722957987453267}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "OostVlaanderen", "CASES": 105, "MS_POPULATION": 93998, "percentage": 0.001117045043511564}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "VlaamsBrabant", "CASES": 81, "MS_POPULATION": 68028, "percentage": 0.0011906861880402186}, {"SEX": "M", "AGEGROUP": "20-29", "PROVINCE": "WestVlaanderen", "CASES": 105, "MS_POPULATION": 71055, "percentage": 0.001477728520160439}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Antwerpen", "CASES": 140, "MS_POPULATION": 121528, "percentage": 0.0011519978934895663}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "BrabantWallon", "CASES": 35, "MS_POPULATION": 23581, "percentage": 0.0014842457911030066}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Hainaut", "CASES": 117, "MS_POPULATION": 83704, "percentage": 0.0013977826627162382}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Limburg", "CASES": 97, "MS_POPULATION": 55582, "percentage": 0.0017451692994134792}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Li\u00e8ge", "CASES": 159, "MS_POPULATION": 70086, "percentage": 0.0022686413834431983}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Luxembourg", "CASES": 54, "MS_POPULATION": 18359, "percentage": 0.0029413366741107903}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "Namur", "CASES": 48, "MS_POPULATION": 31373, "percentage": 0.0015299780065661556}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "OostVlaanderen", "CASES": 144, "MS_POPULATION": 98604, "percentage": 0.0014603870025556773}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "VlaamsBrabant", "CASES": 107, "MS_POPULATION": 70303, "percentage": 0.0015219834146480236}, {"SEX": "M", "AGEGROUP": "30-39", "PROVINCE": "WestVlaanderen", "CASES": 107, "MS_POPULATION": 71014, "percentage": 0.00150674514884389}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Antwerpen", "CASES": 206, "MS_POPULATION": 121067, "percentage": 0.0017015371653712407}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 26621, "percentage": 0.0019533451034897263}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Hainaut", "CASES": 196, "MS_POPULATION": 91355, "percentage": 0.0021454764380712606}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Limburg", "CASES": 193, "MS_POPULATION": 58026, "percentage": 0.003326095198704029}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Li\u00e8ge", "CASES": 235, "MS_POPULATION": 72725, "percentage": 0.003231350979718116}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Luxembourg", "CASES": 66, "MS_POPULATION": 19512, "percentage": 0.0033825338253382535}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "Namur", "CASES": 67, "MS_POPULATION": 32462, "percentage": 0.002063951697369232}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "OostVlaanderen", "CASES": 216, "MS_POPULATION": 102816, "percentage": 0.0021008403361344537}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "VlaamsBrabant", "CASES": 158, "MS_POPULATION": 76199, "percentage": 0.002073518025170934}, {"SEX": "M", "AGEGROUP": "40-49", "PROVINCE": "WestVlaanderen", "CASES": 150, "MS_POPULATION": 76238, "percentage": 0.0019675227576798973}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Antwerpen", "CASES": 350, "MS_POPULATION": 132717, "percentage": 0.0026371904126826252}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "BrabantWallon", "CASES": 69, "MS_POPULATION": 27611, "percentage": 0.002499004020136902}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Hainaut", "CASES": 243, "MS_POPULATION": 91404, "percentage": 0.00265852697912564}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Limburg", "CASES": 297, "MS_POPULATION": 68198, "percentage": 0.004354966421302678}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Li\u00e8ge", "CASES": 289, "MS_POPULATION": 75997, "percentage": 0.0038027816887508717}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Luxembourg", "CASES": 65, "MS_POPULATION": 19737, "percentage": 0.0032933069868774385}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "Namur", "CASES": 83, "MS_POPULATION": 34203, "percentage": 0.0024266877174516856}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "OostVlaanderen", "CASES": 323, "MS_POPULATION": 108042, "percentage": 0.0029895781270246756}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "VlaamsBrabant", "CASES": 262, "MS_POPULATION": 81771, "percentage": 0.0032040699025326826}, {"SEX": "M", "AGEGROUP": "50-59", "PROVINCE": "WestVlaanderen", "CASES": 308, "MS_POPULATION": 88775, "percentage": 0.003469445226696705}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Antwerpen", "CASES": 370, "MS_POPULATION": 104236, "percentage": 0.0035496373613722707}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 21864, "percentage": 0.0023783388218075376}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Hainaut", "CASES": 280, "MS_POPULATION": 75054, "percentage": 0.003730647267300877}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Limburg", "CASES": 274, "MS_POPULATION": 55339, "percentage": 0.004951300168055079}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 62795, "percentage": 0.004984473286089657}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Luxembourg", "CASES": 64, "MS_POPULATION": 15101, "percentage": 0.0042381299251705185}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "Namur", "CASES": 85, "MS_POPULATION": 28668, "percentage": 0.0029649783730989255}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "OostVlaanderen", "CASES": 251, "MS_POPULATION": 84501, "percentage": 0.0029703790487686536}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "VlaamsBrabant", "CASES": 241, "MS_POPULATION": 63019, "percentage": 0.0038242434821244386}, {"SEX": "M", "AGEGROUP": "60-69", "PROVINCE": "WestVlaanderen", "CASES": 236, "MS_POPULATION": 75047, "percentage": 0.003144695990512612}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Antwerpen", "CASES": 371, "MS_POPULATION": 67535, "percentage": 0.005493447841859777}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "BrabantWallon", "CASES": 52, "MS_POPULATION": 13892, "percentage": 0.003743161531816873}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Hainaut", "CASES": 288, "MS_POPULATION": 41795, "percentage": 0.006890776408661323}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Limburg", "CASES": 353, "MS_POPULATION": 33651, "percentage": 0.010490030013966896}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Li\u00e8ge", "CASES": 288, "MS_POPULATION": 35865, "percentage": 0.008030112923462986}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Luxembourg", "CASES": 69, "MS_POPULATION": 8340, "percentage": 0.008273381294964029}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "Namur", "CASES": 64, "MS_POPULATION": 15628, "percentage": 0.004095213718965958}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "OostVlaanderen", "CASES": 257, "MS_POPULATION": 55194, "percentage": 0.004656303221364641}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "VlaamsBrabant", "CASES": 225, "MS_POPULATION": 40155, "percentage": 0.0056032872618602915}, {"SEX": "M", "AGEGROUP": "70-79", "PROVINCE": "WestVlaanderen", "CASES": 269, "MS_POPULATION": 52423, "percentage": 0.005131335482517215}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Antwerpen", "CASES": 410, "MS_POPULATION": 32894, "percentage": 0.012464279199854076}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "BrabantWallon", "CASES": 57, "MS_POPULATION": 6132, "percentage": 0.009295499021526418}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Hainaut", "CASES": 246, "MS_POPULATION": 17698, "percentage": 0.013899875692168606}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Limburg", "CASES": 377, "MS_POPULATION": 15492, "percentage": 0.024335140717789826}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Li\u00e8ge", "CASES": 313, "MS_POPULATION": 16297, "percentage": 0.019205988832300423}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Luxembourg", "CASES": 79, "MS_POPULATION": 4041, "percentage": 0.019549616431576343}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "Namur", "CASES": 109, "MS_POPULATION": 6855, "percentage": 0.015900802334062727}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "OostVlaanderen", "CASES": 375, "MS_POPULATION": 26794, "percentage": 0.013995670672538627}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "VlaamsBrabant", "CASES": 310, "MS_POPULATION": 20216, "percentage": 0.015334388603086665}, {"SEX": "M", "AGEGROUP": "80-89", "PROVINCE": "WestVlaanderen", "CASES": 357, "MS_POPULATION": 25926, "percentage": 0.013769960657255265}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Antwerpen", "CASES": 142, "MS_POPULATION": 3882, "percentage": 0.03657908294693457}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "BrabantWallon", "CASES": 26, "MS_POPULATION": 809, "percentage": 0.032138442521631644}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Hainaut", "CASES": 92, "MS_POPULATION": 2277, "percentage": 0.04040404040404041}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Limburg", "CASES": 148, "MS_POPULATION": 1526, "percentage": 0.09698558322411534}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Li\u00e8ge", "CASES": 92, "MS_POPULATION": 1934, "percentage": 0.047569803516028956}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Luxembourg", "CASES": 17, "MS_POPULATION": 469, "percentage": 0.03624733475479744}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "Namur", "CASES": 27, "MS_POPULATION": 827, "percentage": 0.032648125755743655}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "OostVlaanderen", "CASES": 102, "MS_POPULATION": 3105, "percentage": 0.03285024154589372}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "VlaamsBrabant", "CASES": 129, "MS_POPULATION": 2611, "percentage": 0.04940635771734968}, {"SEX": "M", "AGEGROUP": "90+", "PROVINCE": "WestVlaanderen", "CASES": 121, "MS_POPULATION": 3292, "percentage": 0.03675577156743621}]}}, {"mode": "vega-lite"});
</script>



# Mortality


```
# https://epistat.wiv-isp.be/covid/
# Dataset of mortality by date, age, sex, and region
df_dead_sc = pd.read_csv('https://epistat.sciensano.be/Data/COVID19BE_MORT.csv')
```


```
df_dead_sc.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATE</th>
      <th>REGION</th>
      <th>AGEGROUP</th>
      <th>SEX</th>
      <th>DEATHS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020-03-10</td>
      <td>Brussels</td>
      <td>85+</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020-03-11</td>
      <td>Flanders</td>
      <td>85+</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020-03-11</td>
      <td>Brussels</td>
      <td>75-84</td>
      <td>M</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020-03-11</td>
      <td>Brussels</td>
      <td>85+</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020-03-12</td>
      <td>Brussels</td>
      <td>75-84</td>
      <td>M</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```
df_dead_sc['REGION'].value_counts()
```




    Wallonia    291
    Flanders    275
    Brussels    271
    Name: REGION, dtype: int64




```
df_dead_sc['AGEGROUP'].value_counts()
```




    85+      223
    75-84    205
    65-74    179
    45-64    132
    25-44     19
    0-24       1
    Name: AGEGROUP, dtype: int64




```
df_inhab['AGEGROUP_sc'] =pd.cut(df_inhab['CD_AGE'], bins=[0,24,44,64,74,84,200], labels=['0-24','25-44','45-64','65-74','75-84','85+'], include_lowest=True)
```


```
df_inhab.groupby('AGEGROUP_sc').agg(lowest_age=('CD_AGE', 'min'), highest_age=('CD_AGE', max))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>lowest_age</th>
      <th>highest_age</th>
    </tr>
    <tr>
      <th>AGEGROUP_sc</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-24</th>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>25-44</th>
      <td>25</td>
      <td>44</td>
    </tr>
    <tr>
      <th>45-64</th>
      <td>45</td>
      <td>64</td>
    </tr>
    <tr>
      <th>65-74</th>
      <td>65</td>
      <td>74</td>
    </tr>
    <tr>
      <th>75-84</th>
      <td>75</td>
      <td>84</td>
    </tr>
    <tr>
      <th>85+</th>
      <td>85</td>
      <td>110</td>
    </tr>
  </tbody>
</table>
</div>




```
df_inhab.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CD_REFNIS</th>
      <th>TX_DESCR_NL</th>
      <th>TX_DESCR_FR</th>
      <th>CD_DSTR_REFNIS</th>
      <th>TX_ADM_DSTR_DESCR_NL</th>
      <th>TX_ADM_DSTR_DESCR_FR</th>
      <th>CD_PROV_REFNIS</th>
      <th>TX_PROV_DESCR_NL</th>
      <th>TX_PROV_DESCR_FR</th>
      <th>CD_RGN_REFNIS</th>
      <th>TX_RGN_DESCR_NL</th>
      <th>TX_RGN_DESCR_FR</th>
      <th>CD_SEX</th>
      <th>CD_NATLTY</th>
      <th>TX_NATLTY_NL</th>
      <th>TX_NATLTY_FR</th>
      <th>CD_CIV_STS</th>
      <th>TX_CIV_STS_NL</th>
      <th>TX_CIV_STS_FR</th>
      <th>CD_AGE</th>
      <th>MS_POPULATION</th>
      <th>sc_provence</th>
      <th>AGEGROUP</th>
      <th>AGEGROUP_sc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>69</td>
      <td>11</td>
      <td>Antwerpen</td>
      <td>60-69</td>
      <td>65-74</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>80</td>
      <td>3</td>
      <td>Antwerpen</td>
      <td>70-79</td>
      <td>75-84</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>M</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>30</td>
      <td>2</td>
      <td>Antwerpen</td>
      <td>20-29</td>
      <td>25-44</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>48</td>
      <td>26</td>
      <td>Antwerpen</td>
      <td>40-49</td>
      <td>45-64</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11001</td>
      <td>Aartselaar</td>
      <td>Aartselaar</td>
      <td>11000</td>
      <td>Arrondissement Antwerpen</td>
      <td>Arrondissement d’Anvers</td>
      <td>10000.0</td>
      <td>Provincie Antwerpen</td>
      <td>Province d’Anvers</td>
      <td>2000</td>
      <td>Vlaams Gewest</td>
      <td>Région flamande</td>
      <td>F</td>
      <td>BEL</td>
      <td>Belgen</td>
      <td>Belges</td>
      <td>4</td>
      <td>Gescheiden</td>
      <td>Divorcé</td>
      <td>76</td>
      <td>2</td>
      <td>Antwerpen</td>
      <td>70-79</td>
      <td>75-84</td>
    </tr>
  </tbody>
</table>
</div>




```
df_dead_sc['REGION'].unique()
```




    array(['Brussels', 'Flanders', 'Wallonia'], dtype=object)




```
df_inhab['TX_RGN_DESCR_NL'].value_counts()
```




    Vlaams Gewest                     242865
    Waals Gewest                      199003
    Brussels Hoofdstedelijk Gewest     21513
    Name: TX_RGN_DESCR_NL, dtype: int64




```
df_inhab_gender_prov = df_inhab.groupby(['TX_RGN_DESCR_NL', 'CD_SEX', 'AGEGROUP_sc'])['MS_POPULATION'].sum().reset_index()
```


```
region_sc_to_region_inhad = {'Flanders':'Vlaams Gewest', 'Wallonia':'Waals Gewest', 'Brussels':'Brussels Hoofdstedelijk Gewest'}
```


```
df_dead_sc['TX_RGN_DESCR_NL'] = df_dead_sc['REGION'].map(region_sc_to_region_inhad)
```


```
df_dead_sc.groupby(['TX_RGN_DESCR_NL', 'AGEGROUP', 'SEX'])['DEATHS'].sum()
```




    TX_RGN_DESCR_NL                 AGEGROUP  SEX
    Brussels Hoofdstedelijk Gewest  25-44     F        1
                                              M        4
                                    45-64     F       21
                                              M       43
                                    65-74     F       42
                                              M       71
                                    75-84     F      128
                                              M      170
                                    85+       F      270
                                              M      186
    Vlaams Gewest                   0-24      F        1
                                    25-44     F        2
                                              M        3
                                    45-64     F       27
                                              M       63
                                    65-74     F       67
                                              M      130
                                    75-84     F      199
                                              M      335
                                    85+       F      232
                                              M      309
    Waals Gewest                    25-44     F        5
                                              M        4
                                    45-64     F       41
                                              M       89
                                    65-74     F       98
                                              M      186
                                    75-84     F      290
                                              M      300
                                    85+       F      704
                                              M      421
    Name: DEATHS, dtype: int64




```
df_dead_sc_region_agegroup_gender = df_dead_sc.groupby(['TX_RGN_DESCR_NL', 'AGEGROUP', 'SEX'])['DEATHS'].sum().reset_index()
```


```
df_inhab_gender_prov_deaths = pd.merge(df_inhab_gender_prov, df_dead_sc_region_agegroup_gender, left_on=['TX_RGN_DESCR_NL', 'AGEGROUP_sc', 'CD_SEX'], right_on=['TX_RGN_DESCR_NL', 'AGEGROUP', 'SEX'])
```


```
df_inhab_gender_prov_deaths['MS_POPULATION'].sum()
```




    9077403




```
df_inhab_gender_prov_deaths['DEATHS'].sum()
```




    4442




```
df_inhab_gender_prov_deaths
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TX_RGN_DESCR_NL</th>
      <th>CD_SEX</th>
      <th>AGEGROUP_sc</th>
      <th>MS_POPULATION</th>
      <th>AGEGROUP</th>
      <th>SEX</th>
      <th>DEATHS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>F</td>
      <td>25-44</td>
      <td>197579</td>
      <td>25-44</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>F</td>
      <td>45-64</td>
      <td>137628</td>
      <td>45-64</td>
      <td>F</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>F</td>
      <td>65-74</td>
      <td>45214</td>
      <td>65-74</td>
      <td>F</td>
      <td>42</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>F</td>
      <td>75-84</td>
      <td>30059</td>
      <td>75-84</td>
      <td>F</td>
      <td>128</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>F</td>
      <td>85+</td>
      <td>18811</td>
      <td>85+</td>
      <td>F</td>
      <td>270</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>M</td>
      <td>25-44</td>
      <td>194988</td>
      <td>25-44</td>
      <td>M</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>M</td>
      <td>45-64</td>
      <td>140348</td>
      <td>45-64</td>
      <td>M</td>
      <td>43</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>M</td>
      <td>65-74</td>
      <td>36698</td>
      <td>65-74</td>
      <td>M</td>
      <td>71</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>M</td>
      <td>75-84</td>
      <td>19969</td>
      <td>75-84</td>
      <td>M</td>
      <td>170</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Brussels Hoofdstedelijk Gewest</td>
      <td>M</td>
      <td>85+</td>
      <td>7918</td>
      <td>85+</td>
      <td>M</td>
      <td>186</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Vlaams Gewest</td>
      <td>F</td>
      <td>0-24</td>
      <td>874891</td>
      <td>0-24</td>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Vlaams Gewest</td>
      <td>F</td>
      <td>25-44</td>
      <td>820036</td>
      <td>25-44</td>
      <td>F</td>
      <td>2</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Vlaams Gewest</td>
      <td>F</td>
      <td>45-64</td>
      <td>901554</td>
      <td>45-64</td>
      <td>F</td>
      <td>27</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Vlaams Gewest</td>
      <td>F</td>
      <td>65-74</td>
      <td>353925</td>
      <td>65-74</td>
      <td>F</td>
      <td>67</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Vlaams Gewest</td>
      <td>F</td>
      <td>75-84</td>
      <td>245981</td>
      <td>75-84</td>
      <td>F</td>
      <td>199</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Vlaams Gewest</td>
      <td>F</td>
      <td>85+</td>
      <td>132649</td>
      <td>85+</td>
      <td>F</td>
      <td>232</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Vlaams Gewest</td>
      <td>M</td>
      <td>25-44</td>
      <td>827281</td>
      <td>25-44</td>
      <td>M</td>
      <td>3</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Vlaams Gewest</td>
      <td>M</td>
      <td>45-64</td>
      <td>917008</td>
      <td>45-64</td>
      <td>M</td>
      <td>63</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Vlaams Gewest</td>
      <td>M</td>
      <td>65-74</td>
      <td>336242</td>
      <td>65-74</td>
      <td>M</td>
      <td>130</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Vlaams Gewest</td>
      <td>M</td>
      <td>75-84</td>
      <td>193576</td>
      <td>75-84</td>
      <td>M</td>
      <td>335</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Vlaams Gewest</td>
      <td>M</td>
      <td>85+</td>
      <td>69678</td>
      <td>85+</td>
      <td>M</td>
      <td>309</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Waals Gewest</td>
      <td>F</td>
      <td>25-44</td>
      <td>457356</td>
      <td>25-44</td>
      <td>F</td>
      <td>5</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Waals Gewest</td>
      <td>F</td>
      <td>45-64</td>
      <td>496668</td>
      <td>45-64</td>
      <td>F</td>
      <td>41</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Waals Gewest</td>
      <td>F</td>
      <td>65-74</td>
      <td>199422</td>
      <td>65-74</td>
      <td>F</td>
      <td>98</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Waals Gewest</td>
      <td>F</td>
      <td>75-84</td>
      <td>118224</td>
      <td>75-84</td>
      <td>F</td>
      <td>290</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Waals Gewest</td>
      <td>F</td>
      <td>85+</td>
      <td>68502</td>
      <td>85+</td>
      <td>F</td>
      <td>704</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Waals Gewest</td>
      <td>M</td>
      <td>25-44</td>
      <td>459444</td>
      <td>25-44</td>
      <td>M</td>
      <td>4</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Waals Gewest</td>
      <td>M</td>
      <td>45-64</td>
      <td>487322</td>
      <td>45-64</td>
      <td>M</td>
      <td>89</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Waals Gewest</td>
      <td>M</td>
      <td>65-74</td>
      <td>175508</td>
      <td>65-74</td>
      <td>M</td>
      <td>186</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Waals Gewest</td>
      <td>M</td>
      <td>75-84</td>
      <td>82876</td>
      <td>75-84</td>
      <td>M</td>
      <td>300</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Waals Gewest</td>
      <td>M</td>
      <td>85+</td>
      <td>30048</td>
      <td>85+</td>
      <td>M</td>
      <td>421</td>
    </tr>
  </tbody>
</table>
</div>




```
df_inhab_gender_prov_deaths['percentage'] = df_inhab_gender_prov_deaths['DEATHS']/df_inhab_gender_prov_deaths['MS_POPULATION']
```


```
df_plot = df_inhab_gender_prov_deaths
```


```
regions = df_plot['TX_RGN_DESCR_NL'].unique()
select_province = alt.selection_single(
    name='Select', # name the selection 'Select'
    fields=['TX_RGN_DESCR_NL'], # limit selection to the Major_Genre field
    init={'TX_RGN_DESCR_NL': 'Vlaams Gewest'}, # use first genre entry as initial value
    bind=alt.binding_select(options=regions) # bind to a menu of unique provence values
)

base = alt.Chart(df_plot).add_selection(
    select_province
).transform_filter(
    select_province
).transform_calculate(
    gender=alt.expr.if_(alt.datum.SEX == 'M', 'Male', 'Female')
).properties(
    width=250
)

left = base.transform_filter(
    alt.datum.gender == 'Female'
).encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    x=alt.X('percentage:Q', axis=alt.Axis(format='.2%'),
            title='Percentage',
            sort=alt.SortOrder('descending'),
            # scale=alt.Scale(domain=(0.0, 0.02), clamp=True)
            ),
    color=alt.Color('gender:N', scale=color_scale, legend=None),
    tooltip=[alt.Tooltip('percentage', format='.2%')]
).mark_bar().properties(title='Female')

middle = base.encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    text=alt.Text('AGEGROUP:O'),
).mark_text().properties(width=20)

right = base.transform_filter(
    alt.datum.gender == 'Male'
).encode(
    y=alt.Y('AGEGROUP:O', axis=None),
    # x=alt.X('percentage:Q', title='Percentage', axis=alt.Axis(format='.2%'), scale=alt.Scale(domain=(0.0, 0.02), clamp=True)),
    x=alt.X('percentage:Q', title='Percentage', axis=alt.Axis(format='.2%')),
    color=alt.Color('gender:N', scale=color_scale, legend=None),
    tooltip=[alt.Tooltip('percentage', format='.2%')]
).mark_bar().properties(title='Male')

alt.concat(left, middle, right, spacing=5).properties(title='Percentage of covid-19 deaths per province, gender and age group relative to number of inhabitants in Belgium')
```





<div id="altair-viz-2dad2a5aef0a428894b0b92b6d97b4df"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-2dad2a5aef0a428894b0b92b6d97b4df") {
      outputDiv = document.getElementById("altair-viz-2dad2a5aef0a428894b0b92b6d97b4df");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "concat": [{"mark": "bar", "encoding": {"color": {"type": "nominal", "field": "gender", "legend": null, "scale": {"domain": ["Male", "Female"], "range": ["#1f77b4", "#e377c2"]}}, "tooltip": [{"type": "quantitative", "field": "percentage", "format": ".2%"}], "x": {"type": "quantitative", "axis": {"format": ".2%"}, "field": "percentage", "sort": "descending", "title": "Percentage"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"Select": {"type": "single", "fields": ["TX_RGN_DESCR_NL"], "init": {"TX_RGN_DESCR_NL": "Vlaams Gewest"}, "bind": {"input": "select", "options": ["Brussels Hoofdstedelijk Gewest", "Vlaams Gewest", "Waals Gewest"]}}}, "title": "Female", "transform": [{"filter": {"selection": "Select"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}, {"filter": "(datum.gender === 'Female')"}], "width": 250}, {"mark": "text", "encoding": {"text": {"type": "ordinal", "field": "AGEGROUP"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"Select": {"type": "single", "fields": ["TX_RGN_DESCR_NL"], "init": {"TX_RGN_DESCR_NL": "Vlaams Gewest"}, "bind": {"input": "select", "options": ["Brussels Hoofdstedelijk Gewest", "Vlaams Gewest", "Waals Gewest"]}}}, "transform": [{"filter": {"selection": "Select"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}], "width": 20}, {"mark": "bar", "encoding": {"color": {"type": "nominal", "field": "gender", "legend": null, "scale": {"domain": ["Male", "Female"], "range": ["#1f77b4", "#e377c2"]}}, "tooltip": [{"type": "quantitative", "field": "percentage", "format": ".2%"}], "x": {"type": "quantitative", "axis": {"format": ".2%"}, "field": "percentage", "title": "Percentage"}, "y": {"type": "ordinal", "axis": null, "field": "AGEGROUP"}}, "selection": {"Select": {"type": "single", "fields": ["TX_RGN_DESCR_NL"], "init": {"TX_RGN_DESCR_NL": "Vlaams Gewest"}, "bind": {"input": "select", "options": ["Brussels Hoofdstedelijk Gewest", "Vlaams Gewest", "Waals Gewest"]}}}, "title": "Male", "transform": [{"filter": {"selection": "Select"}}, {"calculate": "if((datum.SEX === 'M'),'Male','Female')", "as": "gender"}, {"filter": "(datum.gender === 'Male')"}], "width": 250}], "data": {"name": "data-ed3089c1cca1599e394e5b0dc87c3c00"}, "spacing": 5, "title": "Percentage of covid-19 deaths per province, gender and age group relative to number of inhabitants in Belgium", "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-ed3089c1cca1599e394e5b0dc87c3c00": [{"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "F", "AGEGROUP_sc": "25-44", "MS_POPULATION": 197579, "AGEGROUP": "25-44", "SEX": "F", "DEATHS": 1, "percentage": 5.061266632587471e-06}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "F", "AGEGROUP_sc": "45-64", "MS_POPULATION": 137628, "AGEGROUP": "45-64", "SEX": "F", "DEATHS": 21, "percentage": 0.00015258522974976024}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "F", "AGEGROUP_sc": "65-74", "MS_POPULATION": 45214, "AGEGROUP": "65-74", "SEX": "F", "DEATHS": 42, "percentage": 0.0009289158225328438}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "F", "AGEGROUP_sc": "75-84", "MS_POPULATION": 30059, "AGEGROUP": "75-84", "SEX": "F", "DEATHS": 128, "percentage": 0.004258292025682823}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "F", "AGEGROUP_sc": "85+", "MS_POPULATION": 18811, "AGEGROUP": "85+", "SEX": "F", "DEATHS": 270, "percentage": 0.014353303917920366}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "M", "AGEGROUP_sc": "25-44", "MS_POPULATION": 194988, "AGEGROUP": "25-44", "SEX": "M", "DEATHS": 4, "percentage": 2.0514082917923155e-05}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "M", "AGEGROUP_sc": "45-64", "MS_POPULATION": 140348, "AGEGROUP": "45-64", "SEX": "M", "DEATHS": 43, "percentage": 0.00030638128081625674}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "M", "AGEGROUP_sc": "65-74", "MS_POPULATION": 36698, "AGEGROUP": "65-74", "SEX": "M", "DEATHS": 71, "percentage": 0.001934710338438062}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "M", "AGEGROUP_sc": "75-84", "MS_POPULATION": 19969, "AGEGROUP": "75-84", "SEX": "M", "DEATHS": 170, "percentage": 0.008513195452952076}, {"TX_RGN_DESCR_NL": "Brussels Hoofdstedelijk Gewest", "CD_SEX": "M", "AGEGROUP_sc": "85+", "MS_POPULATION": 7918, "AGEGROUP": "85+", "SEX": "M", "DEATHS": 186, "percentage": 0.023490780500126294}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "F", "AGEGROUP_sc": "0-24", "MS_POPULATION": 874891, "AGEGROUP": "0-24", "SEX": "F", "DEATHS": 1, "percentage": 1.142999527941195e-06}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "F", "AGEGROUP_sc": "25-44", "MS_POPULATION": 820036, "AGEGROUP": "25-44", "SEX": "F", "DEATHS": 2, "percentage": 2.438917315825159e-06}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "F", "AGEGROUP_sc": "45-64", "MS_POPULATION": 901554, "AGEGROUP": "45-64", "SEX": "F", "DEATHS": 27, "percentage": 2.994828928716416e-05}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "F", "AGEGROUP_sc": "65-74", "MS_POPULATION": 353925, "AGEGROUP": "65-74", "SEX": "F", "DEATHS": 67, "percentage": 0.0001893056438510984}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "F", "AGEGROUP_sc": "75-84", "MS_POPULATION": 245981, "AGEGROUP": "75-84", "SEX": "F", "DEATHS": 199, "percentage": 0.0008090055736012131}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "F", "AGEGROUP_sc": "85+", "MS_POPULATION": 132649, "AGEGROUP": "85+", "SEX": "F", "DEATHS": 232, "percentage": 0.0017489766225150586}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "M", "AGEGROUP_sc": "25-44", "MS_POPULATION": 827281, "AGEGROUP": "25-44", "SEX": "M", "DEATHS": 3, "percentage": 3.626337362999996e-06}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "M", "AGEGROUP_sc": "45-64", "MS_POPULATION": 917008, "AGEGROUP": "45-64", "SEX": "M", "DEATHS": 63, "percentage": 6.870169071589342e-05}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "M", "AGEGROUP_sc": "65-74", "MS_POPULATION": 336242, "AGEGROUP": "65-74", "SEX": "M", "DEATHS": 130, "percentage": 0.0003866262989156619}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "M", "AGEGROUP_sc": "75-84", "MS_POPULATION": 193576, "AGEGROUP": "75-84", "SEX": "M", "DEATHS": 335, "percentage": 0.001730586436335083}, {"TX_RGN_DESCR_NL": "Vlaams Gewest", "CD_SEX": "M", "AGEGROUP_sc": "85+", "MS_POPULATION": 69678, "AGEGROUP": "85+", "SEX": "M", "DEATHS": 309, "percentage": 0.004434685266511668}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "F", "AGEGROUP_sc": "25-44", "MS_POPULATION": 457356, "AGEGROUP": "25-44", "SEX": "F", "DEATHS": 5, "percentage": 1.0932402767209788e-05}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "F", "AGEGROUP_sc": "45-64", "MS_POPULATION": 496668, "AGEGROUP": "45-64", "SEX": "F", "DEATHS": 41, "percentage": 8.255011395942561e-05}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "F", "AGEGROUP_sc": "65-74", "MS_POPULATION": 199422, "AGEGROUP": "65-74", "SEX": "F", "DEATHS": 98, "percentage": 0.0004914202043906891}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "F", "AGEGROUP_sc": "75-84", "MS_POPULATION": 118224, "AGEGROUP": "75-84", "SEX": "F", "DEATHS": 290, "percentage": 0.002452970632020571}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "F", "AGEGROUP_sc": "85+", "MS_POPULATION": 68502, "AGEGROUP": "85+", "SEX": "F", "DEATHS": 704, "percentage": 0.010277072202271467}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "M", "AGEGROUP_sc": "25-44", "MS_POPULATION": 459444, "AGEGROUP": "25-44", "SEX": "M", "DEATHS": 4, "percentage": 8.706175290133292e-06}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "M", "AGEGROUP_sc": "45-64", "MS_POPULATION": 487322, "AGEGROUP": "45-64", "SEX": "M", "DEATHS": 89, "percentage": 0.0001826307862152745}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "M", "AGEGROUP_sc": "65-74", "MS_POPULATION": 175508, "AGEGROUP": "65-74", "SEX": "M", "DEATHS": 186, "percentage": 0.0010597807507350093}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "M", "AGEGROUP_sc": "75-84", "MS_POPULATION": 82876, "AGEGROUP": "75-84", "SEX": "M", "DEATHS": 300, "percentage": 0.003619865823640137}, {"TX_RGN_DESCR_NL": "Waals Gewest", "CD_SEX": "M", "AGEGROUP_sc": "85+", "MS_POPULATION": 30048, "AGEGROUP": "85+", "SEX": "M", "DEATHS": 421, "percentage": 0.014010915867944621}]}}, {"mode": "vega-lite"});
</script>




```

```
<!-- more -->

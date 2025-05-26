---
title: Evolution of burglary in Leuven. Is the trend downwards ?
date: 2020-02-15
created_at: 2020-02-15T10:44:22.941081
last_modified: 2020-02-15T10:44:22.941087
---
# Evolution of burglary in Leuven. Is the trend downwards ?

The local police shared [a graph](https://www.politie.be/5388/nieuws/inbraken-op-leuvens-grondgebied-zijn-in-2019-opnieuw-gedaald) with the number of break-ins in Leuven per year.  The article shows a graph with a downwards trendline. Can we conclude that the number of breakins is showing a downward trend based on those numbers? Let's construct a dataframe with the data from the graph.

```python
import numpy as np
import pandas as pd
import altair as alt

df = pd.DataFrame({'year_int':[y for y in range(2006, 2020)], 
                  'breakins':[1133,834,953,891,1006,1218,992,1079,1266,1112,713,669,730,644]})
df['year'] = pd.to_datetime(df['year_int'], format='%Y')
```

```python
points = alt.Chart(df).mark_line(point=True).encode(
    x='year', y='breakins', tooltip='breakins'
)
points + points.transform_regression('year', 'breakins').mark_line(
    color='green'
).properties(
    title='Regression trend on the number breakins per year in Leuven'
)
```

<div id="altair-viz-649b49ee9d1f44799a0e200be12c8f06"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-649b49ee9d1f44799a0e200be12c8f06") {
      outputDiv = document.getElementById("altair-viz-649b49ee9d1f44799a0e200be12c8f06");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "layer": [{"mark": {"type": "line", "point": true}, "encoding": {"tooltip": {"type": "quantitative", "field": "breakins"}, "x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins"}}}, {"mark": {"type": "line", "color": "green"}, "encoding": {"tooltip": {"type": "quantitative", "field": "breakins"}, "x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins"}}, "title": "Regression trend on the number breakins per year in Leuven", "transform": [{"on": "year", "regression": "breakins"}]}], "data": {"name": "data-e69c4a4577c6a9d2a03c89854c9a4599"}, "$schema": "<https://vega.github.io/schema/vega-lite/v4.8.1.json>", "datasets": {"data-e69c4a4577c6a9d2a03c89854c9a4599": [{"year_int": 2006, "breakins": 1133, "year": "2006-01-01T00:00:00"}, {"year_int": 2007, "breakins": 834, "year": "2007-01-01T00:00:00"}, {"year_int": 2008, "breakins": 953, "year": "2008-01-01T00:00:00"}, {"year_int": 2009, "breakins": 891, "year": "2009-01-01T00:00:00"}, {"year_int": 2010, "breakins": 1006, "year": "2010-01-01T00:00:00"}, {"year_int": 2011, "breakins": 1218, "year": "2011-01-01T00:00:00"}, {"year_int": 2012, "breakins": 992, "year": "2012-01-01T00:00:00"}, {"year_int": 2013, "breakins": 1079, "year": "2013-01-01T00:00:00"}, {"year_int": 2014, "breakins": 1266, "year": "2014-01-01T00:00:00"}, {"year_int": 2015, "breakins": 1112, "year": "2015-01-01T00:00:00"}, {"year_int": 2016, "breakins": 713, "year": "2016-01-01T00:00:00"}, {"year_int": 2017, "breakins": 669, "year": "2017-01-01T00:00:00"}, {"year_int": 2018, "breakins": 730, "year": "2018-01-01T00:00:00"}, {"year_int": 2019, "breakins": 644, "year": "2019-01-01T00:00:00"}]}}, {"mode": "vega-lite"});
</script>

The article claims that the number of breakins stabilizes the last years. Let's perform a local regression to check that.

```python
# https://opendatascience.com/local-regression-in-python
# Loess: https://gist.github.com/AllenDowney/818f6153ef316aee80467c51faee80f8
points + points.transform_loess('year', 'breakins').mark_line(
    color='green'
).properties(
    title='Local regression trend on the number breakins per year in Leuven'
)
```

<div id="altair-viz-524d27ed46b142359cdc597a05a024eb"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-524d27ed46b142359cdc597a05a024eb") {
      outputDiv = document.getElementById("altair-viz-524d27ed46b142359cdc597a05a024eb");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "layer": [{"mark": {"type": "line", "point": true}, "encoding": {"tooltip": {"type": "quantitative", "field": "breakins"}, "x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins"}}}, {"mark": {"type": "line", "color": "green"}, "encoding": {"tooltip": {"type": "quantitative", "field": "breakins"}, "x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins"}}, "title": "Local regression trend on the number breakins per year in Leuven", "transform": [{"loess": "breakins", "on": "year"}]}], "data": {"name": "data-e69c4a4577c6a9d2a03c89854c9a4599"}, "$schema": "<https://vega.github.io/schema/vega-lite/v4.8.1.json>", "datasets": {"data-e69c4a4577c6a9d2a03c89854c9a4599": [{"year_int": 2006, "breakins": 1133, "year": "2006-01-01T00:00:00"}, {"year_int": 2007, "breakins": 834, "year": "2007-01-01T00:00:00"}, {"year_int": 2008, "breakins": 953, "year": "2008-01-01T00:00:00"}, {"year_int": 2009, "breakins": 891, "year": "2009-01-01T00:00:00"}, {"year_int": 2010, "breakins": 1006, "year": "2010-01-01T00:00:00"}, {"year_int": 2011, "breakins": 1218, "year": "2011-01-01T00:00:00"}, {"year_int": 2012, "breakins": 992, "year": "2012-01-01T00:00:00"}, {"year_int": 2013, "breakins": 1079, "year": "2013-01-01T00:00:00"}, {"year_int": 2014, "breakins": 1266, "year": "2014-01-01T00:00:00"}, {"year_int": 2015, "breakins": 1112, "year": "2015-01-01T00:00:00"}, {"year_int": 2016, "breakins": 713, "year": "2016-01-01T00:00:00"}, {"year_int": 2017, "breakins": 669, "year": "2017-01-01T00:00:00"}, {"year_int": 2018, "breakins": 730, "year": "2018-01-01T00:00:00"}, {"year_int": 2019, "breakins": 644, "year": "2019-01-01T00:00:00"}]}}, {"mode": "vega-lite"});
</script>

But what about the trend line? Are we sure the trend is negative ? Bring in the code based on the blogpost [The hacker's guide to uncertainty estimates](https://erikbern.com/2018/10/08/the-hackers-guide-to-uncertainty-estimates.html) to estimate the uncertainty.:

```python
# Code from: https://erikbern.com/2018/10/08/the-hackers-guide-to-uncertainty-estimates.html
import scipy.optimize
import random

def model(xs, k, m):
    return k * xs + m

def neg_log_likelihood(tup, xs, ys):
    # Since sigma > 0, we use use log(sigma) as the parameter instead.
    # That way we have an unconstrained problem.
    k, m, log_sigma = tup
    sigma = np.exp(log_sigma)
    delta = model(xs, k, m) - ys
    return len(xs)/2*np.log(2*np.pi*sigma**2) + \
        np.dot(delta, delta) / (2*sigma**2)

def confidence_bands(xs, ys, nr_bootstrap):
    curves = []
    xys = list(zip(xs, ys))
    for i in range(nr_bootstrap):
        # sample with replacement
        bootstrap = [random.choice(xys) for _ in xys]
        xs_bootstrap = np.array([x for x, y in bootstrap])
        ys_bootstrap = np.array([y for x, y in bootstrap])
        k_hat, m_hat, log_sigma_hat = scipy.optimize.minimize(
          neg_log_likelihood, (0, 0, 0), args=(xs_bootstrap, ys_bootstrap)
        ).x
        curves.append(
          model(xs, k_hat, m_hat) +
          # Note what's going on here: we're _adding_ the random term
          # to the predictions!
          np.exp(log_sigma_hat) * np.random.normal(size=xs.shape)
        )
    lo, hi = np.percentile(curves, (2.5, 97.5), axis=0)
    return lo, hi
```

```python
# Make a plot with a confidence band
df['lo'], df['hi'] = confidence_bands(df.index, df['breakins'], 100)

ci = alt.Chart(df).mark_area().encode(
    x=alt.X('year:T', title=''),
    y=alt.Y('lo:Q'),
    y2=alt.Y2('hi:Q', title=''),
    color=alt.value('lightblue'),
    opacity=alt.value(0.6)
)

chart = alt.Chart(df).mark_line(point=True).encode(
    x='year', y='breakins', tooltip='breakins'
)
ci + chart  + chart.transform_regression('year', 'breakins').mark_line(
    color='red'
).properties(
    title='95% Confidence band of the number of breakins per year in Leuven'
)
```

<div id="altair-viz-56dc093b04d8402a94d0ac71f2593c00"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-56dc093b04d8402a94d0ac71f2593c00") {
      outputDiv = document.getElementById("altair-viz-56dc093b04d8402a94d0ac71f2593c00");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "layer": [{"mark": "area", "encoding": {"color": {"value": "lightblue"}, "opacity": {"value": 0.6}, "x": {"type": "temporal", "field": "year", "title": ""}, "y": {"type": "quantitative", "field": "lo"}, "y2": {"field": "hi", "title": ""}}}, {"mark": {"type": "line", "point": true}, "encoding": {"tooltip": {"type": "quantitative", "field": "breakins"}, "x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins"}}}, {"mark": {"type": "line", "color": "red"}, "encoding": {"tooltip": {"type": "quantitative", "field": "breakins"}, "x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins"}}, "title": "95% Confidence band of the number of breakins per year in Leuven", "transform": [{"on": "year", "regression": "breakins"}]}], "data": {"name": "data-8fd2b6cf615cc0d07dec80616bd3be4e"}, "$schema": "<https://vega.github.io/schema/vega-lite/v4.8.1.json>", "datasets": {"data-8fd2b6cf615cc0d07dec80616bd3be4e": [{"year_int": 2006, "breakins": 1133, "year": "2006-01-01T00:00:00", "lo": 682.3099189747738, "hi": 1440.1937739145749}, {"year_int": 2007, "breakins": 834, "year": "2007-01-01T00:00:00", "lo": 827.6367340730125, "hi": 1486.4533262933012}, {"year_int": 2008, "breakins": 953, "year": "2008-01-01T00:00:00", "lo": 767.7635624924901, "hi": 1413.1424597103937}, {"year_int": 2009, "breakins": 891, "year": "2009-01-01T00:00:00", "lo": 790.4391898489782, "hi": 1419.3697631793243}, {"year_int": 2010, "breakins": 1006, "year": "2010-01-01T00:00:00", "lo": 708.9776311994685, "hi": 1343.5757675169857}, {"year_int": 2011, "breakins": 1218, "year": "2011-01-01T00:00:00", "lo": 727.1312799998013, "hi": 1309.4075604214133}, {"year_int": 2012, "breakins": 992, "year": "2012-01-01T00:00:00", "lo": 648.99978279176, "hi": 1290.1317136935718}, {"year_int": 2013, "breakins": 1079, "year": "2013-01-01T00:00:00", "lo": 654.8634472984102, "hi": 1235.404320558902}, {"year_int": 2014, "breakins": 1266, "year": "2014-01-01T00:00:00", "lo": 610.3003882798392, "hi": 1215.073440406832}, {"year_int": 2015, "breakins": 1112, "year": "2015-01-01T00:00:00", "lo": 577.2201952999367, "hi": 1261.770162301932}, {"year_int": 2016, "breakins": 713, "year": "2016-01-01T00:00:00", "lo": 593.6374616517471, "hi": 1220.5302754770032}, {"year_int": 2017, "breakins": 669, "year": "2017-01-01T00:00:00", "lo": 549.4776941065223, "hi": 1225.3267389185412}, {"year_int": 2018, "breakins": 730, "year": "2018-01-01T00:00:00", "lo": 506.8580347349176, "hi": 1102.1741859626663}, {"year_int": 2019, "breakins": 644, "year": "2019-01-01T00:00:00", "lo": 508.7175615577154, "hi": 1180.8263041098646}]}}, {"mode": "vega-lite"});
</script>

On the above chart, we see that a possitive trend might be possible as well.

# Linear regression

Let's perform a linear regression with statsmodel to calculate the confidence interval on the slope of the regression line.

```python
import statsmodels.formula.api as smf
```

```python
results = smf.ols('breakins ~ index', data=df.reset_index()).fit()
```

```python
results.params
```

    Intercept    1096.314286
    index         -23.169231
    dtype: float64

The most likely slope of the trend line is 23.17 breakins per year. But how sure are we that the trend is heading down ?

```python
results.summary()
```

    C:\Users\lnh6dt5\AppData\Local\Continuum\anaconda3\lib\site-packages\scipy\stats\stats.py:1535: UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=14
      "anyway, n=%i" % int(n))

<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>        <td>breakins</td>     <th>  R-squared:         </th> <td>   0.223</td>
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.159</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   3.451</td>
</tr>
<tr>
  <th>Date:</th>             <td>Sun, 19 Apr 2020</td> <th>  Prob (F-statistic):</th>  <td>0.0879</td>
</tr>
<tr>
  <th>Time:</th>                 <td>10:26:45</td>     <th>  Log-Likelihood:    </th> <td> -92.105</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>    14</td>      <th>  AIC:               </th> <td>   188.2</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>    12</td>      <th>  BIC:               </th> <td>   189.5</td>
</tr>
<tr>
  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>     <td> </td>
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>
</tr>
</table>
<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>Intercept</th> <td> 1096.3143</td> <td>   95.396</td> <td>   11.492</td> <td> 0.000</td> <td>  888.465</td> <td> 1304.164</td>
</tr>
<tr>
  <th>index</th>     <td>  -23.1692</td> <td>   12.472</td> <td>   -1.858</td> <td> 0.088</td> <td>  -50.344</td> <td>    4.006</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td> 1.503</td> <th>  Durbin-Watson:     </th> <td>   1.035</td>
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.472</td> <th>  Jarque-Bera (JB):  </th> <td>   1.196</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 0.577</td> <th>  Prob(JB):          </th> <td>   0.550</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 2.153</td> <th>  Cond. No.          </th> <td>    14.7</td>
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

The analysis reveals that the slope of the best fitting regression line is 23 breakins less per year. However, the confidence interval of the trend is between -50.344 and 4.006. Also the p)value of the regression coefficient is 0.088. Meaning we have eight percent chance that the negative trend is by accident. Hence, based on the current data we are not 95% percent sure the trend is downwards. Hence we can not conclude, based on this data, that there is a negative trend. This corresponds with the width of the 95% certainty band drawn that allows for an upward trend line:

```python
# Here are the confidence intervals of the regression
results.conf_int()
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
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Intercept</th>
      <td>888.464586</td>
      <td>1304.163986</td>
    </tr>
    <tr>
      <th>index</th>
      <td>-50.344351</td>
      <td>4.005889</td>
    </tr>
  </tbody>
</table>
</div>

```python
y_low  = results.params['Intercept'] # ?ost likely value of the intercept
y_high = results.params['Intercept'] + results.conf_int()[1]['index'] * df.shape[0] # Value of upward trend for the last year
df_upward_trend = pd.DataFrame({'year':[df['year'].min(), df['year'].max()], 
                                'breakins':[y_low, y_high]})
possible_upwards_trend = alt.Chart(df_upward_trend).mark_line(
    color='green',
    strokeDash=[10,10]
).encode(
    x='year:T',
    y=alt.Y('breakins:Q',
    title='Number of breakins per year')
)

points = alt.Chart(df).mark_line(point=True).encode(x='year', y='breakins', tooltip='breakins')
(ci + points  + points.transform_regression('year', 'breakins').mark_line(color='red') 
              + possible_upwards_trend).properties(
    title='Trend analysis on the number of breakins per year in Leuven, Belgium'
)
```

<div id="altair-viz-9136ba2616714a16adfdcaf66be8277b"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-9136ba2616714a16adfdcaf66be8277b") {
      outputDiv = document.getElementById("altair-viz-9136ba2616714a16adfdcaf66be8277b");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "layer": [{"mark": "area", "encoding": {"color": {"value": "lightblue"}, "opacity": {"value": 0.6}, "x": {"type": "temporal", "field": "year", "title": ""}, "y": {"type": "quantitative", "field": "lo"}, "y2": {"field": "hi", "title": ""}}}, {"mark": {"type": "line", "point": true}, "encoding": {"tooltip": {"type": "quantitative", "field": "breakins"}, "x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins"}}}, {"mark": {"type": "line", "color": "red"}, "encoding": {"tooltip": {"type": "quantitative", "field": "breakins"}, "x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins"}}, "transform": [{"on": "year", "regression": "breakins"}]}, {"data": {"name": "data-4de61dc9bf5700a168cfe5e53e79ee67"}, "mark": {"type": "line", "color": "green", "strokeDash": [10, 10]}, "encoding": {"x": {"type": "temporal", "field": "year"}, "y": {"type": "quantitative", "field": "breakins", "title": "Number of breakins per year"}}}], "data": {"name": "data-8fd2b6cf615cc0d07dec80616bd3be4e"}, "title": "Trend analysis on the number of breakins per year in Leuven, Belgium", "$schema": "<https://vega.github.io/schema/vega-lite/v4.8.1.json>", "datasets": {"data-8fd2b6cf615cc0d07dec80616bd3be4e": [{"year_int": 2006, "breakins": 1133, "year": "2006-01-01T00:00:00", "lo": 682.3099189747738, "hi": 1440.1937739145749}, {"year_int": 2007, "breakins": 834, "year": "2007-01-01T00:00:00", "lo": 827.6367340730125, "hi": 1486.4533262933012}, {"year_int": 2008, "breakins": 953, "year": "2008-01-01T00:00:00", "lo": 767.7635624924901, "hi": 1413.1424597103937}, {"year_int": 2009, "breakins": 891, "year": "2009-01-01T00:00:00", "lo": 790.4391898489782, "hi": 1419.3697631793243}, {"year_int": 2010, "breakins": 1006, "year": "2010-01-01T00:00:00", "lo": 708.9776311994685, "hi": 1343.5757675169857}, {"year_int": 2011, "breakins": 1218, "year": "2011-01-01T00:00:00", "lo": 727.1312799998013, "hi": 1309.4075604214133}, {"year_int": 2012, "breakins": 992, "year": "2012-01-01T00:00:00", "lo": 648.99978279176, "hi": 1290.1317136935718}, {"year_int": 2013, "breakins": 1079, "year": "2013-01-01T00:00:00", "lo": 654.8634472984102, "hi": 1235.404320558902}, {"year_int": 2014, "breakins": 1266, "year": "2014-01-01T00:00:00", "lo": 610.3003882798392, "hi": 1215.073440406832}, {"year_int": 2015, "breakins": 1112, "year": "2015-01-01T00:00:00", "lo": 577.2201952999367, "hi": 1261.770162301932}, {"year_int": 2016, "breakins": 713, "year": "2016-01-01T00:00:00", "lo": 593.6374616517471, "hi": 1220.5302754770032}, {"year_int": 2017, "breakins": 669, "year": "2017-01-01T00:00:00", "lo": 549.4776941065223, "hi": 1225.3267389185412}, {"year_int": 2018, "breakins": 730, "year": "2018-01-01T00:00:00", "lo": 506.8580347349176, "hi": 1102.1741859626663}, {"year_int": 2019, "breakins": 644, "year": "2019-01-01T00:00:00", "lo": 508.7175615577154, "hi": 1180.8263041098646}], "data-4de61dc9bf5700a168cfe5e53e79ee67": [{"year": "2006-01-01T00:00:00", "breakins": 1096.314285714286}, {"year": "2019-01-01T00:00:00", "breakins": 1152.3967336789888}]}}, {"mode": "vega-lite"});
</script>

In the above graph, we see that a slight positive trend (green dashed line) is in the 95% confidence band on the regression coefficient. We are not sure that the trend on the number of breakins is downwards.

```python

```
<!-- more -->

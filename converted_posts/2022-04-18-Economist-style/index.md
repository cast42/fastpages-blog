---
title: Reconstructing Economist graph with Altair
date: 2022-04-18
created_at: 2022-04-18T10:44:22.941081
last_modified: 2022-04-18T10:44:22.941087
---
# "Reconstructing Economist graph with Altair"

\#30DayChartChallenge \#altair \#day12



In an Economist article ["The metamorphosis: How Jeremy Corbyn took control of Labour"](https://www.economist.com/britain/2016/08/13/the-metamorphosis), the following graph appeared:

![](https://www.economist.com/img/b/400/363/90/sites/default/files/20160813_BRC304_0.png "Credit: https://www.economist.com/britain/2016/08/13/the-metamorphosis")

Later, [Sarah Leo](https://twitter.com/misssarahleo?lang=nl), data visualiser at The Economist, improved the graph to:

![](https://miro.medium.com/max/875/1*9QE_yL3boSLqopJkSBfL5A.png "Credit: https://twitter.com/misssarahleo?lang=nl")
The rationale behind this improvement is discussed in her article: ['Mistakes, we made a few'](
https://medium.economist.com/mistakes-weve-drawn-a-few-8cdd8a42d368).

In this article, I show how visualisation library Altair can be used to reconstruct the improved graph.


```python
import numpy as np
import pandas as pd
import altair as alt
```

Read the data for the graph into a Pandas dataframe:


```python
df = pd.read_csv('http://infographics.economist.com/databank/Economist_corbyn.csv').dropna()
```

This is how the data looks:


```python
df
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
      <th>Page</th>
      <th>Average number of likes per Facebook post 2016</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jeremy Corbyn</td>
      <td>5210.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Labour Party</td>
      <td>845.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Momentum</td>
      <td>229.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Owen Smith</td>
      <td>127.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andy Burnham</td>
      <td>105.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Saving Labour</td>
      <td>56.0</td>
    </tr>
  </tbody>
</table>
</div>



A standard bar graph in Altair gives this:


```python
alt.Chart(df).mark_bar().encode(
    x='Average number of likes per Facebook post 2016:Q',
    y='Page:O'
)
```





<div id="altair-viz-2028adcb520c41f5ba7c39708b6dbd85"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-2028adcb520c41f5ba7c39708b6dbd85") {
      outputDiv = document.getElementById("altair-viz-2028adcb520c41f5ba7c39708b6dbd85");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
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
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-37b1b21769609e0260f58cacd3f745f7"}, "mark": "bar", "encoding": {"x": {"field": "Average number of likes per Facebook post 2016", "type": "quantitative"}, "y": {"field": "Page", "type": "ordinal"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-37b1b21769609e0260f58cacd3f745f7": [{"Page": "Jeremy Corbyn", "Average number of likes per Facebook post 2016": 5210.0}, {"Page": "Labour Party", "Average number of likes per Facebook post 2016": 845.0}, {"Page": "Momentum", "Average number of likes per Facebook post 2016": 229.0}, {"Page": "Owen Smith", "Average number of likes per Facebook post 2016": 127.0}, {"Page": "Andy Burnham ", "Average number of likes per Facebook post 2016": 105.0}, {"Page": "Saving Labour", "Average number of likes per Facebook post 2016": 56.0}]}}, {"mode": "vega-lite"});
</script>



The message of the graph is that Jerermy Corbyn has by far the most likes per Facebook post in 2016. There are a number of improvements possible:

The number on the x-axis are multiple of thousands. In spirit of removing as much inkt as possible, let's rescale the x-asis with factor 1000.
The label 'Page' on the y-axis is superfluous. Let's remove it.


```python
df['page1k'] = df['Average number of likes per Facebook post 2016']/1000.0
```

After scaling the graphs looks like this:


```python
alt.Chart(df).mark_bar().encode(
    x=alt.X('page1k', title='Average number of likes per Facebook post 2016'),
    y=alt.Y('Page:O', title='')
)
```





<div id="altair-viz-66c5e9ed26374bc6bd869b3a2bd8d62c"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-66c5e9ed26374bc6bd869b3a2bd8d62c") {
      outputDiv = document.getElementById("altair-viz-66c5e9ed26374bc6bd869b3a2bd8d62c");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
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
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-1913a809e59f1dfc25bb5719e6f7f706"}, "mark": "bar", "encoding": {"x": {"field": "page1k", "title": "Average number of likes per Facebook post 2016", "type": "quantitative"}, "y": {"field": "Page", "title": "", "type": "ordinal"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-1913a809e59f1dfc25bb5719e6f7f706": [{"Page": "Jeremy Corbyn", "Average number of likes per Facebook post 2016": 5210.0, "page1k": 5.21}, {"Page": "Labour Party", "Average number of likes per Facebook post 2016": 845.0, "page1k": 0.845}, {"Page": "Momentum", "Average number of likes per Facebook post 2016": 229.0, "page1k": 0.229}, {"Page": "Owen Smith", "Average number of likes per Facebook post 2016": 127.0, "page1k": 0.127}, {"Page": "Andy Burnham ", "Average number of likes per Facebook post 2016": 105.0, "page1k": 0.105}, {"Page": "Saving Labour", "Average number of likes per Facebook post 2016": 56.0, "page1k": 0.056}]}}, {"mode": "vega-lite"});
</script>



A third improvement is to sort the bars from high to low. This supports the message, Jeremy Corbyn has the most clicks.


```python
alt.Chart(df).mark_bar().encode(
    x=alt.X('page1k:Q', title='Average number of likes per Facebook post 2016'),
    y=alt.Y('Page:O', title='', sort=alt.EncodingSortField(
            field="Average number of likes per Facebook post 2016:Q",  # The field to use for the sort
            op="sum",  # The operation to run on the field prior to sorting
            order="ascending"  # The order to sort in
        ))
)
```





<div id="altair-viz-cd35fb523fa64e0ba36aa0ad2f8af0fb"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-cd35fb523fa64e0ba36aa0ad2f8af0fb") {
      outputDiv = document.getElementById("altair-viz-cd35fb523fa64e0ba36aa0ad2f8af0fb");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
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
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-1913a809e59f1dfc25bb5719e6f7f706"}, "mark": "bar", "encoding": {"x": {"field": "page1k", "title": "Average number of likes per Facebook post 2016", "type": "quantitative"}, "y": {"field": "Page", "sort": {"field": "Average number of likes per Facebook post 2016:Q", "op": "sum", "order": "ascending"}, "title": "", "type": "ordinal"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-1913a809e59f1dfc25bb5719e6f7f706": [{"Page": "Jeremy Corbyn", "Average number of likes per Facebook post 2016": 5210.0, "page1k": 5.21}, {"Page": "Labour Party", "Average number of likes per Facebook post 2016": 845.0, "page1k": 0.845}, {"Page": "Momentum", "Average number of likes per Facebook post 2016": 229.0, "page1k": 0.229}, {"Page": "Owen Smith", "Average number of likes per Facebook post 2016": 127.0, "page1k": 0.127}, {"Page": "Andy Burnham ", "Average number of likes per Facebook post 2016": 105.0, "page1k": 0.105}, {"Page": "Saving Labour", "Average number of likes per Facebook post 2016": 56.0, "page1k": 0.056}]}}, {"mode": "vega-lite"});
</script>



Now, we see that we have to many ticks on the x-axis. We can add a scale and map the x-axis to integers to cope with that. While adding markup for the x-axis, we add orient='top'. That move the xlabel text to the top of the graph.


```python
alt.Chart(df).mark_bar().encode(
    x=alt.X('page1k:Q', title='Average number of likes per Facebook post 2016',
            axis=alt.Axis(title='Average number of likes per Facebook post 2016', orient="top", format='d', values=[1,2,3,4,5,6]),
            scale=alt.Scale(round=True, domain=[0,6])),
    y=alt.Y('Page:O', title='', sort=alt.EncodingSortField(
            field="Average number of likes per Facebook post 2016:Q",  # The field to use for the sort
            op="sum",  # The operation to run on the field prior to sorting
            order="ascending"  # The order to sort in
        ))
)
```





<div id="altair-viz-88eda3b8382040fbb4241afc459a247f"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-88eda3b8382040fbb4241afc459a247f") {
      outputDiv = document.getElementById("altair-viz-88eda3b8382040fbb4241afc459a247f");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
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
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-1913a809e59f1dfc25bb5719e6f7f706"}, "mark": "bar", "encoding": {"x": {"axis": {"format": "d", "orient": "top", "title": "Average number of likes per Facebook post 2016", "values": [1, 2, 3, 4, 5, 6]}, "field": "page1k", "scale": {"domain": [0, 6], "round": true}, "title": "Average number of likes per Facebook post 2016", "type": "quantitative"}, "y": {"field": "Page", "sort": {"field": "Average number of likes per Facebook post 2016:Q", "op": "sum", "order": "ascending"}, "title": "", "type": "ordinal"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-1913a809e59f1dfc25bb5719e6f7f706": [{"Page": "Jeremy Corbyn", "Average number of likes per Facebook post 2016": 5210.0, "page1k": 5.21}, {"Page": "Labour Party", "Average number of likes per Facebook post 2016": 845.0, "page1k": 0.845}, {"Page": "Momentum", "Average number of likes per Facebook post 2016": 229.0, "page1k": 0.229}, {"Page": "Owen Smith", "Average number of likes per Facebook post 2016": 127.0, "page1k": 0.127}, {"Page": "Andy Burnham ", "Average number of likes per Facebook post 2016": 105.0, "page1k": 0.105}, {"Page": "Saving Labour", "Average number of likes per Facebook post 2016": 56.0, "page1k": 0.056}]}}, {"mode": "vega-lite"});
</script>



Now, we want to remove the x-axis itself as it adds nothing extra. We do that by putting the stroke at None in the configure_view. We also adjust the x-axis title to make clear the numbers are multiples of thousands.


```python
alt.Chart(df).mark_bar().encode(
    x=alt.X('page1k:Q', title="Average number of likes per Facebook post 2016  ('000)",
            axis=alt.Axis(title='Average number of likes per Facebook post 2016', orient="top", format='d', values=[1,2,3,4,5,6]),
            scale=alt.Scale(round=True, domain=[0,6])),
    y=alt.Y('Page:O', title='', sort=alt.EncodingSortField(
            field="Average number of likes per Facebook post 2016:Q",  # The field to use for the sort
            op="sum",  # The operation to run on the field prior to sorting
            order="ascending"  # The order to sort in
        ))
).configure_view(
    stroke=None, # Remove box around graph
)
```





<div id="altair-viz-b12d657e69db4d56ad0be37ebdf61fb0"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-b12d657e69db4d56ad0be37ebdf61fb0") {
      outputDiv = document.getElementById("altair-viz-b12d657e69db4d56ad0be37ebdf61fb0");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
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
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300, "stroke": null}}, "data": {"name": "data-1913a809e59f1dfc25bb5719e6f7f706"}, "mark": "bar", "encoding": {"x": {"axis": {"format": "d", "orient": "top", "title": "Average number of likes per Facebook post 2016", "values": [1, 2, 3, 4, 5, 6]}, "field": "page1k", "scale": {"domain": [0, 6], "round": true}, "title": "Average number of likes per Facebook post 2016  ('000)", "type": "quantitative"}, "y": {"field": "Page", "sort": {"field": "Average number of likes per Facebook post 2016:Q", "op": "sum", "order": "ascending"}, "title": "", "type": "ordinal"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-1913a809e59f1dfc25bb5719e6f7f706": [{"Page": "Jeremy Corbyn", "Average number of likes per Facebook post 2016": 5210.0, "page1k": 5.21}, {"Page": "Labour Party", "Average number of likes per Facebook post 2016": 845.0, "page1k": 0.845}, {"Page": "Momentum", "Average number of likes per Facebook post 2016": 229.0, "page1k": 0.229}, {"Page": "Owen Smith", "Average number of likes per Facebook post 2016": 127.0, "page1k": 0.127}, {"Page": "Andy Burnham ", "Average number of likes per Facebook post 2016": 105.0, "page1k": 0.105}, {"Page": "Saving Labour", "Average number of likes per Facebook post 2016": 56.0, "page1k": 0.056}]}}, {"mode": "vega-lite"});
</script>



Next we try to left align the y-axis labels:


```python
alt.Chart(df).mark_bar().encode(
    x=alt.X('page1k:Q',
            axis=alt.Axis(title="Average number of likes per Facebook post 2016  ('000)", orient="top", format='d', values=[1,2,3,4,5,6]),
            scale=alt.Scale(round=True, domain=[0,6])),
    y=alt.Y('Page:O', title='', sort=alt.EncodingSortField(
            field="Average number of likes per Facebook post 2016:Q",  # The field to use for the sort
            op="sum",  # The operation to run on the field prior to sorting
            order="ascending"  # The order to sort in
        ))
).configure_view(
    stroke=None, # Remove box around graph
).configure_axisY(
    labelPadding=70,
    labelAlign='left'
)
```





<div id="altair-viz-87d1289164334e3aa3b878db78924909"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-87d1289164334e3aa3b878db78924909") {
      outputDiv = document.getElementById("altair-viz-87d1289164334e3aa3b878db78924909");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
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
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300, "stroke": null}, "axisY": {"labelAlign": "left", "labelPadding": 70}}, "data": {"name": "data-1913a809e59f1dfc25bb5719e6f7f706"}, "mark": "bar", "encoding": {"x": {"axis": {"format": "d", "orient": "top", "title": "Average number of likes per Facebook post 2016  ('000)", "values": [1, 2, 3, 4, 5, 6]}, "field": "page1k", "scale": {"domain": [0, 6], "round": true}, "type": "quantitative"}, "y": {"field": "Page", "sort": {"field": "Average number of likes per Facebook post 2016:Q", "op": "sum", "order": "ascending"}, "title": "", "type": "ordinal"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-1913a809e59f1dfc25bb5719e6f7f706": [{"Page": "Jeremy Corbyn", "Average number of likes per Facebook post 2016": 5210.0, "page1k": 5.21}, {"Page": "Labour Party", "Average number of likes per Facebook post 2016": 845.0, "page1k": 0.845}, {"Page": "Momentum", "Average number of likes per Facebook post 2016": 229.0, "page1k": 0.229}, {"Page": "Owen Smith", "Average number of likes per Facebook post 2016": 127.0, "page1k": 0.127}, {"Page": "Andy Burnham ", "Average number of likes per Facebook post 2016": 105.0, "page1k": 0.105}, {"Page": "Saving Labour", "Average number of likes per Facebook post 2016": 56.0, "page1k": 0.056}]}}, {"mode": "vega-lite"});
</script>



Now, we apply the Economist style:


```python
square = alt.Chart().mark_rect(width=50, height=18, color='#EB111A', xOffset=-105, yOffset=10)

bars = alt.Chart(df).mark_bar().encode(
    x=alt.X('page1k:Q',
            axis=alt.Axis(title="", orient="top", format='d', values=[1,2,3,4,5,6], labelFontSize=14),
            scale=alt.Scale(round=True, domain=[0,6])),
    y=alt.Y('Page:O', title='', sort=alt.EncodingSortField(
            field="Average number of likes per Facebook post 2016:Q",  # The field to use for the sort
            op="sum",  # The operation to run on the field prior to sorting
            order="ascending"  # The order to sort in
        ),
        # Based on https://stackoverflow.com/questions/66684882/color-some-x-labels-in-altair-plot
        axis=alt.Axis(labelFontSize=14, labelFontStyle=alt.condition('datum.value == "Jeremy Corbyn"', alt.value('bold'), alt.value('italic'))))
).properties(title={
      "text": ["Left Click", ],
      "subtitle": ["Average number of likes per Facebook post\n", "2016, '000"],
      "align": 'left',
      "anchor": 'start'
    }
)

source = alt.Chart(
    {"values": [{"text": "Source: Facebook"}]}
).mark_text(size=12, align='left', dx=-120, color='darkgrey').encode(
    text="text:N"
)

# from https://stackoverflow.com/questions/57244390/has-anyone-figured-out-a-workaround-to-add-a-subtitle-to-an-altair-generated-cha
chart = alt.vconcat(
    square,
    bars,
    source
).configure_concat(
    spacing=0
).configure(
    background='#D9E9F0'
).configure_view(
    stroke=None, # Remove box around graph
).configure_axisY(
    labelPadding=110,
    labelAlign='left',
    ticks=False,
    grid=False
).configure_title(
    fontSize=22,
    subtitleFontSize=18,
    offset=30,
    dy=30
)

chart
```





<div id="altair-viz-88568b3fe0524bcaa4de8a91e927b439"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-88568b3fe0524bcaa4de8a91e927b439") {
      outputDiv = document.getElementById("altair-viz-88568b3fe0524bcaa4de8a91e927b439");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
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
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "4.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300, "stroke": null}, "axisY": {"grid": false, "labelAlign": "left", "labelPadding": 110, "ticks": false}, "background": "#D9E9F0", "title": {"dy": 30, "fontSize": 22, "offset": 30, "subtitleFontSize": 18}}, "vconcat": [{"data": {"name": "empty"}, "mark": {"type": "rect", "color": "#EB111A", "height": 18, "width": 50, "xOffset": -105, "yOffset": 10}}, {"data": {"name": "data-1913a809e59f1dfc25bb5719e6f7f706"}, "mark": "bar", "encoding": {"x": {"axis": {"format": "d", "labelFontSize": 14, "orient": "top", "title": "", "values": [1, 2, 3, 4, 5, 6]}, "field": "page1k", "scale": {"domain": [0, 6], "round": true}, "type": "quantitative"}, "y": {"axis": {"labelFontSize": 14, "labelFontStyle": {"condition": {"test": "datum.value == \"Jeremy Corbyn\"", "value": "bold"}, "value": "italic"}}, "field": "Page", "sort": {"field": "Average number of likes per Facebook post 2016:Q", "op": "sum", "order": "ascending"}, "title": "", "type": "ordinal"}}, "title": {"text": ["Left Click"], "subtitle": ["Average number of likes per Facebook post\n", "2016, '000"], "align": "left", "anchor": "start"}}, {"data": {"name": "data-a4de834d9d3c210d2fa4d84e065850aa"}, "mark": {"type": "text", "align": "left", "color": "darkgrey", "dx": -120, "size": 12}, "encoding": {"text": {"field": "text", "type": "nominal"}}}], "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"empty": [{}], "data-1913a809e59f1dfc25bb5719e6f7f706": [{"Page": "Jeremy Corbyn", "Average number of likes per Facebook post 2016": 5210.0, "page1k": 5.21}, {"Page": "Labour Party", "Average number of likes per Facebook post 2016": 845.0, "page1k": 0.845}, {"Page": "Momentum", "Average number of likes per Facebook post 2016": 229.0, "page1k": 0.229}, {"Page": "Owen Smith", "Average number of likes per Facebook post 2016": 127.0, "page1k": 0.127}, {"Page": "Andy Burnham ", "Average number of likes per Facebook post 2016": 105.0, "page1k": 0.105}, {"Page": "Saving Labour", "Average number of likes per Facebook post 2016": 56.0, "page1k": 0.056}], "data-a4de834d9d3c210d2fa4d84e065850aa": [{"text": "Source: Facebook"}]}}, {"mode": "vega-lite"});
</script>



The only thing, I could not reproduce with Altair is the light bar around the the first label and bar. For those final touches I think it's better to export the graph and add those finishing touches with a tool such as Inkscape or Illustrator.
<!-- more -->

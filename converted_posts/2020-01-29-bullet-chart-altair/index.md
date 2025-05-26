---
title: Bullet chart in python Altair
date: 2020-01-29
created_at: 2020-01-29T10:44:22.941081
last_modified: 2020-01-29T10:44:22.941087
---

# Bullet chart in python Altair

In the article ["Bullet Charts - What Is It And How To Use It"](https://jscharting.com/blog/bullet-charts/) I learned about Bullet charts. It's a specific kind of barchart that must convey the state of a measure or KPI. The goal is to see in a glance if the target is met.
Here is an example bullet chart from the article:

```python
# This causes issues to: 
# from IPython.display import Image
# Image('https://jscharting.com/blog/bullet-charts/images/bullet_components.png')
```

![Example Bullet Chart](https://jscharting.com/blog/bullet-charts/images/bullet_components.png)

```python
# <img src="https://jscharting.com/blog/bullet-charts/images/bullet_components.png" alt="Bullet chart" style="width: 200px;"/>
```

Below is some Python code that generates bullets graphs using the [Altair](https://altair-viz.github.io/) library.

```python
import altair as alt
import pandas as pd

df = pd.DataFrame.from_records([
    {"title":"Revenue","subtitle":"US$, in thousands","ranges":[150,225,300],"measures":[220,270],"markers":[250]},
    {"title":"Profit","subtitle":"%","ranges":[20,25,30],"measures":[21,23],"markers":[26]},
    {"title":"Order Size","subtitle":"US$, average","ranges":[350,500,600],"measures":[100,320],"markers":[550]},
    {"title":"New Customers","subtitle":"count","ranges":[1400,2000,2500],"measures":[1000,1650],"markers":[2100]},
    {"title":"Satisfaction","subtitle":"out of 5","ranges":[3.5,4.25,5],"measures":[3.2,4.7],"markers":[4.4]}
])

alt.layer(
    alt.Chart().mark_bar(color='#eee').encode(alt.X("ranges[2]:Q", scale=alt.Scale(nice=False), title=None)),
    alt.Chart().mark_bar(color='#ddd').encode(x="ranges[1]:Q"),
    alt.Chart().mark_bar(color='#bbb').encode(x="ranges[0]:Q"),
    alt.Chart().mark_bar(color='steelblue', size=10).encode(x='measures[0]:Q'),
    alt.Chart().mark_tick(color='black', size=12).encode(x='markers[0]:Q'),
    data=df
).facet(
    row=alt.Row("title:O", title='')
).resolve_scale(
    x='independent'
)
```

<div id="altair-viz-c4832b7a7930443a9e3838b5ed329707"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-c4832b7a7930443a9e3838b5ed329707") {
      outputDiv = document.getElementById("altair-viz-c4832b7a7930443a9e3838b5ed329707");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-51276fdc382351453eb0c63bc10cd921"}, "facet": {"row": {"type": "ordinal", "field": "title", "title": ""}}, "spec": {"layer": [{"mark": {"type": "bar", "color": "#eee"}, "encoding": {"x": {"type": "quantitative", "field": "ranges[2]", "scale": {"nice": false}, "title": null}}}, {"mark": {"type": "bar", "color": "#ddd"}, "encoding": {"x": {"type": "quantitative", "field": "ranges[1]"}}}, {"mark": {"type": "bar", "color": "#bbb"}, "encoding": {"x": {"type": "quantitative", "field": "ranges[0]"}}}, {"mark": {"type": "bar", "color": "steelblue", "size": 10}, "encoding": {"x": {"type": "quantitative", "field": "measures[0]"}}}, {"mark": {"type": "tick", "color": "black", "size": 12}, "encoding": {"x": {"type": "quantitative", "field": "markers[0]"}}}]}, "resolve": {"scale": {"x": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-51276fdc382351453eb0c63bc10cd921": [{"title": "Revenue", "subtitle": "US$, in thousands", "ranges": [150, 225, 300], "measures": [220, 270], "markers": [250]}, {"title": "Profit", "subtitle": "%", "ranges": [20, 25, 30], "measures": [21, 23], "markers": [26]}, {"title": "Order Size", "subtitle": "US$, average", "ranges": [350, 500, 600], "measures": [100, 320], "markers": [550]}, {"title": "New Customers", "subtitle": "count", "ranges": [1400, 2000, 2500], "measures": [1000, 1650], "markers": [2100]}, {"title": "Satisfaction", "subtitle": "out of 5", "ranges": [3.5, 4.25, 5], "measures": [3.2, 4.7], "markers": [4.4]}]}}, {"mode": "vega-lite"});
</script>

<!-- more -->

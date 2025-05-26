---
title: Bar chart made in Altair with Financial Times style
date: 2022-04-24
created_at: 2022-04-24T10:44:22.941081
last_modified: 2022-04-24T10:44:22.941087
---
# Bar chart made in Altair with Financial Times style

\#30DayChartChallenge \#Day24 Themeday: Financial times


```python
import pandas as pd
import altair as alt
```

The #30DayChartChallenge Day 24 calls for Financial Times themed charts. The bar chart that I will try to reproduce in Altair was published in the article: ["Financial warfare: will there be a backlash against the dollar?"](https://www.ft.com/content/220db8f2-2980-410f-aab8-f471369ac3cf)

This is the graph (without FT background) to we want to reproduce:
![](https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd6c748xw2pzm8.cloudfront.net%2Fprod%2Ff4926320-b74a-11ec-ac86-5174c5daccd3-standard.png?dpr=1&fit=scale-down&quality=highest&source=next&width=700 "Credit: ft.com")

I digitized the heights of yhe bars with [WebplotDigitizer](https://apps.automeris.io/wpd/):


```python
data = """Bar0, 3.23
Bar1, 1.27
Bar2, 1.02
Bar3, 0.570
Bar4, 0.553
Bar5, 0.497
Bar6, 0.467
Bar7, 0.440
Bar8, 0.420
Bar9, 0.413
Bar10, 0.317
Bar11, 0.0433"""

data_values = [float(x.split()[1]) for x in data.splitlines()]
```

I put the values into a Pandas dataframe:


```python
source = pd.DataFrame({
    'label': ['China', 'Japan', 'Switserland', 'India', 'Taiwan', 'Hong Kong', 'Russia', 'South Korea', 'Saudi Arabia', 'Singapore', 'Eurozone', 'US'],
    'val': data_values
})
```

Now we build the graph and alter it's style to resemble the Financial Times style:


```python
square = alt.Chart().mark_rect(width=80, height=5, color='black', xOffset=-112, yOffset=10)

bars = alt.Chart(source).mark_bar(color='#174C7F', size=30).encode(
    x=alt.X('val:Q', title='', axis=alt.Axis(tickCount=6, domain=False, labelColor='darkgray'), scale=alt.Scale(domain=[0, 3.0])),
    y=alt.Y('label:N', title='', sort=alt.EncodingSortField(
            field="val:Q",  # The field to use for the sort
            op="sum",  # The operation to run on the field prior to sorting
            order="ascending"  # The order to sort in
        ), axis=alt.Axis(domainColor='lightgray',
                         labelFontSize=18, labelColor='darkgray', labelPadding=5,
                         labelFontStyle='Bold',
                         tickSize=18, tickColor='lightgray'))
).properties(title={
      "text": ["The biggest holders of FX reserves", ],
      "subtitle": ["Official foreign exchange reserve (Jan 2022, $tn)"],
      "align": 'left',
      "anchor": 'start'
    },
    width=700,
    height=512
)

source_text = alt.Chart(
    {"values": [{"text": "Source: IMF, © FT"}]}
).mark_text(size=12, align='left', dx=-140, color='darkgrey').encode(
    text="text:N"
)

# from https://stackoverflow.com/questions/57244390/has-anyone-figured-out-a-workaround-to-add-a-subtitle-to-an-altair-generated-cha
chart = alt.vconcat(
    square,
    bars,
    source_text
).configure_concat(
    spacing=0
).configure(
    background='#fff1e5',
).configure_view(
    stroke=None, # Remove box around graph
).configure_title(
    # font='metricweb',
    fontSize=22,
    fontWeight=400,
    subtitleFontSize=18,
    subtitleColor='darkgray',
    subtitleFontWeight=400,
    subtitlePadding=15,
    offset=80,
    dy=40
)

chart
```





<div id="altair-viz-80793582b97e479ca5b66521e9670b81"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-80793582b97e479ca5b66521e9670b81") {
      outputDiv = document.getElementById("altair-viz-80793582b97e479ca5b66521e9670b81");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300, "stroke": null}, "background": "#fff1e5", "title": {"dy": 40, "fontSize": 22, "fontWeight": 400, "offset": 80, "subtitleColor": "darkgray", "subtitleFontSize": 18, "subtitleFontWeight": 400, "subtitlePadding": 15}}, "vconcat": [{"data": {"name": "empty"}, "mark": {"type": "rect", "color": "black", "height": 5, "width": 80, "xOffset": -112, "yOffset": 10}}, {"data": {"name": "data-df71ec9f3957c236109e455bd72c3eb3"}, "mark": {"type": "bar", "color": "#174C7F", "size": 30}, "encoding": {"x": {"axis": {"domain": false, "labelColor": "darkgray", "tickCount": 6}, "field": "val", "scale": {"domain": [0, 3.0]}, "title": "", "type": "quantitative"}, "y": {"axis": {"domainColor": "lightgray", "labelColor": "darkgray", "labelFontSize": 18, "labelFontStyle": "Bold", "labelPadding": 5, "tickColor": "lightgray", "tickSize": 18}, "field": "label", "sort": {"field": "val:Q", "op": "sum", "order": "ascending"}, "title": "", "type": "nominal"}}, "height": 512, "title": {"text": ["The biggest holders of FX reserves"], "subtitle": ["Official foreign exchange reserve (Jan 2022, $tn)"], "align": "left", "anchor": "start"}, "width": 700}, {"data": {"name": "data-0a30ac8e3706e989ddfc777785723af1"}, "mark": {"type": "text", "align": "left", "color": "darkgrey", "dx": -140, "size": 12}, "encoding": {"text": {"field": "text", "type": "nominal"}}}], "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"empty": [{}], "data-df71ec9f3957c236109e455bd72c3eb3": [{"label": "China", "val": 3.23}, {"label": "Japan", "val": 1.27}, {"label": "Switserland", "val": 1.02}, {"label": "India", "val": 0.57}, {"label": "Taiwan", "val": 0.553}, {"label": "Hong Kong", "val": 0.497}, {"label": "Russia", "val": 0.467}, {"label": "South Korea", "val": 0.44}, {"label": "Saudi Arabia", "val": 0.42}, {"label": "Singapore", "val": 0.413}, {"label": "Eurozone", "val": 0.317}, {"label": "US", "val": 0.0433}], "data-0a30ac8e3706e989ddfc777785723af1": [{"text": "Source: IMF, \u00a9 FT"}]}}, {"mode": "vega-lite"});
</script>



# Trying to use the offical Financial Times fonts

The chart looks quit similar to the original. Biggest difference is the typography. The Financial times uses its own Metric Web and Financier Display Web fonts and Altair can only use fonts available in the browser.

The fonts could be made available via CSS:

```css
@font-face {
    font-family: 'metricweb';
    src: url('https://www.ft.com/__origami/service/build/v2/files/o-fonts-assets@1.5.0/MetricWeb-Regular.woff2''
);
}
```


```python
from IPython.display import HTML
from google.colab.output import _publish as publish
publish.css("""@font-face {
    font-family: 'metricweb', sans-serif;
    src: url('https://www.ft.com/__origami/service/build/v2/files/o-fonts-assets@1.5.0/MetricWeb-Regular.woff2') format('woff2');
}""")
```


<style>@font-face {
    font-family: 'metricweb', sans-serif;
    src: url('https://www.ft.com/__origami/service/build/v2/files/o-fonts-assets@1.5.0/MetricWeb-Regular.woff2') format('woff2');
}</style>



```python
square = alt.Chart().mark_rect(width=80, height=5, color='black', xOffset=-112, yOffset=10)

bars = alt.Chart(source).mark_bar(color='#174C7F', size=30).encode(
    x=alt.X('val:Q', title='', axis=alt.Axis(tickCount=6, domain=False), scale=alt.Scale(domain=[0, 3.0])),
    y=alt.Y('label:N', title='', sort=alt.EncodingSortField(
            field="val:Q",  # The field to use for the sort
            op="sum",  # The operation to run on the field prior to sorting
            order="ascending"  # The order to sort in
        ), axis=alt.Axis(domainColor='lightgray',
                         labelFontSize=18, labelColor='darkgray', labelPadding=5,
                         labelFontStyle='Bold',
                         tickSize=18, tickColor='lightgray'))
).properties(title={
      "text": ["The biggest holders of FX reserves", ],
      "subtitle": ["Official foreign exchange reserve (Jan 2022, $tn)"],
      "align": 'left',
      "anchor": 'start'
    },
    width=700,
    height=512
)

source_text = alt.Chart(
    {"values": [{"text": "Source: IMF, © FT"}]}
).mark_text(size=12, align='left', dx=-140, color='darkgrey').encode(
    text="text:N"
)

# from https://stackoverflow.com/questions/57244390/has-anyone-figured-out-a-workaround-to-add-a-subtitle-to-an-altair-generated-cha
chart = alt.vconcat(
    square,
    bars,
    source_text
).configure_concat(
    spacing=0
).configure(
    background='#fff1e5',
).configure_view(
    stroke=None, # Remove box around graph
).configure_title(
    font='metricweb',
    fontSize=22,
    fontWeight=400,
    subtitleFont='metricweb',
    subtitleFontSize=18,
    subtitleColor='darkgray',
    subtitleFontWeight=400,
    subtitlePadding=15,
    offset=80,
    dy=40
)

chart
```





<div id="altair-viz-4e3b9cb8f81842a7953a6fb0fb834a7f"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-4e3b9cb8f81842a7953a6fb0fb834a7f") {
      outputDiv = document.getElementById("altair-viz-4e3b9cb8f81842a7953a6fb0fb834a7f");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300, "stroke": null}, "background": "#fff1e5", "title": {"dy": 40, "font": "metricweb", "fontSize": 22, "fontWeight": 400, "offset": 80, "subtitleColor": "darkgray", "subtitleFont": "metricweb", "subtitleFontSize": 18, "subtitleFontWeight": 400, "subtitlePadding": 15}}, "vconcat": [{"data": {"name": "empty"}, "mark": {"type": "rect", "color": "black", "height": 5, "width": 80, "xOffset": -112, "yOffset": 10}}, {"data": {"name": "data-df71ec9f3957c236109e455bd72c3eb3"}, "mark": {"type": "bar", "color": "#174C7F", "size": 30}, "encoding": {"x": {"axis": {"domain": false, "tickCount": 6}, "field": "val", "scale": {"domain": [0, 3.0]}, "title": "", "type": "quantitative"}, "y": {"axis": {"domainColor": "lightgray", "labelColor": "darkgray", "labelFontSize": 18, "labelFontStyle": "Bold", "labelPadding": 5, "tickColor": "lightgray", "tickSize": 18}, "field": "label", "sort": {"field": "val:Q", "op": "sum", "order": "ascending"}, "title": "", "type": "nominal"}}, "height": 512, "title": {"text": ["The biggest holders of FX reserves"], "subtitle": ["Official foreign exchange reserve (Jan 2022, $tn)"], "align": "left", "anchor": "start"}, "width": 700}, {"data": {"name": "data-0a30ac8e3706e989ddfc777785723af1"}, "mark": {"type": "text", "align": "left", "color": "darkgrey", "dx": -140, "size": 12}, "encoding": {"text": {"field": "text", "type": "nominal"}}}], "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"empty": [{}], "data-df71ec9f3957c236109e455bd72c3eb3": [{"label": "China", "val": 3.23}, {"label": "Japan", "val": 1.27}, {"label": "Switserland", "val": 1.02}, {"label": "India", "val": 0.57}, {"label": "Taiwan", "val": 0.553}, {"label": "Hong Kong", "val": 0.497}, {"label": "Russia", "val": 0.467}, {"label": "South Korea", "val": 0.44}, {"label": "Saudi Arabia", "val": 0.42}, {"label": "Singapore", "val": 0.413}, {"label": "Eurozone", "val": 0.317}, {"label": "US", "val": 0.0433}], "data-0a30ac8e3706e989ddfc777785723af1": [{"text": "Source: IMF, \u00a9 FT"}]}}, {"mode": "vega-lite"});
</script>



For the moment the font does not look at all to be Metric web :-(

A second minor difference are the alignment of the 0.0 and 3.0 labels of the x-axis. In the orginal, those labels are centered. Altair aligns 0.0 to the left and 3.0 to the right.


```python

```
<!-- more -->

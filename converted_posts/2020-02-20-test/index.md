---
title: Fastpages Notebook Blog Post
date: 2020-02-20
created_at: 2020-02-20T10:44:22.941081
last_modified: 2020-02-20T10:44:22.941087
---

# Fastpages Notebook Blog Post
>
> A tutorial of fastpages for Jupyter notebooks.

- toc: true
- badges: true
- comments: true
- categories: [jupyter]
- image: images/chart-preview.png

# About

This notebook is a demonstration of some of capabilities of [fastpages](https://github.com/fastai/fastpages) with notebooks.

With `fastpages` you can save your jupyter notebooks into the `_notebooks` folder at the root of your repository, and they will be automatically be converted to Jekyll compliant blog posts!

## Front Matter

The first cell in your Jupyter Notebook or markdown blog post contains front matter. Front matter is metadata that can turn on/off options in your Notebook. It is formatted like this:

```
# "My Title"
> "Awesome summary"

- toc: true- branch: master- badges: true
- comments: true
- author: Hamel Husain & Jeremy Howard
- categories: [fastpages, jupyter]
```

- Setting `toc: true` will automatically generate a table of contents
- Setting `badges: true` will automatically include GitHub and Google Colab links to your notebook.
- Setting `comments: true` will enable commenting on your blog post, powered by [utterances](https://github.com/utterance/utterances).

The title and description need to be enclosed in double quotes only if they include special characters such as a colon. More details and options for front matter can be viewed on the [front matter section](https://github.com/fastai/fastpages#front-matter-related-options) of the README.

## Markdown Shortcuts

A `#hide` comment at the top of any code cell will hide **both the input and output** of that cell in your blog post.

A `#hide_input` comment at the top of any code cell will **only hide the input** of that cell.

```python
#hide_input
print('The comment #hide_input was used to hide the code that produced this.')
```

    The comment #hide_input was used to hide the code that produced this.

put a `#collapse-hide` flag at the top of any cell if you want to **hide** that cell by default, but give the reader the option to show it:

```python
#collapse-hide
import pandas as pd
import altair as alt
```

put a `#collapse-show` flag at the top of any cell if you want to **show** that cell by default, but give the reader the option to hide it:

```python
#collapse-show
cars = 'https://vega.github.io/vega-datasets/data/cars.json'
movies = 'https://vega.github.io/vega-datasets/data/movies.json'
sp500 = 'https://vega.github.io/vega-datasets/data/sp500.csv'
stocks = 'https://vega.github.io/vega-datasets/data/stocks.csv'
flights = 'https://vega.github.io/vega-datasets/data/flights-5k.json'
```

## Interactive Charts With Altair

Charts made with Altair remain interactive.  Example charts taken from [this repo](https://github.com/uwdata/visualization-curriculum), specifically [this notebook](https://github.com/uwdata/visualization-curriculum/blob/master/altair_interaction.ipynb).

```python
# hide
df = pd.read_json(movies) # load movies data
genres = df['Major_Genre'].unique() # get unique field values
genres = list(filter(lambda d: d is not None, genres)) # filter out None values
genres.sort() # sort alphabetically
```

```python
#hide
mpaa = ['G', 'PG', 'PG-13', 'R', 'NC-17', 'Not Rated']
```

### Example 1: DropDown

```python
# single-value selection over [Major_Genre, MPAA_Rating] pairs
# use specific hard-wired values as the initial selected values
selection = alt.selection_single(
    name='Select',
    fields=['Major_Genre', 'MPAA_Rating'],
    init={'Major_Genre': 'Drama', 'MPAA_Rating': 'R'},
    bind={'Major_Genre': alt.binding_select(options=genres), 'MPAA_Rating': alt.binding_radio(options=mpaa)}
)
  
# scatter plot, modify opacity based on selection
alt.Chart(movies).mark_circle().add_selection(
    selection
).encode(
    x='Rotten_Tomatoes_Rating:Q',
    y='IMDB_Rating:Q',
    tooltip='Title:N',
    opacity=alt.condition(selection, alt.value(0.75), alt.value(0.05))
)
```

<div id="altair-viz-1a49e83878ce4d678d7b162f3d6b510f"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-1a49e83878ce4d678d7b162f3d6b510f");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"url": "<https://vega.github.io/vega-datasets/data/movies.json"}>, "mark": "circle", "encoding": {"opacity": {"condition": {"value": 0.75, "selection": "Select"}, "value": 0.05}, "tooltip": {"type": "nominal", "field": "Title"}, "x": {"type": "quantitative", "field": "Rotten_Tomatoes_Rating"}, "y": {"type": "quantitative", "field": "IMDB_Rating"}}, "selection": {"Select": {"type": "single", "fields": ["Major_Genre", "MPAA_Rating"], "init": {"Major_Genre": "Drama", "MPAA_Rating": "R"}, "bind": {"Major_Genre": {"input": "select", "options": ["Action", "Adventure", "Black Comedy", "Comedy", "Concert/Performance", "Documentary", "Drama", "Horror", "Musical", "Romantic Comedy", "Thriller/Suspense", "Western"]}, "MPAA_Rating": {"input": "radio", "options": ["G", "PG", "PG-13", "R", "NC-17", "Not Rated"]}}}}, "$schema": "<https://vega.github.io/schema/vega-lite/v4.0.2.json"}>, {"mode": "vega-lite"});
</script>

### Example 2: Tooltips

```python
alt.Chart(movies).mark_circle().add_selection(
    alt.selection_interval(bind='scales', encodings=['x'])
).encode(
    x='Rotten_Tomatoes_Rating:Q',
    y=alt.Y('IMDB_Rating:Q', axis=alt.Axis(minExtent=30)), # use min extent to stabilize axis title placement
    tooltip=['Title:N', 'Release_Date:N', 'IMDB_Rating:Q', 'Rotten_Tomatoes_Rating:Q']
).properties(
    width=600,
    height=400
)
```

<div id="altair-viz-c022b476f4fb482ca6f609bf6ed082d2"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-c022b476f4fb482ca6f609bf6ed082d2");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"url": "<https://vega.github.io/vega-datasets/data/movies.json"}>, "mark": "circle", "encoding": {"tooltip": [{"type": "nominal", "field": "Title"}, {"type": "nominal", "field": "Release_Date"}, {"type": "quantitative", "field": "IMDB_Rating"}, {"type": "quantitative", "field": "Rotten_Tomatoes_Rating"}], "x": {"type": "quantitative", "field": "Rotten_Tomatoes_Rating"}, "y": {"type": "quantitative", "axis": {"minExtent": 30}, "field": "IMDB_Rating"}}, "height": 400, "selection": {"selector001": {"type": "interval", "bind": "scales", "encodings": ["x"]}}, "width": 600, "$schema": "<https://vega.github.io/schema/vega-lite/v4.0.2.json"}>, {"mode": "vega-lite"});
</script>

### Example 3: More Tooltips

```python
# select a point for which to provide details-on-demand
label = alt.selection_single(
    encodings=['x'], # limit selection to x-axis value
    on='mouseover',  # select on mouseover events
    nearest=True,    # select data point nearest the cursor
    empty='none'     # empty selection includes no data points
)

# define our base line chart of stock prices
base = alt.Chart().mark_line().encode(
    alt.X('date:T'),
    alt.Y('price:Q', scale=alt.Scale(type='log')),
    alt.Color('symbol:N')
)

alt.layer(
    base, # base line chart
    
    # add a rule mark to serve as a guide line
    alt.Chart().mark_rule(color='#aaa').encode(
        x='date:T'
    ).transform_filter(label),
    
    # add circle marks for selected time points, hide unselected points
    base.mark_circle().encode(
        opacity=alt.condition(label, alt.value(1), alt.value(0))
    ).add_selection(label),

    # add white stroked text to provide a legible background for labels
    base.mark_text(align='left', dx=5, dy=-5, stroke='white', strokeWidth=2).encode(
        text='price:Q'
    ).transform_filter(label),

    # add text labels for stock prices
    base.mark_text(align='left', dx=5, dy=-5).encode(
        text='price:Q'
    ).transform_filter(label),
    
    data=stocks
).properties(
    width=700,
    height=400
)
```

<div id="altair-viz-9283d3681fd24aafa3d1e2f9ad193ecf"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-9283d3681fd24aafa3d1e2f9ad193ecf");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "layer": [{"mark": "line", "encoding": {"color": {"type": "nominal", "field": "symbol"}, "x": {"type": "temporal", "field": "date"}, "y": {"type": "quantitative", "field": "price", "scale": {"type": "log"}}}}, {"mark": {"type": "rule", "color": "#aaa"}, "encoding": {"x": {"type": "temporal", "field": "date"}}, "transform": [{"filter": {"selection": "selector002"}}]}, {"mark": "circle", "encoding": {"color": {"type": "nominal", "field": "symbol"}, "opacity": {"condition": {"value": 1, "selection": "selector002"}, "value": 0}, "x": {"type": "temporal", "field": "date"}, "y": {"type": "quantitative", "field": "price", "scale": {"type": "log"}}}, "selection": {"selector002": {"type": "single", "encodings": ["x"], "on": "mouseover", "nearest": true, "empty": "none"}}}, {"mark": {"type": "text", "align": "left", "dx": 5, "dy": -5, "stroke": "white", "strokeWidth": 2}, "encoding": {"color": {"type": "nominal", "field": "symbol"}, "text": {"type": "quantitative", "field": "price"}, "x": {"type": "temporal", "field": "date"}, "y": {"type": "quantitative", "field": "price", "scale": {"type": "log"}}}, "transform": [{"filter": {"selection": "selector002"}}]}, {"mark": {"type": "text", "align": "left", "dx": 5, "dy": -5}, "encoding": {"color": {"type": "nominal", "field": "symbol"}, "text": {"type": "quantitative", "field": "price"}, "x": {"type": "temporal", "field": "date"}, "y": {"type": "quantitative", "field": "price", "scale": {"type": "log"}}}, "transform": [{"filter": {"selection": "selector002"}}]}], "data": {"url": "<https://vega.github.io/vega-datasets/data/stocks.csv"}>, "height": 400, "width": 700, "$schema": "<https://vega.github.io/schema/vega-lite/v4.0.2.json"}>, {"mode": "vega-lite"});
</script>

## Data Tables

You can display tables per the usual way in your blog:

```python
movies = 'https://vega.github.io/vega-datasets/data/movies.json'
df = pd.read_json(movies)
# display table with pandas
df[['Title', 'Worldwide_Gross', 
    'Production_Budget', 'Distributor', 'MPAA_Rating', 'IMDB_Rating', 'Rotten_Tomatoes_Rating']].head()
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
      <th>Title</th>
      <th>Worldwide_Gross</th>
      <th>Production_Budget</th>
      <th>Distributor</th>
      <th>MPAA_Rating</th>
      <th>IMDB_Rating</th>
      <th>Rotten_Tomatoes_Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Land Girls</td>
      <td>146083.0</td>
      <td>8000000.0</td>
      <td>Gramercy</td>
      <td>R</td>
      <td>6.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>First Love, Last Rites</td>
      <td>10876.0</td>
      <td>300000.0</td>
      <td>Strand</td>
      <td>R</td>
      <td>6.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>I Married a Strange Person</td>
      <td>203134.0</td>
      <td>250000.0</td>
      <td>Lionsgate</td>
      <td>None</td>
      <td>6.8</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Let's Talk About Sex</td>
      <td>373615.0</td>
      <td>300000.0</td>
      <td>Fine Line</td>
      <td>None</td>
      <td>NaN</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Slam</td>
      <td>1087521.0</td>
      <td>1000000.0</td>
      <td>Trimark</td>
      <td>R</td>
      <td>3.4</td>
      <td>62.0</td>
    </tr>
  </tbody>
</table>
</div>

## Images

### Local Images

You can reference local images and they will be copied and rendered on your blog automatically.  You can include these with the following markdown syntax:

`![](my_icons/fastai_logo.png)`

![](my_icons/fastai_logo.png)

### Remote Images

Remote images can be included with the following markdown syntax:

`![](https://image.flaticon.com/icons/svg/36/36686.svg)`

![](https://image.flaticon.com/icons/svg/36/36686.svg)

### Animated Gifs

Animated Gifs work, too!

`![](https://upload.wikimedia.org/wikipedia/commons/7/71/ChessPawnSpecialMoves.gif)`

![](https://upload.wikimedia.org/wikipedia/commons/7/71/ChessPawnSpecialMoves.gif)

### Captions

You can include captions with markdown images like this:

```
![](https://www.fast.ai/images/fastai_paper/show_batch.png "Credit: https://www.fast.ai/2020/02/13/fastai-A-Layered-API-for-Deep-Learning/")
```

![](https://www.fast.ai/images/fastai_paper/show_batch.png "Credit: https://www.fast.ai/2020/02/13/fastai-A-Layered-API-for-Deep-Learning/")

# Other Elements

## GitHub Flavored Emojis

Typing `I give this post two :+1:!` will render this:

I give this post two :+1:!

## Tweetcards

Typing `> twitter: https://twitter.com/jakevdp/status/1204765621767901185?s=20` will render this:

> twitter: <https://twitter.com/jakevdp/status/1204765621767901185?s=20>

## Youtube Videos

Typing `> youtube: https://youtu.be/XfoYk_Z5AkI` will render this:

> youtube: <https://youtu.be/XfoYk_Z5AkI>

## Boxes / Callouts

Typing `> Warning: There will be no second warning!` will render this:

> Warning: There will be no second warning!

Typing `> Important: Pay attention! It's important.` will render this:

> Important: Pay attention! It's important.

Typing `> Tip: This is my tip.` will render this:

> Tip: This is my tip.

Typing `> Note: Take note of this.` will render this:

> Note: Take note of this.

Typing `> Note: A doc link to [an example website: fast.ai](https://www.fast.ai/) should also work fine.` will render in the docs:

> Note: A doc link to [an example website: fast.ai](https://www.fast.ai/) should also work fine.

## Footnotes

You can have footnotes in notebooks, however the syntax is different compared to markdown documents. [This guide provides more detail about this syntax](https://github.com/fastai/fastpages/blob/master/_fastpages_docs/NOTEBOOK_FOOTNOTES.md), which looks like this:

```
{% raw %}For example, here is a footnote {% fn 1 %}.
And another {% fn 2 %}
{{ 'This is the footnote.' | fndetail: 1 }}
{{ 'This is the other footnote. You can even have a [link](www.github.com)!' | fndetail: 2 }}{% endraw %}
```

For example, here is a footnote {% fn 1 %}.

And another {% fn 2 %}

{{ 'This is the footnote.' | fndetail: 1 }}
{{ 'This is the other footnote. You can even have a [link](www.github.com)!' | fndetail: 2 }}

<!-- more -->

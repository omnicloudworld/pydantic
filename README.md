
<p align="center" style="text-align:center" >

__This package is a part of cloud application framework [SkyANT](https://skyant.dev). For more information please read [the documentation](https://docs.skyant.dev/projects/data).__

</p>


<br/><br/>

<p align="center" style="text-align:center" >

## __Cloud Application Framework__

</p>

Cloud Application Framework is a fleet of well-known software libraries which was been extended by cloud related methods.

SkyANT now contains components inherited from [Plotly Dash](https://dash.plotly.com), [Pydantic](https://docs.pydantic.dev/), [Dask](https://dask.org), [Odoo](https://odoo.com), etc & work with [Google Cloud Platform](https://cloud.google.com).


<br/>

<p align="center" style="text-align:center" >

## __Value__

</p>


Making software for a cloud requires two vectors business-logic & cloud integration codding.

SkyANT components already contain cloud integration tools, so it gives developers opportunities to work with business-logic only.



## Features

#### data types

- [x] structured (json, yaml)
- [ ] unstructured (jpg, jpeg, png)


#### save/send and load

- [x] to/from Google Cloud Storage
- [x] to/from local file
- [x] to/from Google Firestore
- [x] to Google PubSub topic & Google Tasks
- [ ] to/from REST endpoint (partial completed)


#### other

- [x] send request with an authentication header for Google Cloud Platform (with `skyant-tools`)
- [x] transparently work with a document reference in Google Firestore

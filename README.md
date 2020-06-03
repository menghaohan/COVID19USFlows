[![MIT License][license-shield]][license-url]


The data processing framework for the mobility flow dataset production.}
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://geods.geography.wisc.edu/">
    <img src="images/GeoDSLogo.jpg" alt="Logo" width="100">
  </a>

  <h2 align="center">Multiscale Dynamic Human Mobility Flow Data in the U.S. during the COVID-19 Epidemic</h2>

  <p align="center">
    GeoDS Lab, Department of Geography, University of Wisconsin-Madison.
    <br />
    <a href="https://geods.geography.wisc.edu/covid-19-physical-distancing">Website</a>
    ·
    <a href="http://geods.geography.wisc.edu/covid19/King_WA.html">View Demo</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Data Processing and Data Descriptor](#processing)
* [Field Descriptions](#records)
* [Folder Structure](#folder)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project


The efficiency of reducing human mobility and social activities has been proved for containing the transmission of the COVID-19 epidemic. Many governments have responded with public health policies and interventions such as social distancing, lockdown cities, stay-at-home orders, and travel restrictions. 
Understanding human mobility patterns at different geographic scales is crucial for monitoring and measuring the impacts of non-pharmaceutical interventions during the pandemic. 
In this paper, we introduce a multiscale dynamic human mobility flow dataset across the United States since March 1st, 2020.
By tracking millions of anonymous mobile phone users’ visit trajectories to various places provided by [SafeGraph](https://www.safegraph.com/), the daily and weekly dynamic population flows are computed, aggregated, and inferred at three geographic scales including census tract to census tract, county to county, and state to state, respectively.
Results of the comparison between our mobility flow dataset and openly available data sources show high consistency, which proves the reliability of the produced data. 
Such a high spatiotemporal resolution of human mobility flow dataset at different scales over time may not only help monitor epidemic spreading dynamics and inform public health policy making and beyond, but also deepen our understanding of human behaviors and changes in the society under the unprecedented public health crisis. 


<!-- GETTING STARTED -->
## Data Processing and Data Descriptor 

The data processing framework for the mobility flow dataset production:  
<p align="center">
  <a href="https://geods.geography.wisc.edu/">
    <img src="images/framework.png" alt="framework" >
  </a>
</p>

Spatial distribution of places collected by SafeGraph across the whole United States.  
<p align="center">
  <a href="https://geods.geography.wisc.edu/">
    <img src="images/safegraph_core_usa_eq_hist.png" alt="Core Places" >
  </a>
</p>

Spatial patterns of mobility flows during March 2nd to March 8th at the county to county level.  
<p align="center">
  <a href="https://geods.geography.wisc.edu/">
    <img src="images/County_03_02.png" alt="Weekly Flows" >
  </a>
</p>

Spatial patterns of mobility flows during April 6th to April 12th at the county to county level.  
<p align="center">
  <a href="https://geods.geography.wisc.edu/">
    <img src="images/County_04_06.png" alt="Weekly Flows" >
  </a>
</p>


A full description of the methodology used for this study can be found here: .

## Data Records and Field Descriptions

The folders and files are organized as follows.   
```
project
|-- code
|-- daily_flows
|   |-- state2state
|   |   |-- daily_03_01_state2state.csv
|   |   |-- daily_03_02_state2state.csv
|   |   `-- ...
|   |-- county2county
|   |   |-- daily_03_01_county2county.csv
|   |   |-- daily_03_02_county2county.csv
|   |   `-- ...
|   `-- ct2ct
|       |-- 03_01
|       |   |-- daily_03_01_ct2ct_0.csv
|       |   |-- daily_03_02_ct2ct_1.csv
|       |   `-- ...
|       |-- 03_02
|       |   |-- daily_03_02_ct2ct_0.csv
|       |   |-- daily_03_02_ct2ct_1.csv
|       |   `-- ...
|       `-- ...
`-- weekly_flows
    |-- state2state
    |   |-- weekly_03_02_state2state.csv
    |   |-- weekly_03_09_state2state.csv
    |   `-- ...
    |-- county2county
    |   |-- weekly_03_02_county2county.csv
    |   |-- weekly_03_09_county2county.csv
    |   `-- ...
    `-- ct2ct
        |-- 03_02
        |   |-- weekly_03_02_ct2ct_0.csv
        |   |-- weekly_03_02_ct2ct_1.csv
        |   `-- ...
        |-- 03_09
        |   |-- weekly_03_09_ct2ct_0.csv
        |   |-- weekly_03_09_ct2ct_1.csv
        |   `-- ...
        `-- ...
```

A description of all attributes in the database is shown below:  

#### Weekly Flow Data (folder: weekly_flows)
geoid\_o - Unique identifier of the origin geographic unit (census tract, county, and state). Type: string.   
geoid\_d - Unique identifier of the destination geographic unit (census tract, county, and state). Type: string.   
lat\_o - Latitude of the geometric centroid of the origin unit. Type: float.   
lng\_o - Longitude of the geometric centroid of the origin unit. Type: float.   
lat\_d - Latitude of the geometric centroid of the destination unit. Type: float.   
lng\_d - Longitude of the geometric centroid of the destination unit. Type: float.   
date\_range - Date range of the records. Type: string.   
visitor\_flows - Estimated number of visitors detected by SafeGraph between the two geographic units (from geoid\_o to geoid\_d). Type: float.   
pop\_flows - Estimated population flows between the two geographic units (from geoid\_o to geoid\_d), inferred from visitor\_flows. Type: float.  

#### Daily Flow Data (folder: daily_flows)
geoid\_o -  Unique identifier of the origin geographic unit (census tract, county, and state). Type: string.  
geoid\_d - Unique identifier of the destination geographic unit (census tract, county, and state). Type: string.  
lat\_o - Latitude of the geometric centroid of the origin unit. Type: float.  
lng\_o - Longitude of the geometric centroid of the origin unit. Type: float.  
lat\_d - Latitude of the geometric centroid of the destination unit. Type: float.  
lng\_d - Longitude of the geometric centroid of the destination unit. Type: float.  
date - Date of the records. Type: string.  
visitor\_flows - Estimated number of visitors between the two geographic units (from geoid\_o to geoid\_d). Type: float.  
pop\_flows - Estimated population flows between the two geographic units (from geoid\_o to geoid\_d), inferred from visitor\_flows. Type: float.  

#### Combine Files
Please note that at census tract level, since file sizes are larger than 100 MB, we split them into 20 files.  
To merge them together, we provide merge_files.py 

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Song Gao - [@gissong](https://twitter.com/gissong) - song.gao at wisc.edu  
Yuhao Kang - [@YuhaoKang](https://twitter.com/YuhaoKang) - yuhao.kang at wisc.edu  

Project Link: [https://github.com/GeoDS/COVID19USFlows](https://github.com/GeoDS/COVID19USFlows)  



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [SafeGraph](https://www.safegraph.com/)
* [GeoDS Lab](https://shields.io)

## Funding
We would like to thank the funding support provided by the National Science Foundation (Award No. BCS-2027375). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation. Support for this research was partly provided by the University of Wisconsin - Madison Office of the Vice Chancellor for Research and Graduate Education with funding from the Wisconsin Alumni Research Foundation.


<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/GeoDS/COVID19USFlows/blob/master/LICENSE.txt

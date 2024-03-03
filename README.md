# Predicting the Price of New York City Airbnbs

## Contributors / Authors
- Riddhi Battu
- Oliver Gullery
- Rashi Selarka
- Prithvi Sureka

## Project Summary
At the heart of our exploration lies the vibrant, dynamic world of New York City's Airbnb landscape. Our project dives into rich data from [insideairbnb.com](http://insideairbnb.com/get-the-data/) detailing Airbnb's listing activity and review metrics within NYC from 2011 to December 2023. Through our analysis, we aim to uncover patterns and insights into the geographical distribution of listings, the trends in reviews, and the underlying factors driving popularity and pricing across all boroughs of NYC. This investigation can give us a unique lens to understand the nuances of urban hospitality and its ripple effects on local tourism and community dynamics, and specific to NYC, can help us better understand the impact of Local Law 18 on Airbnb prices.

## How to Run This Analysis

To execute our data analysis, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine to get started.
   ```
   git clone https://github.com/DSCI-310-2024/DSCI_310_Group_9_NY-airbnb-analysis
   ```
2. **Navigate to Project Directory**: Change your directory to the project folder.
   ```
   cd <project-directory>
   ```
3. **Create and Activate the Conda Environment**: Use the `dsci.yml` file to create a Conda environment that includes all necessary dependencies.
   ```
   conda env create -f dsci.yml
   conda activate dsci
   ```
4. **Run the Analysis**: Open JupyterLab and run the notebook `milestone_1.ipynb` under the src folder.

## Dependencies

This project relies on several dependencies and Python libraries for data manipulation, analysis, and visualization:
- JupyterLab

- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`
- `sklearn`
- `plotly`
- `folium`
- `xgboost`
- `requests`
- `branca`
- `scipy`

## Licenses

This project is licensed under the [MIT License](./LICENSE) and the data is licensed under the [Creative Commons Attribution 4.0 International License](./LICENSE).

_Please refer to `LICENSE.md` for detailed licensing information._

## Dataset Acknowledgement

This project utilizes New York City Airbnb Open Data from [insideairbnb.com](http://insideairbnb.com/get-the-data/). The dataset encompasses a wide array of information pertinent to Airbnb listings in NYC from 2011 to 2023, including host details, geographic availability, and essential metrics for insightful predictions and analyses. We extend our gratitude to Insideairbnb for making this data publicly available, facilitating a deeper understanding of the short-term rental landscape in New York City.

## Inspiration for Analysis

Our analysis is driven by the quest to decode the complexities of the Airbnb ecosystem in NYC, particularly since the Airbnb ban implemented in late 2023. We aim to answer pressing questions such as the variance in host activity across different areas, the impact of location and amenities on pricing strategies, and the trends in guest preferences. Through predictive modeling, we aspire to forecast future patterns in listings and pricing, offering valuable insights for hosts, guests, and policymakers alike.
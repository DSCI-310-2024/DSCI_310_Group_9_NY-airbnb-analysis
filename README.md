# Predicting the Price of New York City Airbnbs

## Contributors / Authors
- Riddhi Battu
- Oliver Gullery
- Rashi Selarka
- Prithvi Sureka

## Project Summary
At the heart of our exploration lies the vibrant, dynamic world of New York City's Airbnb landscape. Our project dives into rich data from [insideairbnb.com](http://insideairbnb.com/get-the-data/) detailing Airbnb's listing activity and review metrics within NYC from 2011 to December 2023. Through our analysis, we aim to uncover patterns and insights into the geographical distribution of listings, the trends in reviews, and the underlying factors driving popularity and pricing across all boroughs of NYC. This investigation can give us a unique lens to understand the nuances of urban hospitality and its ripple effects on local tourism and community dynamics, and specific to NYC, can help us better understand the impact of Local Law 18 on Airbnb prices.

## How to Run This Analysis

**NOTE: This analysis can take a few minutes to run.**

To execute our data analysis in a containerized environment, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine to get started.
   ```
   git clone https://github.com/DSCI-310-2024/DSCI_310_Group_9_NY-airbnb-analysis
   ```
2. **Navigate to Project Directory**: Change your directory to the project folder.
   ```
   cd DSCI_310_Group_9_NY-airbnb-analysis
   ```
3. **Launch the Analysis Environment**: Use Docker Compose to build and run the containerized environment. First clear all previous analysis using `make clean`.
   ```
   docker-compose run --rm analysis-env make clean
   ```
4. Then run the analysis using `make all`.
   ```
   docker-compose run --rm analysis-env make all
   ```

**If you run into a memory error while executing the script `04_model.py`, follow the instructions below:**

## Increasing Docker Container Memory Limit

Since the analysis performed by this project is resource-intensive, it may require more memory than the default Docker container settings allow. To ensure the analysis runs smoothly, we recommend manually increasing the memory allocated to Docker containers on your system. Follow these steps to adjust the memory settings:

1. Open *Docker Desktop* on your machine.
2. Click on the *Settings* gear icon in the top right corner.
3. Navigate to *Resources* > *Memory*.
4. Use the slider or enter a specific value to set the memory limit. For this analysis, we recommend setting it to *16 GB*.
5. Click *Apply & Restart* to apply the changes. Docker Desktop will restart with the new memory allocation.

Please note that increasing Docker's memory allocation may affect your system's overall performance. Adjust the settings based on your system capabilities and requirements.

## Dependencies

This project relies on several dependencies within the Docker container for data manipulation, analysis, and visualization:
- JupyterLab
- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`
- `scikit-learn`
- `plotly`
- `folium`
- `requests`
- `scipy`

All dependencies are managed through the container to ensure reproducibility. The environment setup is handled automatically when you launch the container.

## Using the Docker Container

Our project leverages Docker to create a reproducible computational environment. This approach simplifies dependency management and makes it easier to run our analysis across different machines. The `docker-compose.yml` file in our repository defines the necessary settings to build and start the containerized environment, ready to use with all required dependencies installed.

To stop the container, press `CTRL+C` in the terminal where you ran `docker-compose`. To remove the container, use `docker-compose rm`.

## Licenses

This project is licensed under the [MIT License](./LICENSE) and the data is licensed under the [Creative Commons Attribution 4.0 International License](./LICENSE).

_Please refer to `LICENSE.md` for detailed licensing information._

## Dataset Acknowledgement

This project utilizes New York City Airbnb Open Data from [insideairbnb.com](http://insideairbnb.com/get-the-data/). The dataset encompasses a wide array of information pertinent to Airbnb listings in NYC from 2011 to 2023, including host details, geographic availability, and essential metrics for insightful predictions and analyses. We extend our gratitude to Insideairbnb for making this data publicly available, facilitating a deeper understanding of the short-term rental landscape in New York City.

## Inspiration for Analysis

Our analysis is driven by the quest to decode the complexities of the Airbnb ecosystem in NYC, particularly since the Airbnb ban implemented in late 2023. We aim to answer pressing questions such as the variance in host activity across different areas, the impact of location and amenities on pricing strategies, and the trends in guest preferences. Through predictive modeling, we aspire to forecast future patterns in listings and pricing, offering valuable insights for hosts, guests, and policymakers alike. 
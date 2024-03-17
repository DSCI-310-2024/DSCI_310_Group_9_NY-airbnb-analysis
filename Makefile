# author: Prithvi Surekha, Oliver Gullery 
# date: 2024-03-12

all: data/airbnb_data_2023.csv \
     data \
     results/figures/corr_heat_map.jpg \
     results/figures/listing_locations.jpg \
     results/figures/price_vs_reviews.jpg \
     results/figures/price_vs_reviews_per_month.jpg \
     results/figures/neighbourhood_groups_boxplots.jpg \
     results/figures/room_type_boxplots.jpg \
     results/figures/price_histogram.jpg \
     results/tables/correlations_ranked.csv \
     results/tables/dummy_classification_report.csv \
     results/tables/knn_classification_report.csv \
     results/tables/hyperparam_classification_report.csv

# download data makefile build
data/airbnb_data_2023.csv: src/01_fetch_data_and_export.py
	python src/01_fetch_data_and_export.py \
	--input_file="http://data.insideairbnb.com/united-states/ny/new-york-city/2023-12-04/visualisations/listings.csv"\
	--out_dir="data/raw/airbnb_data_2023.csv"

# data preprocesssing makefile build
data: data/cleaned/X_train.csv \
      data/cleaned/X_test.csv \
      data/cleaned/y_train.csv \
      data/cleaned/y_test.csv \
      data/cleaned/test_df.csv \
      data/cleaned/train_df.csv

data/cleaned/X_train.csv data/cleaned/X_test.csv data/cleaned/y_train.csv data/cleaned/y_test.csv data/cleaned/test_df.csv data/cleaned/train_df.csv: data/airbnb_data_2023.csv src/02_data_preprocessing.py
	python src/02_data_preprocessing.py \
	--input_dir="data/airbnb_data_2023.csv"\
	--out_dir="data/cleaned"

# visualization makefile build
results/figures/corr_heat_map.jpg results/figures/listing_locations.jpg results/figures/price_vs_reviews.jpg results/figures/price_vs_reviews_per_month.jpg results/figures/neighbourhood_groups_boxplots.jpg results/figures/room_type_boxplots.jpg results/figures/price_histogram.jpg results/tables/correlations_ranked.csv: src/visualization.py data/cleaned/train_df.csv
	python src/visualization.py \
	--input_file="data/cleaned/train_df.csv"\
	--viz_out_dir="results/figures"\
	--tbl_out_dir="results/tables"

# model makefile build
results/tables/dummy_classification_report.csv results/tables/knn_classification_report.csv results/tables/hyperparam_classification_report.csv: src/04_model.py data/cleaned/X_train.csv data/cleaned/X_test.csv data/cleaned/y_train.csv data/cleaned/y_test.csv
	python src/04_model.py \
	--input_dir="data/cleaned"\
	--tbl_out_dir="results/tables"

# render to html
reports/milestone_2.html: results/milestone_2.qmd
	quarto render reports/milestone_2.qmd --to html

# render to pdf
reports/milestone_2.pdf: results/milestone_2.qmd
	quarto render reports/milestone_2.qmd --to pdf

#remove all targeted files using 'make clean'
clean:
	rm -rf data/airbnb_data_2023.csv \
	data/cleaned/X_train.csv \
	data/cleaned/X_test.csv \
	data/cleaned/y_train.csv \
	data/cleaned/y_test.csv \
	data/cleaned/test_df.csv \
	data/cleaned/train_df.csv \
	results/figures/corr_heat_map.jpg \
	results/figures/listing_locations.jpg \
	results/figures/price_vs_reviews.jpg \
	results/figures/price_vs_reviews_per_month.jpg \
	results/figures/neighbourhood_groups_boxplots.jpg \
	results/figures/room_type_boxplots.jpg \
	results/figures/price_histogram.jpg \
	results/tables/correlations_ranked.csv \
	results/tables/dummy_classification_report.csv \
	results/tables/knn_classification_report.csv \
	results/tables/hyperparam_classification_report.csv \
	reports/milestone_2.html \
	reports/milestone_2.pdf
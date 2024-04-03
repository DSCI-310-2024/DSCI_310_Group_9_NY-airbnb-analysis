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
     results/tables/hyperparam_classification_report.csv \
	 reports/milestone_3.html \
	 reports/milestone_3.pdf

# download data makefile build
data/airbnb_data_2023.csv: scripts/fetch_data_and_export.py
	python scripts/fetch_data_and_export.py \

# data preprocesssing makefile build
data: data/cleaned/X_train.csv \
      data/cleaned/X_test.csv \
      data/cleaned/y_train.csv \
      data/cleaned/y_test.csv \
      data/cleaned/test_df.csv \
      data/cleaned/train_df.csv

data/cleaned/X_train.csv data/cleaned/X_test.csv data/cleaned/y_train.csv data/cleaned/y_test.csv data/cleaned/test_df.csv data/cleaned/train_df.csv: data/airbnb_data_2023.csv scripts/data_preprocessing.py
	python scripts/data_preprocessing.py \

# visualization makefile build
results/figures/corr_heat_map.jpg results/figures/listing_locations.jpg results/figures/price_vs_reviews.jpg results/figures/price_vs_reviews_per_month.jpg results/figures/neighbourhood_groups_boxplots.jpg results/figures/room_type_boxplots.jpg results/figures/price_histogram.jpg results/tables/correlations_ranked.csv: data/cleaned/train_df.csv scripts/visualizations.py
	python scripts/visualizations.py \

# model makefile build
results/tables/dummy_classification_report.csv results/tables/knn_classification_report.csv results/tables/hyperparam_classification_report.csv: scripts/model.py data/cleaned/X_train.csv data/cleaned/X_test.csv data/cleaned/y_train.csv data/cleaned/y_test.csv
	python scripts/model.py \

# render to html
reports/milestone_3.html: reports/milestone_3.qmd
	quarto render reports/milestone_3.qmd --to html

# render to pdf
reports/milestone_3.pdf: reports/milestone_3.qmd
	quarto render reports/milestone_3.qmd --to pdf

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
	reports/milestone_3.html
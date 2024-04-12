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
	 reports/final_report.html \
	 reports/final_report.pdf

# download data makefile build
data/airbnb_data_2023.csv: scripts/ny_airbnb_data.py
	python scripts/ny_airbnb_data.py \

# data preprocesssing makefile build
data: data/cleaned/X_train.csv \
      data/cleaned/X_test.csv \
      data/cleaned/y_train.csv \
      data/cleaned/y_test.csv \
      data/cleaned/test_df.csv \
      data/cleaned/train_df.csv

data/cleaned/X_train.csv data/cleaned/X_test.csv data/cleaned/y_train.csv data/cleaned/y_test.csv data/cleaned/test_df.csv data/cleaned/train_df.csv: data/airbnb_data_2023.csv scripts/ny_airbnb_data.py
	python scripts/ny_airbnb_data.py \

# visualization makefile build
results/figures/corr_heat_map.jpg results/figures/listing_locations.jpg results/figures/price_vs_reviews.jpg results/figures/price_vs_reviews_per_month.jpg results/figures/neighbourhood_groups_boxplots.jpg results/figures/room_type_boxplots.jpg results/figures/price_histogram.jpg results/tables/correlations_ranked.csv: data/cleaned/train_df.csv scripts/ny_airbnb_plot.py
	python scripts/ny_airbnb_plot.py \

# model makefile build
results/tables/dummy_classification_report.csv results/tables/knn_classification_report.csv results/tables/hyperparam_classification_report.csv: scripts/ny_airbnb_analysis.py data/cleaned/X_train.csv data/cleaned/X_test.csv data/cleaned/y_train.csv data/cleaned/y_test.csv
	python scripts/ny_airbnb_analysis.py \

# render to html
reports/final_report.html: reports/final_report.qmd
	quarto render reports/final_report.qmd --to html

# render to pdf
reports/final_report.pdf: reports/final_report.qmd
	quarto render reports/final_report.qmd --to pdf

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
	reports/final_report.html
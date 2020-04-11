#
# Created by Faisal Amir
# FrogoBox Inc License
# -----------------------------------------
# Mini-ML-Air-BnB
# Copyright (C) 08/04/2020.      
# All rights reserved
# -----------------------------------------
# Name     : Muhammad Faisal Amir
# E-mail   : faisalamircs@gmail.com
# Github   : github.com/amirisback
# LinkedIn : linkedin.com/in/faisalamircs
# -----------------------------------------
# FrogoBox Software Industries
# 
# /
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from com.frogobox.base.config import *
from matplotlib import style
from com.frogobox.algorithm.kmeans import Kmeans
from com.frogobox.base.helper import cast_to_int, print_border_line

style.use('ggplot')


def create_result_clustering(column_label, kmeans, save_path_file):
    item_column_0 = []
    item_column_1 = []
    item_column_2 = []
    item_column_3 = []
    result_label_cluster = []

    for classification in kmeans.classes:
        for column in kmeans.classes[classification]:
            item_column_0.append(cast_to_int(column[0]))
            item_column_1.append(cast_to_int(column[1]))
            item_column_2.append(cast_to_int(column[2]))
            item_column_3.append(cast_to_int(column[3]))
            label_cluster = classification + 1
            result_label_cluster.append(COLUMN_CLASS + "_" + str(label_cluster))

    clustering_data_frame = pd.DataFrame({column_label[0]: item_column_0,
                                          column_label[1]: item_column_1,
                                          column_label[2]: item_column_2,
                                          column_label[3]: item_column_3,
                                          COLUMN_CLASS: result_label_cluster})

    print_border_line()
    print("Result Clustering : " + save_path_file)
    print_border_line()
    print(clustering_data_frame)
    print()

    # Create clustering result csv
    clustering_data_frame.to_csv(save_path_file, index=False)


def create_image_result_cluster(kmeans):
    print("Drawing Cluster ...")

    for centroid in kmeans.centroids:
        plt.scatter(kmeans.centroids[centroid][0],
                    kmeans.centroids[centroid][1],
                    marker="o",
                    color="k",
                    s=150,
                    linewidths=5)

    for classification in kmeans.classes:
        color = COLORS_CLUSTERING[classification]
        for featureset in kmeans.classes[classification]:
            plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)

    plt.show()


def clustering(path_file_raw_dataset, column_label, save_path_file):
    label_encoder = LabelEncoder()

    raw_data_set = pd.read_csv(path_file_raw_dataset)
    raw_data_set = raw_data_set[column_label]  # ['room_type', 'price', 'minimum_nights', 'number_of_reviews']

    raw_data_set[column_label[0]] = label_encoder.fit_transform(raw_data_set[column_label[0]])

    x = raw_data_set.values
    kmeans = Kmeans()
    kmeans.fit(x)
    create_result_clustering(column_label, kmeans, save_path_file)
    # create_image_result_cluster(kmeans)

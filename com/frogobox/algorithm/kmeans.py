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

import numpy as np

np.seterr(divide='ignore', invalid='ignore')


class Kmeans:
    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def fit(self, data):

        self.centroids = {}

        # inisialasi centroid
        for i in range(self.k):
            self.centroids[i] = data[i]

        # Mulai Iterasi
        for i in range(self.max_iterations):
            self.classes = {}
            for i in range(self.k):
                self.classes[i] = []

            # Remukan jarak terdekat dengan centroid lalu pilih
            for features in data:
                distances = [np.linalg.norm(features - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classes[classification].append(features)

            previous = dict(self.centroids)

            # rata-rata datapoints cluster untuk menghitung ulang centroid
            for classification in self.classes:
                self.centroids[classification] = np.average(self.classes[classification], axis=0)

            isOptimal = True

            for centroid in self.centroids:

                original_centroid = previous[centroid]
                curr = self.centroids[centroid]

                if np.sum((curr - original_centroid) / original_centroid * 100.0) > self.tolerance:
                    isOptimal = False

            # Hentikan looping jika tida terjadi perubuhan centroid
            if isOptimal:
                break

    def prediction(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
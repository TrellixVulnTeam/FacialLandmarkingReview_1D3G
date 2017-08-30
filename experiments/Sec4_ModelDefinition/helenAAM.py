#! /usr/bin/env python
# -*- coding: utf-8 -*-
# S.D.G

"""AAM test for HELEN dataset



:author: Ben Johnston
:license: 3-Clause BSD

"""

# Imports
import os
import menpo.io as mio
from aam import AAM 
from menpofit.aam import HolisticAAM, PatchAAM


class HelenAAM(AAM):
    """ Helen AAM class """


    def __init__(self, path_to_data, model_type=HolisticAAM, filename='helen_aam.txt', verbose=True):

        super(HelenAAM, self).__init__(
            path_to_data, model_type, filename, verbose)

    def _crop_grayscale_images(self, filepath, crop_percentage):

        images = []

        for i in mio.import_images(filepath, max_images=None, verbose=self.verbose):
            i = i.crop_to_landmarks_proportion(crop_percentage)

            # Convert to grayscale if required
            if i.n_channels == 3:
                i = i.as_greyscale() # Default to luminosity

            # Due to large training set size use generators for better memory 
            # efficiency
            yield i


    def load_data(self, crop_percentage=0.1):
        """ Load the images and landmarks in an menpo.io
        format and crop the images using the specified
        landmarks as a guide
        
        Parameters
        ---------
        
        """

        train_path = os.path.join(self.filepath, 'trainset')
        self.train_set = self._crop_grayscale_images(train_path, crop_percentage)

        test_path = os.path.join(self.filepath, 'testset')
        self.test_set = self._crop_grayscale_images(test_path, crop_percentage)

if __name__ == "__main__":

    a = HelenAAM('~/datasets/HELEN', PatchAAM, 'helen_patch.txt')
    a.load_data()
    a.train_model(diagonal=200, max_shape_components=None, max_appearance_components=None)
    a.fit_model()
    a.predict_test_set()
    a.generate_cdf()
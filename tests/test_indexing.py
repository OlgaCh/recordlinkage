from __future__ import print_function

import unittest

import pandas.util.testing as pdt
import recordlinkage
import numpy as np
import pandas as pd

from recordlinkage import datasets

# Two larger numeric dataframes
df_large_numeric_1 = pd.DataFrame(np.arange(1000))
df_large_numeric_1.index.name = None
df_large_numeric_2 = pd.DataFrame(np.arange(1000))
df_large_numeric_2.index.name = None

# nosetests tests/test_indexing.py:TestIndexApi
class TestIndexApi(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.data_A = {
            'name':['Bob', 'Anne', 'Micheal'],
            'age': [40, 45, 69]
            }
        self.data_B = {
            'name':['Bob', 'Anne', 'Micheal'],
            'age': [40, 45, 68]
            }

        self.index = ['rec1','rec2','rec3']

    def test_instance(self):

        A = pd.DataFrame(self.data_A)
        B = pd.DataFrame(self.data_B)

        index_cl = recordlinkage.Pairs(A, B)

        # index full
        pairs = index_cl.full()
        self.assertIsInstance(pairs, pd.MultiIndex)

        # index block
        pairs = index_cl.block('name')
        self.assertIsInstance(pairs, pd.MultiIndex)

        # index sni
        pairs = index_cl.sortedneighbourhood('name', 3)
        self.assertIsInstance(pairs, pd.MultiIndex)

        # index eye
        pairs = index_cl.eye()
        self.assertIsInstance(pairs, pd.MultiIndex)

        # index random
        pairs = index_cl.random(3)
        self.assertIsInstance(pairs, pd.MultiIndex)

    def test_index_names_different(self):

        index_A = pd.Index(self.index, name='left')
        index_B = pd.Index(self.index, name='right')

        A = pd.DataFrame(self.data_A, index=index_A)
        B = pd.DataFrame(self.data_B, index=index_B)

        # index full
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.full()
        self.assertEqual(pairs.names, ['left', 'right'])

        # index block
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.block('name')
        self.assertEqual(pairs.names, ['left', 'right'])

        # index sni 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.sortedneighbourhood('name')
        self.assertEqual(pairs.names, ['left', 'right'])

        # index eye 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.eye()
        self.assertEqual(pairs.names, ['left', 'right'])

        # index random 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.random(3)
        self.assertEqual(pairs.names, ['left', 'right'])

    def test_index_names_equal(self):

        index_A = pd.Index(self.index, name='leftright')
        index_B = pd.Index(self.index, name='leftright')

        A = pd.DataFrame(self.data_A, index=index_A)
        B = pd.DataFrame(self.data_B, index=index_B)

        # index full
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.full()
        self.assertEqual(pairs.names, ['leftright', 'leftright'])

        # index block
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.block('name')
        self.assertEqual(pairs.names, ['leftright', 'leftright'])

        # index sni 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.sortedneighbourhood('name')
        self.assertEqual(pairs.names, ['leftright', 'leftright'])

        # index eye 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.eye()
        self.assertEqual(pairs.names, ['leftright', 'leftright'])

        # index random 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.random(3)
        self.assertEqual(pairs.names, ['leftright', 'leftright'])

    def test_index_names_none(self):

        index_A = pd.Index(self.index)
        index_B = pd.Index(self.index)

        A = pd.DataFrame(self.data_A, index=index_A)
        B = pd.DataFrame(self.data_B, index=index_B)

        # index full
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.full()
        self.assertEqual(pairs.names, [None, None])

        # index block
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.block('name')
        self.assertEqual(pairs.names, [None, None])

        # index sni 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.sortedneighbourhood('name')
        self.assertEqual(pairs.names, [None, None])

        # index eye 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.eye()
        self.assertEqual(pairs.names, [None, None])

        # index random 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.random(3)
        self.assertEqual(pairs.names, [None, None])

    def test_index_names_one_none(self):

        index_A = pd.Index(self.index)
        index_B = pd.Index(self.index)

        A = pd.DataFrame(self.data_A, index=index_A)
        B = pd.DataFrame(self.data_B, index=pd.Index(index_B, name='right'))

        # index full
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.full()
        self.assertEqual(pairs.names, [None, 'right'])

        # index block
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.block('name')
        self.assertEqual(pairs.names, [None, 'right'])

        # index sni 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.sortedneighbourhood('name')
        self.assertEqual(pairs.names, [None, 'right'])

        # index eye 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.eye()
        self.assertEqual(pairs.names, [None, 'right'])

        # index random 
        index_cl = recordlinkage.Pairs(A, B)
        pairs = index_cl.random(3)
        self.assertEqual(pairs.names, [None, 'right'])







# nosetests tests/test_indexing.py:TestIndexing
class TestIndexing(unittest.TestCase):

    def test_full_index_names(self):

        df1 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=pd.Index(['001', '002', '003'], name='index_A'))
        df2 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=pd.Index(['001', '002', '003'], name='index_B'))

        index = recordlinkage.Pairs(df1, df2)
        pairs = index.full()

        index_exp = [('001', '001'), ('001', '002'), ('001', '003'), ('002', '001'), ('002', '002'), ('002', '003'), ('003', '001'), ('003', '002'), ('003', '003')]

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), len(df1)*len(df2))

    def test_full_index(self):

        index = recordlinkage.Pairs(df_large_numeric_1, df_large_numeric_2)
        pairs = index.full()

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(1000000, len(df_large_numeric_1)*len(df_large_numeric_2))

    def test_block_index_unique(self):

        df1 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=pd.Index(['001', '002', '003'], name='index_A'))
        df2 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=pd.Index(['001', '002', '003'], name='index_B'))

        index = recordlinkage.Pairs(df1, df2)
        pairs = index.block('name')

        index_exp = [('001', '001'), ('002', '002'),('003', '003')]

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), 3)

    def test_sortedneighbourhood_index_unique(self):

        df1 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=pd.Index(['001', '002', '003'], name='index_A'))
        df2 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=pd.Index(['001', '002', '003'], name='index_B'))

        index = recordlinkage.Pairs(df1, df2)
        pairs = index.sortedneighbourhood('name')

        index_exp = [('001', '001'), ('002', '002'),('003', '003')]

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

    #####################################
    ##          RANDOM INDEXING        ##
    #####################################

    def test_random_index_unique(self):

        n_pairs = 5

        df1 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=pd.Index(['001', '002', '003'], name='index_A'))
        df2 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=pd.Index(['001', '002', '003'], name='index_B'))

        index = recordlinkage.Pairs(df1, df2)
        pairs = index.random(n_pairs)

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), n_pairs)

    def test_random_index_less_than_25(self):

        n_pairs = 10000

        index = recordlinkage.Pairs(df_large_numeric_1, df_large_numeric_2)
        pairs = index.random(n_pairs)

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), n_pairs)

    def test_random_index_more_than_25(self):

        n_pairs = 300000

        index = recordlinkage.Pairs(df_large_numeric_1, df_large_numeric_2)
        pairs = index.random(n_pairs)

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), n_pairs)

    def test_random_index_linking(self):

        dfA, dfB = datasets.load_febrl4()
        # dfB.index.name = dfB.index.name + "_"

        index = recordlinkage.Pairs(dfA, dfB)
        pairs = index.random(1000)

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

        # Check is number of pairs is correct
        self.assertTrue(len(pairs) <= 1000)

    def test_full_index_linking(self):

        dfA, dfB = datasets.load_febrl4()
        # dfB.index.name = dfB.index.name + "_"

        index = recordlinkage.Pairs(dfA, dfB)
        pairs = index.full()

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), len(dfA)*len(dfB))

    def test_block_index_linking(self):

        dfA, dfB = datasets.load_febrl4()
        # dfB.index.name = dfB.index.name + "_"

        index = recordlinkage.Pairs(dfA, dfB)
        pairs = index.block('given_name')

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

    def test_qgram_index_linking(self):

        dfA, dfB = datasets.load_febrl4()
        # dfB.index.name = dfB.index.name + "_"

        index = recordlinkage.Pairs(dfA[0:100], dfB[0:100])
        pairs = index.qgram('given_name')

        # Check if index is unique
        self.assertTrue(pairs.is_unique)

    def test_sorted_index_linking(self):

        dfA, dfB = datasets.load_febrl4()
        # dfB.index.name = dfB.index.name + "_"

        index = recordlinkage.Pairs(dfA, dfB)
        pairs = index.sortedneighbourhood('given_name')

        # Check if index is unique
        self.assertTrue(pairs.is_unique)


    def test_blocking_special_case_of_sorting(self):

        dfA, dfB = datasets.load_febrl4()
        # dfB.index.name = dfB.index.name + "_"

        index = recordlinkage.Pairs(dfA, dfB)
        bl = index.block('given_name')
        sn = index.sortedneighbourhood('given_name', window=1)

        print('The number of record pairs found with blocking', len(bl))
        print('The number of record pairs found with sorted neighbourhood indexing', len(sn))
        
        # The length of the union should be the same as the length of bl or sn.
        self.assertEqual(len(bl), len(sn))

    def test_full_iter_index_linking(self):

        dfA, dfB = datasets.load_febrl4()
        # dfB.index.name = dfB.index.name + "_"

        index_chucks = recordlinkage.Pairs(dfA, dfB, chunks=(100,200))
        index = recordlinkage.Pairs(dfA, dfB)

        # Compute pairs in one iteration
        pairs_single = index.full()

        # Compute pairs in iterations
        n_pairs_iter = 0
        for pairs in index_chucks.full():

            print (len(pairs))
            n_pairs_iter +=  len(pairs)

            # Check if index is unique
            self.assertTrue(pairs.is_unique)

        self.assertEqual(len(pairs_single), n_pairs_iter)

        # Check is number of pairs is correct
        self.assertEqual(n_pairs_iter, len(dfA)*len(dfB))

    def test_full_iter_index_deduplication(self):

        dfA = datasets.load_febrl1()

        # Compute pairs in one iteration
        index = recordlinkage.Pairs(dfA)
        pairs_single = index.full()

        # Compute pairs in iterations
        n_pairs_iter = 0

        index_chucks = recordlinkage.Pairs(dfA, chunks=100)

        for pairs in index_chucks.full():

            print (len(pairs))
            n_pairs_iter += len(pairs)

            # print (pairs)

            # Check if index is unique
            self.assertTrue(pairs.is_unique)

        self.assertEqual(len(pairs_single), n_pairs_iter)

        # Check is number of pairs is correct
        self.assertEqual(n_pairs_iter, (len(dfA)-1)*len(dfA)/2)

    def test_reduction_ratio(self):

        dfA, dfB = datasets.load_febrl4()
        # dfB.index.name = dfB.index.name + "_"

        index = recordlinkage.Pairs(dfA, dfB)
        pairs = index.full()

        rr = index.reduction

        self.assertEqual(rr, 0)






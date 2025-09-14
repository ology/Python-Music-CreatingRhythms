import sys
sys.path.append('./src')
import unittest
from music_creatingrhythms.music_creatingrhythms import Rhythms
from math import isclose

class TestMusicCreatingRhythms(unittest.TestCase):
    def setUp(self):
        self.mcr = Rhythms(verbose=1)

    def test_defaults(self):
        self.assertEqual(self.mcr.verbose, 1)

    def test_binary_to_intervals(self):
        self.assertEqual(self.mcr.b2int(''), [])
        self.assertEqual(self.mcr.b2int('0'), [1])
        self.assertEqual(self.mcr.b2int('110100'), [1,2,3])
        self.assertEqual(self.mcr.b2int('101011010'), [2,2,1,2,2])
        self.assertEqual(self.mcr.b2int('10001000'), [4,4])
        self.assertEqual(self.mcr.b2int('00000000'), [8])
        self.assertEqual(self.mcr.b2int('1111'), [1,1,1,1])
        self.assertEqual(self.mcr.b2int('11111111'), [1,1,1,1,1,1,1,1])

    def test_continued_fraction_convergent(self):
        self.assertEqual(self.mcr.cfcv(1,2), [3,2])
        self.assertEqual(self.mcr.cfcv(1,2,2), [7,5])
        self.assertEqual(self.mcr.cfcv(1,2,2,2), [17,12])
        self.assertEqual(self.mcr.cfcv(1,1,2), [5,3])
        self.assertEqual(self.mcr.cfcv(1,1,2,1,2), [19,11])

    def test_continued_fraction_square_root(self):
        self.assertEqual(self.mcr.cfsqrt(0), [0])
        self.assertEqual(self.mcr.cfsqrt(1), [1])
        self.assertEqual(self.mcr.cfsqrt(2), [1, 2])
        self.assertEqual(self.mcr.cfsqrt(3), [1, 1, 2])
        self.assertEqual(self.mcr.cfsqrt(4), [2])
        self.assertEqual(self.mcr.cfsqrt(5), [2, 4])
        self.assertEqual(self.mcr.cfsqrt(6), [2, 2, 4])
        self.assertEqual(self.mcr.cfsqrt(7), [2, 1, 1, 1, 4])
        self.assertEqual(self.mcr.cfsqrt(8), [2, 1, 4])
        self.assertEqual(self.mcr.cfsqrt(9), [3])
        self.assertEqual(self.mcr.cfsqrt(42), [6, 2, 12])

    def test_chsequl(self):
        self.assertEqual(self.mcr.chsequl('l',1,0), [0])
        self.assertEqual(self.mcr.chsequl('u',1,0), [1])
        self.assertEqual(self.mcr.chsequl('l',1,1), [0,1])
        self.assertEqual(self.mcr.chsequl('u',1,1), [1,0])
        self.assertEqual(self.mcr.chsequl('l',1,2), [0,0,1])
        self.assertEqual(self.mcr.chsequl('u',1,2), [1,0,0])
        self.assertEqual(self.mcr.chsequl('l',2,0), [0,1])
        self.assertEqual(self.mcr.chsequl('u',2,0), [1,1])
        self.assertEqual(self.mcr.chsequl('l',2,1), [0,1,1])
        self.assertEqual(self.mcr.chsequl('u',2,1), [1,1,0])
        self.assertEqual(self.mcr.chsequl('l',2,2), [0,1,0,1])
        self.assertEqual(self.mcr.chsequl('u',2,2), [1,0,1,0])
        self.assertEqual(self.mcr.chsequl('l',11,5), [0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1])
        self.assertEqual(self.mcr.chsequl('u',11,5), [1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0])
        self.assertEqual(self.mcr.chsequl('l',11,5,4), [0,1,1,0])
        self.assertEqual(self.mcr.chsequl('u',11,5,4), [1,1,1,0])

    def test_comp(self):
        self.assertEqual(self.mcr.comp(1), [[1]])
        self.assertEqual(self.mcr.comp(2), [[1,1],[2]])
        self.assertEqual(self.mcr.comp(3), [[1,1,1],[1,2],[2,1],[3]])
        self.assertEqual(self.mcr.comp(4), [[1,1,1,1],[1,1,2],[1,2,1],[1,3],[2,1,1],[2,2],[3,1],[4]])

    def test_compa(self):
        self.assertEqual(self.mcr.compa(1,1), [[1]])
        self.assertEqual(self.mcr.compa(1,2), [])
        self.assertEqual(self.mcr.compa(2,2), [[2]])
        self.assertEqual(self.mcr.compa(3,1), [[1,1,1]])
        self.assertEqual(self.mcr.compa(4,1), [[1,1,1,1]])
        self.assertEqual(self.mcr.compa(4,1,2), [[1,1,1,1],[1,1,2],[1,2,1],[2,1,1],[2,2]])
        self.assertEqual(self.mcr.compa(4,1,2,3), [[1,1,1,1],[1,1,2],[1,2,1],[1,3],[2,1,1],[2,2],[3,1]])

    def test_compam(self):
        self.assertEqual(self.mcr.compam(1,1,1), [[1]])
        self.assertEqual(self.mcr.compam(1,2,1), [])
        self.assertEqual(self.mcr.compam(2,2,1), [[1,1]])
        self.assertEqual(self.mcr.compam(3,3,1), [[1,1,1]])
        self.assertEqual(self.mcr.compam(4,4,1), [[1,1,1,1]])
        self.assertEqual(self.mcr.compam(4,3,1,2), [[1,1,2],[1,2,1],[2,1,1]])
        self.assertEqual(self.mcr.compam(4,2,1,2,3), [[1,3],[2,2],[3,1]])

    def test_compm(self):
        self.assertEqual(self.mcr.compm(1,1), [[1]])
        self.assertEqual(self.mcr.compm(1,2), [])
        self.assertEqual(self.mcr.compm(2,2), [[1,1]])
        self.assertEqual(self.mcr.compm(3,2), [[1,2],[2,1]])
        self.assertEqual(self.mcr.compm(4,2), [[1,3],[2,2],[3,1]])
        self.assertEqual(self.mcr.compm(5,2), [[1,4],[2,3],[3,2],[4,1]])
        self.assertEqual(self.mcr.compm(6,2), [[1,5],[2,4],[3,3],[4,2],[5,1]])

    def test_compmrnd(self):
        self.assertEqual(sum(self.mcr.compmrnd(0,0)), 0)
        self.assertEqual(sum(self.mcr.compmrnd(1,1)), 1)
        self.assertEqual(sum(self.mcr.compmrnd(16,4)), 16)

    def test_comprnd(self):
        self.assertEqual(sum(self.mcr.comprnd(0)), 0)
        self.assertEqual(sum(self.mcr.comprnd(1)), 1)
        self.assertEqual(sum(self.mcr.comprnd(16)), 16)

    def test_count_ones(self):
        self.assertEqual(self.mcr.count_ones(0), 0)
        self.assertEqual(self.mcr.count_ones([0]), 0)
        self.assertEqual(self.mcr.count_ones(1), 1)
        self.assertEqual(self.mcr.count_ones([1]), 1)
        self.assertEqual(self.mcr.count_ones('010'), 1)
        self.assertEqual(self.mcr.count_ones([0,1,0]), 1)

    # def test_count_zeros(self):
    #     self.assertEqual(self.mcr.count_zeros(0), 1)
    #     self.assertEqual(self.mcr.count_zeros([0]), 1)
    #     self.assertEqual(self.mcr.count_zeros(1), 0)
    #     self.assertEqual(self.mcr.count_zeros([1]), 0)
    #     self.assertEqual(self.mcr.count_zeros('010'), 2)
    #     self.assertEqual(self.mcr.count_zeros([0,1,0]), 2)

    # def test_de_bruijn(self):
    #     self.assertEqual(self.mcr.de_bruijn(0), [0])
    #     self.assertEqual(self.mcr.de_bruijn(1), [1,0])
    #     self.assertEqual(self.mcr.de_bruijn(2), [1,1,0,0])
    #     self.assertEqual(self.mcr.de_bruijn(3), [1,1,1,0,1,0,0,0])

    # def test_euclid(self):
    #     self.assertEqual(self.mcr.euclid(1,1), [1])
    #     self.assertEqual(self.mcr.euclid(1,2), [1,0])
    #     self.assertEqual(self.mcr.euclid(1,3), [1,0,0])
    #     self.assertEqual(self.mcr.euclid(1,4), [1,0,0,0])
    #     self.assertEqual(self.mcr.euclid(2,4), [1,0,1,0])
    #     self.assertEqual(self.mcr.euclid(3,4), [1,1,0,1])
    #     self.assertEqual(self.mcr.euclid(4,4), [1,1,1,1])

    # def test_int2b(self):
    #     self.assertEqual(self.mcr.int2b([[1,2,3]]), [[1,1,0,1,0,0]])
    #     self.assertEqual(self.mcr.int2b([[1],[2],[3]]), [[1],[1,0],[1,0,0]])

    # def test_invert_at(self):
    #     parts = [1,0,1,0,0]
    #     self.assertEqual(self.mcr.invert_at(0, parts), [0,1,0,1,1])
    #     self.assertEqual(self.mcr.invert_at(1, parts), [1,1,0,1,1])
    #     self.assertEqual(self.mcr.invert_at(2, parts), [1,0,0,1,1])
    #     self.assertEqual(self.mcr.invert_at(3, parts), [1,0,1,1,1])
    #     self.assertEqual(self.mcr.invert_at(4, parts), [1,0,1,0,1])
    #     self.assertEqual(self.mcr.invert_at(5, parts), [1,0,1,0,0])

    # def test_neck(self):
    #     self.assertEqual(self.mcr.neck(1), [[1],[0]])
    #     self.assertEqual(self.mcr.neck(2), [[1,1],[1,0],[0,0]])
    #     self.assertEqual(self.mcr.neck(3), [[1,1,1],[1,1,0],[1,0,0],[0,0,0]])
    #     self.assertEqual(self.mcr.neck(4), [[1,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,1,0],[1,0,0,0],[0,0,0,0]])

    # def test_necka(self):
    #     self.assertEqual(self.mcr.necka(1,1), [[1]])
    #     self.assertEqual(self.mcr.necka(1,2), [])
    #     self.assertEqual(self.mcr.necka(2,2), [[1,0]])
    #     self.assertEqual(self.mcr.necka(3,1), [[1,1,1]])
    #     self.assertEqual(self.mcr.necka(4,1), [[1,1,1,1]])
    #     self.assertEqual(self.mcr.necka(4,1,2), [[1,1,1,1],[1,1,1,0],[1,0,1,0]])
    #     self.assertEqual(self.mcr.necka(4,1,2,3), [[1,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,1,0]])

    # def test_neckam(self):
    #     self.assertEqual(self.mcr.neckam(1,1,1), [[1]])
    #     self.assertEqual(self.mcr.neckam(1,2,1), [])
    #     self.assertEqual(self.mcr.neckam(2,2,1), [[1,1]])
    #     self.assertEqual(self.mcr.neckam(3,3,1), [[1,1,1]])
    #     self.assertEqual(self.mcr.neckam(4,4,1), [[1,1,1,1]])
    #     self.assertEqual(self.mcr.neckam(4,3,1,2), [[1,1,1,0]])
    #     self.assertEqual(self.mcr.neckam(4,2,1,2,3), [[1,1,0,0],[1,0,1,0]])

    # def test_neckm(self):
    #     self.assertEqual(self.mcr.neckm(1,1), [[1]])
    #     self.assertEqual(self.mcr.neckm(1,2), [])
    #     self.assertEqual(self.mcr.neckm(2,2), [[1,1]])
    #     self.assertEqual(self.mcr.neckm(3,2), [[1,1,0]])
    #     self.assertEqual(self.mcr.neckm(4,2), [[1,1,0,0],[1,0,1,0]])
    #     self.assertEqual(self.mcr.neckm(5,2), [[1,1,0,0,0],[1,0,1,0,0]])
    #     self.assertEqual(self.mcr.neckm(6,2), [[1,1,0,0,0,0],[1,0,1,0,0,0],[1,0,0,1,0,0]])

    # def test_part(self):
    #     self.assertEqual(self.mcr.part(1), [[1]])
    #     self.assertEqual(self.mcr.part(2), [[1,1],[2]])
    #     self.assertEqual(self.mcr.part(3), [[1,1,1],[1,2],[3]])
    #     self.assertEqual(self.mcr.part(4), [[1,1,1,1],[1,1,2],[2,2],[1,3],[4]])

    # def test_parta(self):
    #     self.assertEqual(self.mcr.parta(1,1), [[1]])
    #     self.assertEqual(self.mcr.parta(1,2), [])
    #     self.assertEqual(self.mcr.parta(2,2), [[2]])
    #     self.assertEqual(self.mcr.parta(3,1), [[1,1,1]])
    #     self.assertEqual(self.mcr.parta(4,1), [[1,1,1,1]])
    #     self.assertEqual(self.mcr.parta(4,1,2), [[1,1,1,1],[1,1,2],[2,2]])
    #     self.assertEqual(self.mcr.parta(4,1,2,3), [[1,1,1,1],[1,1,2],[2,2],[1,3]])

    # def test_partam(self):
    #     self.assertEqual(self.mcr.partam(1,1,1), [[1]])
    #     self.assertEqual(self.mcr.partam(1,2,1), [])
    #     self.assertEqual(self.mcr.partam(2,2,1), [[1,1]])
    #     self.assertEqual(self.mcr.partam(3,3,1), [[1,1,1]])
    #     self.assertEqual(self.mcr.partam(4,4,1), [[1,1,1,1]])
    #     self.assertEqual(self.mcr.partam(4,3,1,2), [[1,1,2]])
    #     self.assertEqual(self.mcr.partam(4,2,1,2,3), [[1,3],[2,2]])

    # def test_partm(self):
    #     self.assertEqual(self.mcr.partm(1,1), [[1]])
    #     self.assertEqual(self.mcr.partm(1,2), [])
    #     self.assertEqual(self.mcr.partm(2,2), [[1,1]])
    #     self.assertEqual(self.mcr.partm(3,2), [[1,2]])
    #     self.assertEqual(self.mcr.partm(4,2), [[1,3],[2,2]])
    #     self.assertEqual(self.mcr.partm(5,2), [[1,4],[2,3]])
    #     self.assertEqual(self.mcr.partm(6,2), [[1,5],[2,4],[3,3]])

    # def test_permi(self):
    #     parts = [1,0,1]
    #     self.assertEqual(self.mcr.permi(parts), [[1,0,1],[1,1,0],[0,1,1],[0,1,1],[1,1,0],[1,0,1]])

    # def test_pfold(self):
    #     self.assertEqual(self.mcr.pfold(-1,1,1), [])
    #     self.assertEqual(self.mcr.pfold(1,1,1), [1])
    #     self.assertEqual(self.mcr.pfold(2,1,1), [1,1])
    #     self.assertEqual(self.mcr.pfold(3,1,1), [1,1,0])
    #     self.assertEqual(self.mcr.pfold(4,1,1), [1,1,0,1])
    #     self.assertEqual(self.mcr.pfold(15,4,0), [0,0,1,0,0,1,1,0,0,0,1,1,0,1,1])
    #     self.assertEqual(self.mcr.pfold(15,4,1), [1,0,0,0,1,1,0,0,1,0,0,1,1,1,0])

    # def test_reverse_at(self):
    #     parts = [1,0,1,0,0]
    #     self.assertEqual(self.mcr.reverse_at(0, parts), [0,0,1,0,1])
    #     self.assertEqual(self.mcr.reverse_at(1, parts), [1,0,0,1,0])
    #     self.assertEqual(self.mcr.reverse_at(2, parts), [1,0,0,0,1])
    #     self.assertEqual(self.mcr.reverse_at(3, parts), [1,0,1,0,0])
    #     self.assertEqual(self.mcr.reverse_at(4, parts), [1,0,1,0,0])

    # def test_rotate_n(self):
    #     parts = [1,0,1,0,0]
    #     self.assertEqual(self.mcr.rotate_n(0, parts), [1,0,1,0,0])
    #     self.assertEqual(self.mcr.rotate_n(1, parts), [0,1,0,1,0])
    #     self.assertEqual(self.mcr.rotate_n(2, parts), [0,0,1,0,1])
    #     self.assertEqual(self.mcr.rotate_n(3, parts), [1,0,0,1,0])
    #     self.assertEqual(self.mcr.rotate_n(4, parts), [0,1,0,0,1])
    #     self.assertEqual(self.mcr.rotate_n(5, parts), [1,0,1,0,0])

if __name__ == '__main__':
    unittest.main()

import unittest
from ComplexVector import *

a, b = [4, 1], [2, 6]
c, d = [7, 5], [2, 9]


class Test(unittest.TestCase):

    def testSuma(self):
        self.assertEqual(sumVec((a, b), (a, b)), [2, 6 ,2, 6])
        self.assertEqual(sumVec([a, c], [c, b]), [7,5,2,6])

    def testVectorInverso(self):
      self.assertEqual(inversavec([a,c]),[(-4,-1),(-7,-5)])
      self.assertEqual(inversavec([b,a]),[(-2,-6),(-4,-1)])

    def testEscalVect(self):
        self.assertEqual(vectoPorEscalar(b, [a, b]), [(2, 26), (-32, 24)])
        self.assertEqual(vectoPorEscalar(c, [b, c]), [(-16, 52), (24, 70)])

    def testSumaMatriz(self):
        self.assertEqual(adicionMat([[a, a], [b, b]], [[b, a], [a, b]]), [[(6, 7), (8, 2)], [(6, 7), (4, 12)]])
        self.assertEqual(adicionMat([[c, a], [a, b]], [[b, c], [b, b]]), [[(9, 11), (11, 6)], [(6, 7), (4, 12)]])

    #def testInversaMatriz(self):
     #  self.assertEqual(inversaMat([a, b, c]), [[[-1, -3]], [[-2, -4]], [[-6, -5]]])
      # self.assertEqual(inversaMat([[a, a, c], [c, b, a], [d, c, b]]),
       #                 [[[-1, -3], [-1, -3], [-6, -5]], [[-6, -5], [-2, -4], [-1, -3]],
        #                 [[-4, -9], [-6, -5], [-2, -4]]])

    def testEscalMatriz(self):
        self.assertEqual(matrizPorEscalar(d, [[c, a], [a, d]]), [[(-31, 73), (-1, 38)], [(-1, 38), (-77, 36)]])
        self.assertEqual(matrizPorEscalar(c, [[a, a], [b, b]]), [[(23, 27), (23, 27)], [(-16, 52), (-16, 52)]])

    def testTranspuesta(self):
        self.assertEqual(transpuesta([[b, a, a], [a, b, a]]), [[[2, 6], [4, 1]], [[4, 1], [2, 6]], [[4, 1], [4, 1]]])

    def testMatrizConjugada(self):
        self.assertEqual(conjugada([[b, a, c], [c, b, d]]),
                         [[(2, -6), (4, -1), (7, -5)], [(7, -5), (2, -6), (2, -9)]])

    def testMatrizAdjunta(self):
        self.assertEqual(adjunta([[b, a, a], [a, b, a]]),
                         [[(2, -6), (4, -1)], [(4, -1), (2, -6)], [(4, -1), (4, -1)]])

    def testMultiplicaMatrices(self):
        self.assertEqual(productoMat([[a, a], [b, b]], [[b, a], [a, b]]),
                         [[(17, 34), (17, 34)], [(-30, 50), (-30, 50)]])

    def testAccion(self):
        a, b, c, d, e = [1, 4], [4, 0], [7, -1], [0, 1], [5, 6]
        A, V = [[[0, 0], [0, -2]], [[0, 2], [0, 0]]], [[0, 1], [1, 0]]
        self.assertEqual(accion([[a, c, d], [b, c, b], [d, b, e]], [e, d, c]), [(-17, 40), (49, 27), (35, 46)])

    def testNorma(self):
        a, b = [3, 0], [-6, 0]
        c = [2, 0]
        N = [[6.5, 2.7], [3.1, -3.8]]
        self.assertEqual(normaVec([a, b, c]), (49) ** (1 / 2))
        self.assertEqual(normaVec(N), 5.489080068645383)

    def testProductoInterno(self):
        a, b = [3, 0], [-6, 0]
        c = [2, 0]
        self.assertEqual(productoInternVec([a, b, c], [a, b, c]), (49, 0))

    def testDistancia(self):
        a, b = [3, 0], [1, 0]
        c, d = [2, 0], [-1, 0]
        self.assertEqual(distaciaVec([a, b, c], [c, c, d]), 11 ** (1 / 2))

    def testIsUnitary(self):
        a, b = [1, 0], [0, 0]
        c = [0, 1]
        self.assertFalse(matrizUnitaria([[a, c], [b, c]]))
        self.assertFalse(matrizUnitaria([[c, a], [a, b]]))
        self.assertFalse(matrizUnitaria([[c, a], [b, a]]))

    def testHermitian(self):
        a, b = [7, 0], [6, 5]
        c, d = [6, -5], [-3, 0]
        e, f = [1, 0], [0, 0]
        self.assertFalse(matrizHermitiana([[a, b], [c, d]]))
        self.assertFalse(matrizHermitiana([[f, f], [e, e]]))

    def testTensor(self):
        mat1 = [[2, 0], [3, 0]]
        mat2 = [[4, 0], [6, 0], [3, 0]]
        self.assertEqual(productoTensor(mat1, mat2), [(8, 0), (12, 0), (6, 0), (12, 0), (18, 0), (9, 0)])


if __name__ == "__main__":
    unittest.main()
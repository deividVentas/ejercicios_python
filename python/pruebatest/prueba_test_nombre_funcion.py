import unittest

from prueba_nombre_funcion import formato_nombre

class Formato_correcto(unittest.TestCase):

	""" Aqui ponemos los casos que queremos evaluar """

	def test_nombre_apellidos(self):

		""" En estos casos trabajara el programa David Ventas """

		formato_nombres = formato_nombre('david', 'ventas')
		self.assertEqual(formato_nombres, 'David Ventas')

unittest.main()
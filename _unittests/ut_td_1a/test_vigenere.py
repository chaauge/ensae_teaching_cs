"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper.loghelper as skip_

from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.td_1a.vigenere import DecodeVigenereLongueurCle, DecodeVigenereCle, DecodeVigenere, CodeVigenere, CasseVigenere, code_vigenere


class TestVigenere (unittest.TestCase):

    def test_vigenere(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fold = os.path.join(os.path.split(__file__)[0], "data")

        # on lit Victor Hugo
        with open(os.path.join(fold, "hugo_dernier_jour_condamne.txt"), "r") as f:
            message = f.read()  # lit tout d'une seule traite

        # on limite la taille du fichier
        message = message[5000:7000]

        # on enleve les signes de ponctuation et on met en majuscule
        message = message.replace("\n", "")
        message = message.replace("\r", "")
        message = message.replace("\t", "")
        message = message.replace(" ", "")
        message = message.replace(",", "")
        message = message.replace(";", "")
        message = message.replace(":", "")
        message = message.replace(".", "")
        message = message.replace("'", "")
        message = message.replace("\"", "")
        message = message.replace("-", "")
        message = message.replace("!", "")
        message = message.replace("?", "")
        message = message.replace("(", "")
        message = message.replace(")", "")
        message = message.upper()

        # on code
        fLOG("on code, longueur du message ", len(message))
        cle = "VIGENERES"
        code = CodeVigenere(message, cle)
        memoire = cle
        cle = None   # on oublie la cle

        # on determine la longueur de la cle
        l = DecodeVigenereLongueurCle(code)
        # on determine la cle en suppose que la lettre E est la plus frequente
        # ne marche pas pour les textes anglais
        cle_code = DecodeVigenereCle(code, l)
        # decode le texte
        decode = DecodeVigenere(code, cle_code)

        assert "VIGENERES" == cle_code

        casse = CasseVigenere(code)
        assert len(code) == len(casse)
        assert casse.startswith(
            "IDERLACAUSEDUNCONDAMNEQUELCONQUEEXECUTEUNJOURQUELCO")

        fLOG("------------------ vraie")
        fLOG(memoire)
        fLOG("------------------ cle trouve par Babbage")
        fLOG("longueur ", l, " cle : ", cle_code)
        if memoire == cle_code:
            fLOG("bonne cle")
        else:
            fLOG("mauvaise cle")
        fLOG("------------------ message")
        fLOG(message[:200])
        fLOG("------------------ message code")
        fLOG(code[:200])
        fLOG("------------------ message decode")
        fLOG(decode[:200])
        fLOG("------------------")
        if decode == message:
            fLOG("message bien retranscrit")
        else:
            rows = []
            for i in range(0, len(decode)):
                if message[i] != decode[i]:
                    rows.append(
                        "{0}: {1} --- {2}".format(i, message[i], decode[i]))
            raise Exception("\n".join(rows))

    def test_vigenere_binary(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        text = b"abcdefghijklmdkjnlkfbqlbsdklbDKL2#33"
        cle = b"key"
        code = code_vigenere(text, cle, binary=True)
        deco = code_vigenere(code, cle, decode=True, binary=True)
        self.assertEqual(text, deco)


if __name__ == "__main__":
    unittest.main()

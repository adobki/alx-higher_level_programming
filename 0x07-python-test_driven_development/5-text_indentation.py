#!/usr/bin/python3
"""Module with a function, and some extra code for testing."""


def text_indentation(text):
    """Prints text with 2 lines after each of these characters: ., ? and :."""

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        for char in text[:]:
            if char in ('.', '?', ':'):
                print('\n')
            else:
                print(char, end='')


def main():
    """Tests the code."""

    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing\
     elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas\
     commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum\
    , sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi vid\
    eri nihil dolere. Transfer idem ad modestiam vel temperantiam, quae es\
    t moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde \
    sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid vole\
    s, postea. Quae animi affectio suum cuique tribuens atque hanc, quam d\
    ico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres""")


if __name__ == "__main__":
    main()

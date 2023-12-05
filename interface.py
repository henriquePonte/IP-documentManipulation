import constants
import text_processing


def menu():
    option = None
    text_file = text_processing.read_file('os_maias_eca_queiroz.txt')
    lexicon_file = text_processing.read_file('lexico_por_bra.txt')
    stop_file = text_processing.read_file('stopwords_pt.txt')

    while option != 0:
        print('Menu')
        print('1 - Gerar palavras')
        print('2 - Remover pontuação e números')
        print('3 - Palavras que não ocorrem no léxicos')
        print('4 - Remover as stopwords')
        print('5 - Calcular a frequência absoluta')
        print('6 - Calcular a frequência relativa')
        print('7- Gerar lista das palavras que ocorrem num determinado intervalo de frequências absolutas')
        print('8- Gerar lista das palavras que ocorrem num determinado intervalo de frequências relativas')
        print('0 - Sair')

        option = int(input('Escolha a opção do menu -> '))

        if option == 0:
            print("Saiu")

        elif option == 1:
            print("Texto: ", text_file)

        elif option == 2:
            text_file = text_processing.remove_punctuation_and_numbers(text_file, constants.PUNCTUATION,
                                                                       constants.NUMBERS)
            print("Palavras sem pontuação: ", text_file)

        elif option == 3:
            text_file = text_processing.remove_words(text_file, lexicon_file)

            print("Palavras que não ocorrem no léxico atual: ", text_file)

        elif option == 4:
            text_file = text_processing.remove_words(text_file, stop_file)

            print("Texto sem stopwords: ", text_file)

        elif option == 5:
            word_count, total_words = text_processing.calculate_absolute_frequency(text_file)

            print("Frequência absoluta das palavras: ", word_count)

        elif option == 6:
            word_count, total_words = text_processing.calculate_absolute_frequency(text_file)
            relative_frequency = text_processing.calculate_relative_frequency(word_count, total_words)

            print("Frequência relativa das palavras: ", relative_frequency)

        elif option == 7:
            min_absolute_frequency = int(input('Escolha um numero -> '))
            max_absolute_frequency = int(input('Escolha um numero -> '))
            words_within_absolute_range = text_processing.words_in_frequency_range(
                text_processing.count_words(text_file),
                min_absolute_frequency,
                max_absolute_frequency)

            print(f"Palavras que ocorrem entre {min_absolute_frequency} e {max_absolute_frequency}"
                  f" vezes: {words_within_absolute_range}")

        elif option == 8:
            min_relative_frequency = int(input('Escolha um numero -> '))
            max_relative_frequency = int(input('Escolha um numero -> '))
            word_count, total_words = text_processing.calculate_absolute_frequency(text_file)
            relative_frequency = text_processing.calculate_relative_frequency(word_count, total_words)
            words_within_relative_range = text_processing.words_in_relative_frequency_range(relative_frequency,
                                                                                            min_relative_frequency,
                                                                                            max_relative_frequency)

            print(f"Palavras que ocorrem entre {min_relative_frequency} "
                  f"e {max_relative_frequency} de frequência relativa: {words_within_relative_range}")

        else:
            print("Opção inválida. Tente novamente.")
